from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from movies.forms import movieForm, movieSearchForm, movieFilterForm, associationsFilterForm # Import movieForm class
from roles.permissions import admin_permission
from flask_login import login_user, login_required, logout_user, current_user

movies = Blueprint('movies', __name__, url_prefix='/movies', template_folder='templates')

#dj325 20/11/23 
@movies.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = movieSearchForm()
    if form.validate_on_submit():
        try:
            from utils.movies import movies
            from utils.lazy import DictToObject
            
            # Fetch movie data
            result = movies.get_movie(form.title.data)
            #print(f"Debug: Result: {result}")
            
            if result and result['results']:
                countForNumberOfInsertion = 0
                for movie in result['results']:
                    # Fetching the movie from results
                    #print(f"Debug: Movie: {movie}")
                    try:
                        # Formating the release date
                        release_date = f"{movie['releaseDate']['year']}-{movie['releaseDate']['month']}-{movie['releaseDate']['day']}"
                        #dj325 20/11/23 
                        if movie['primaryImage'] is not None:  # Checking if primaryImage is not None
                            query = """
                                INSERT INTO IS601_Movies (api_id, title, title_type, release_date, image_url)
                                VALUES (%s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                api_id = VALUES(api_id),
                                title = VALUES(title),
                                title_type = VALUES(title_type),
                                release_date = VALUES(release_date),
                                image_url = VALUES(image_url)
                            """

                            db_insert_result = DB.insertOne(
                                query,
                                movie['id'],
                                movie['originalTitleText']['text'],
                                movie['titleType']['text'],
                                release_date,
                                movie['primaryImage']['url']
                            )
                            #print("result",db_insert_result)
                            if db_insert_result:  # Checking if insertion was successful
                                countForNumberOfInsertion+=1
                            
                        
                    except Exception as e:
                        pass
                if countForNumberOfInsertion>0:
                    flash(f"Loaded {countForNumberOfInsertion} movies", "success")
                else:
                    flash(f"Not loaded any movies", "success")

            else:
                flash("No results found for the movie", "warning")
        except Exception as e:
            flash(f"Error loading movies record: {e}", "danger")
    return render_template("movie_search.html", form=form)

#dj325 20/11/23 
@movies.route("/list", methods=["GET"])
#@admin_permission.require(http_exception=403)
def list():
    searchForm = movieFilterForm(request.args)
    query = "SELECT id, api_id, title, title_type, release_date, image_url FROM IS601_Movies WHERE 1 = 1"
    args = {}
    if searchForm.title.data:
        query += " AND title LIKE %(title)s"
        args["title"] = f"%{searchForm.title.data}%"

    if searchForm.title_type.data:
        query += " AND title_type LIKE %(title_type)s"
        args["title_type"] = f"{searchForm.title_type.data}"
    
    if searchForm.release_dateStart.data and searchForm.release_dateEnd.data :
        query += " AND release_date >= %(release_dateStart)s AND release_date <= %(release_dateEnd)s"
        args["release_dateStart"] = f"{searchForm.release_dateStart.data}"
        args["release_dateEnd"] = f"{searchForm.release_dateEnd.data}"
    
    # dj325 27/11/23
    if searchForm.sort.data and searchForm.order.data:
        query += f" ORDER BY {searchForm.sort.data} {searchForm.order.data}"
    
    if searchForm.limit.data:
        if searchForm.limit.data >100 or searchForm.limit.data<1:
            searchForm.limit.data = 10
            query += f" LIMIT 10"
        else:
            query += f" LIMIT {searchForm.limit.data}"
    else:
        query += f" LIMIT 10"

    if searchForm.validate_on_submit():
        pass
    else:
        print(searchForm.errors)
    
    rows = []
    print(query,args)
    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting movie records", "danger")
    #print(rows[0])
    return render_template("movies_list.html", rows=rows, form=searchForm,current_user=current_user,page="list")

#dj325 20/11/23 
@movies.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = movieForm()
    if form.validate_on_submit():
        try:
            # print(form.title.data.lower(), form.title_type.data.lower(), form.release_date.data)
            query = f"SELECT title, title_type, release_date FROM IS601_Movies WHERE LOWER(title) = '{str(form.title.data.lower())}' AND LOWER(title_type) = '{str(form.title_type.data.lower())}' AND release_date = '{str(form.release_date.data)}'"
            print(query)
            result = DB.selectAll(query, {}
            )
            # print(result)
            if result.status and result.rows[0]:
                flash("Already Available","warning")
        except Exception as e:
            print(e)
            try:
                # Create a new movie record in the database
                result = DB.insertOne(
                    "INSERT INTO IS601_Movies (title, title_type, release_date, image_url) VALUES (%s, %s, %s, %s)",
                    form.title.data, form.title_type.data, form.release_date.data, form.image_url.data
                )
                if result.status:
                    flash(f"Created movie record for {form.title.data}", "success")
            except Exception as e:
                flash(f"Error creating movie record: {e}", "danger")
    return render_template("movie_form.html", form=form, type="Create")


#dj325 20/11/23 
@movies.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = movieForm()
    id = request.args.get("id")
    print(form.image_url.errors)
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("movies.list"))
    if form.validate_on_submit() and id:
        try:
            # print(form.title.data.lower(), form.title_type.data.lower(), form.release_date.data)
            query = f"SELECT title, title_type, release_date, image_url FROM IS601_Movies WHERE LOWER(title) = '{str(form.title.data.lower())}' AND LOWER(title_type) = '{str(form.title_type.data.lower())}' AND release_date = '{str(form.release_date.data)}' AND image_url = '{str(form.image_url.data)}'"
            print(query)
            result = DB.selectAll(query, {}
            )
            # print(result)
            if result.status and result.rows[0]:
                flash("Already Available","warning")
        except Exception as e:
            print(e)
            try:
                # Update the existing movie record in the database
                result = DB.insertOne(
                    "UPDATE IS601_Movies SET title = %s, title_type = %s, release_date = %s, image_url = %s WHERE id = %s",
                    form.title.data, form.title_type.data, form.release_date.data, form.image_url.data, id
                )
                if result.status:
                    flash(f"Updated movie record for {form.title.data}", "success")
            except Exception as e:
                flash(f"Error updating movie record: {e}", "danger")
    #dj325 28/11/23 #error on submiting the edit form 
    else:
        print("Form Errors:", form.errors)
        if len(form.errors) >0:
            return render_template("movie_form.html", form=form, type="Edit")
    try:
        result = DB.selectOne(
            "SELECT id, api_id , title, title_type, release_date, image_url, created, modified FROM IS601_Movies WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = movieForm(data=result.row)
    except Exception as e:
        flash("Error fetching movie record", "danger")
    print(form.image_url.errors)
    return render_template("movie_form.html", form=form, type="Edit")

def check_association(user_id,id):
    #user association Check 
    # dj325 28-11-23
    try:
        result = DB.selectOne(
            "SELECT movie_id, user_id  FROM IS601_UsersAssociation WHERE movie_id = %s AND user_id = %s AND is_active = 1",
            int(id) , int(user_id)
        )
        print(result,result.row)
        if result.status and len(result.row)>0:
            return True
        else:
            False
    except:
        print("Not associated with this movie")
        return False
    # User Association Check -----Ends

#dj325 20/11/23 
@movies.route("/view", methods=["GET"])
def view():
    id = request.args.get("id")
    page = request.args.get("page")
    user_id = current_user.get_id()
    print("Movie id: ",id," User Id: ",user_id)
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("movies.list"))
    try:
        result = DB.selectOne(
            "SELECT id, api_id, title, title_type, release_date, image_url FROM IS601_Movies WHERE id = %s",
            id
        )
        
        if result.status and result.row :
            #user association Check 
            # dj325 28-11-23
            association = check_association(user_id,id)
            return render_template("movie_view.html", movie=result.row,current_user=current_user, movie_id = id, association = association,page=page)
        else:
            flash("Movie record not found", "danger")
    except Exception as e:
        print(f"Movie error {e}")
        flash("Error fetching Movie record", "danger")
    if page == "notassociated":
        return redirect(url_for("movies.notassociated"))
    
    
    return redirect(url_for("movies.list"))

#dj325 20/11/23 
@movies.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            # Delete the movie associations first record from the database
            result = DB.delete("DELETE FROM IS601_UsersAssociation WHERE movie_id = %s", id)
            if result.status:    
            # Delete the movie record from the database
                result = DB.delete("DELETE FROM IS601_Movies WHERE id = %s", id)
                if result.status:
                    flash("Deleted movie record", "success")
        except Exception as e:
            flash(f"Error deleting movie record: {e}", "danger")
        del args["id"]
    else:
        flash("No ID present", "warning")
    # return redirect(url_for("movies.list", **args))
    # updated this to get back to the same query
    query_params = request.referrer
    return redirect(query_params)



#dj325 28/11/23 watchlater route for list
@movies.route("/watch", methods=["GET"])
#@admin_permission.require(http_exception=403)
def watch():
    args = {}
    rows = []
    #dj325 30/11/23 Added search filters
    searchForm = movieFilterForm(request.args)
    user_id = current_user.get_id()
    query = """ SELECT m.id, m.api_id, m.title, m.title_type, m.release_date, m.image_url
            FROM 
                IS601_UsersAssociation AS ua
            JOIN 
                IS601_Movies AS m ON ua.movie_id = m.id
            WHERE 
                ua.user_id = %(user_id)s AND ua.is_active = 1"""
    args["user_id"] = f"{user_id}"

    if searchForm.title.data:
        query += " AND m.title LIKE %(title)s"
        args["title"] = f"%{searchForm.title.data}%"

    if searchForm.title_type.data:
        query += " AND m.title_type LIKE %(title_type)s"
        args["title_type"] = f"{searchForm.title_type.data}"
    
    if searchForm.release_dateStart.data and searchForm.release_dateEnd.data :
        query += " AND m.release_date >= %(release_dateStart)s AND m.release_date <= %(release_dateEnd)s"
        args["release_dateStart"] = f"{searchForm.release_dateStart.data}"
        args["release_dateEnd"] = f"{searchForm.release_dateEnd.data}"
    
    # dj325 27/11/23
    if searchForm.sort.data and searchForm.order.data:
        query += f" ORDER BY {searchForm.sort.data} {searchForm.order.data}"
    
    # removing this because I will use a limit in rows
    # if searchForm.limit.data:
    #     if searchForm.limit.data >100 or searchForm.limit.data<1:
    #         searchForm.limit.data = 10
    #         query += f" LIMIT 10"
    #     else:
    #         query += f" LIMIT {searchForm.limit.data}"
    # else:
    #     query += f" LIMIT 10"

    if searchForm.validate_on_submit():
        pass
    else:
        print(searchForm.errors)

    print(query,args)
    try:
        result = DB.selectAll(query, args)
        print(result.status)
        if result.status and result.rows:
            rows = result.rows
            movies_count = " - "+str(len(rows))+" movies "
            print(rows)
        else:
            movies_count="- No movies to display"
    except Exception as e:
        print(e)
        flash("Error getting movie records", "danger")
    #print(rows[0])
    if searchForm.limit.data:
        limit = searchForm.limit.data
    else:
        limit = 10
    return render_template("watch_list.html", rows=rows[:limit], current_user=current_user,movies_count=movies_count,form=searchForm, page="watch")

#dj325 28/11/23 page for assiciation of a movie to a user
@movies.route("/associate", methods=["GET"])
# @admin_permission.require(http_exception=403)
def associate():
    id = request.args.get("id")
    page = request.args.get("page")
    args = {**request.args}
    user_id = current_user.get_id()
    if id:
        try:
            # Delete the movie record from the database
            result = DB.insertOne("INSERT INTO IS601_UsersAssociation (movie_id, user_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE is_active = !is_active", id,user_id)
            print(result.status)
            if result.status:
                if page == "view_add":
                    flash("Movie Added to Watch Later", "success")
                elif page == "view_remove":
                    flash("Movie Removed From Watch Later", "success")
        except Exception as e:
            # if "Duplicate entry" in str(e):
            #     flash("Already Added to watch later","success")
            # else:
            flash(f"Error Adding to Watch Later: {e}", "danger")
    else:
        flash("No ID present for Association", "warning")
    # return redirect(url_for("movies.list", **args))
    # updated this to get back to the same query
    if page and "view" in page:
        return redirect(url_for("movies.view",**args))
    if page and page == "watch":
        return redirect(url_for("movies.watch",**args))
    query_params = request.referrer
    return redirect(url_for("movies.list"))

#dj325 30/11/23 remove all watch list items
@movies.route("/remove", methods=["GET"])
# @admin_permission.require(http_exception=403)
def remove():
    user_id = current_user.get_id()
    args = {**request.args}
    if id:
        try:
            # Update the all is_active columns from 1 to 0
            result = DB.update("UPDATE IS601_UsersAssociation SET is_active = 0 WHERE user_id = %s;",user_id)
            if result.status:
                flash("Removed all the movies from Watch List", "success")
        except Exception as e:
            flash(f"Error deleting movie record: {e}", "danger")
    else:
        flash("Something went wrong", "warning")
    # return redirect(url_for("movies.list", **args))
    # updated this to get back to the same query
    query_params = request.referrer
    return redirect(url_for("movies.watch"))



# dj325 30/11/23
#all users association page.
@movies.route("/associations", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def associations():
    searchForm = associationsFilterForm(request.args)
    query = """SELECT m.id AS movie_id, u.id AS user_id , m.title AS watch_list_movies, m.image_url, u.username AS user_name, user_counts.total_count
    FROM IS601_Movies m
    LEFT JOIN IS601_UsersAssociation ua ON m.id = ua.movie_id AND ua.is_active = 1
    LEFT JOIN IS601_Users u ON ua.user_id = u.id
    LEFT JOIN (
        SELECT movie_id, COUNT(user_id) AS total_count
        FROM IS601_UsersAssociation
        WHERE is_active = 1
        GROUP BY movie_id
    ) AS user_counts ON m.id = user_counts.movie_id
    WHERE ua.user_id IS NOT NULL
    """
    args = {}
    rows = []
    # dj325 01/12/23
    if searchForm.title.data:
        query += " AND m.title LIKE %(title)s"
        args["title"] = f"%{searchForm.title.data}%"
    if searchForm.user_name.data:
        query += " AND u.username LIKE %(user_name)s"
        args["user_name"] = f"%{searchForm.user_name.data}%"

    query += " GROUP BY m.id, m.title, m.image_url, u.username, user_counts.total_count"
    if searchForm.limit.data and searchForm.limit.data>0 and searchForm.limit.data<=100:
        limit = searchForm.limit.data
        query+= f" LIMIT {limit}"
    else:
        limit = 10
        query+= f" LIMIT 10"

    print(query,args)
    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
            print("debug", rows)
        count = DB.selectOne(""" SELECT COUNT(m.id) AS `count`
    FROM IS601_Movies m
    LEFT JOIN IS601_UsersAssociation ua ON m.id = ua.movie_id AND ua.is_active = 1
    LEFT JOIN IS601_Users u ON ua.user_id = u.id
    LEFT JOIN (
        SELECT movie_id, COUNT(user_id) AS total_count
        FROM IS601_UsersAssociation
        WHERE is_active = 1
        GROUP BY movie_id
    ) AS user_counts ON m.id = user_counts.movie_id
    WHERE ua.user_id IS NOT NULL LIMIT 0,100""" , )
        if count.status:
            TotalCount = count.row["count"]
    except Exception as e:
        print(e)
        flash("Error getting movie records", "danger")
    
    #print(rows[0])
    return render_template("associations_list.html", rows=rows,page="list",associations_count = str(TotalCount), form=searchForm)


#dj325 01/12/23 page for assiciation of a movie to a user
@movies.route("/dissociate", methods=["GET"])
@admin_permission.require(http_exception=403)
def dissociate():
    id = request.args.get("id")
    page = request.args.get("page")
    args = {**request.args}
    user_id = request.args.get("user_id")
    if id:
        try:
            # Delete the movie record from the database
            result = DB.insertOne("INSERT INTO IS601_UsersAssociation (movie_id, user_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE is_active = !is_active", id,user_id)
            print(result.status)
            if result.status:
                flash("Successfully removed movie from user's watchlist","success")
        except Exception as e:
            # if "Duplicate entry" in str(e):
            #     flash("Already Added to watch later","success")
            # else:
            flash(f"Error Adding to Watch Later: {e}", "danger")
    else:
        flash("No ID present for Association", "warning")
    # return redirect(url_for("movies.list", **args))
    # updated this to get back to the same query
    return redirect(url_for("movies.associations"))


# dj325 01/12/23
# page for movie that is not associated with any users.
@movies.route("/notassociated", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def notassociated():
    searchForm = movieFilterForm(request.args)
    query = """SELECT m.id, m.title AS movie_title, title_type, release_date, image_url
FROM IS601_Movies m
LEFT JOIN IS601_UsersAssociation ua ON m.id = ua.movie_id AND ua.is_active = 1
WHERE ua.movie_id IS NULL 
    """
    args = {}
    rows = []
    TotalCount = 0
    # dj325 01/12/23
    if searchForm.title.data:
        query += " AND m.title LIKE %(title)s"
        args["title"] = f"%{searchForm.title.data}%"

    if searchForm.title_type.data:
        query += " AND m.title_type LIKE %(title_type)s"
        args["title_type"] = f"{searchForm.title_type.data}"
    
    if searchForm.release_dateStart.data and searchForm.release_dateEnd.data :
        query += " AND m.release_date >= %(release_dateStart)s AND m.release_date <= %(release_dateEnd)s"
        args["release_dateStart"] = f"{searchForm.release_dateStart.data}"
        args["release_dateEnd"] = f"{searchForm.release_dateEnd.data}"
    
    # dj325 01/12/23
    if searchForm.sort.data and searchForm.order.data:
        query += f" ORDER BY {searchForm.sort.data} {searchForm.order.data}"
    if searchForm.limit.data:
        limit = searchForm.limit.data
        query+= f" LIMIT {limit}"
    else:
        query+= " LIMIT 10"
    if searchForm.validate_on_submit():
        pass
    else:
        print(searchForm.errors)
    
    print(query,args)
    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
            print("debug", rows)
        count = DB.selectOne("""SELECT COUNT(m.id) AS `count`
        FROM IS601_Movies m
        LEFT JOIN IS601_UsersAssociation ua ON m.id = ua.movie_id AND ua.is_active = 1
        WHERE ua.movie_id IS NULL """,)
        TotalCount = count.row["count"]
        # print(TotalCount,"This is total count")
    except Exception as e:
        print(e)
        flash("Error getting movie records", "danger")
    
    #print(rows[0])
    return render_template("not_associated_list.html", rows=rows,page="notassociated",not_associations_count = str(TotalCount), form=searchForm)



# dj325 01/12/23
# assign page for admin to associate movies with users

@movies.route("/assign", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def assign():
    users = []
    movies = []

    username = request.args.get("username")
    title = request.args.get("title")
    if username:
        try:
            result = DB.selectAll("""
            SELECT id, username, 
                (SELECT GROUP_CONCAT( title, ' (' , IF(ua.is_active = 1,'active','inactive') , ')') from 
                IS601_UsersAssociation ua JOIN IS601_Movies on ua.movie_id = IS601_Movies.id WHERE ua.user_id = IS601_Users.id) as watchlist
            FROM IS601_Users where username like %s limit 25
            
            """, f"%{username}%")
            if result.status and result.rows:
                users = result.rows
        except Exception as e:
            flash(str(e), "danger")
    if title:
        try:
            query = "SELECT id, title FROM IS601_Movies WHERE 1 = 1"
            if title:
                query+=f" AND title LIKE '%{title}%'"
            query+= " LIMIT 25"
            print(query)
            result = DB.selectAll(query,)
            if result.status and result.rows:
                movies = result.rows
        except Exception as e:
            flash(str(e),"danger")
    return render_template("movies_assign.html", users=users, movies=movies)

@movies.route("/apply", methods=["POST"])
@admin_permission.require(http_exception=403)
def apply():
    # https://stackoverflow.com/a/24808706
    users = request.form.getlist("users[]")
    movies = request.form.getlist("movies[]")
    print(users, movies)
    args = {**request.args}
    if users and movies: # we need both for this to work
        mappings = []
        for user in users:
            for movie in movies:
                print(user, movie)
                mappings.append((int(user), int(movie)))
        if len(mappings) > 0:
            try:
                result = DB.insertMany("INSERT INTO IS601_UsersAssociation (user_id, movie_id, is_active) VALUES(%s, %s, 1) ON DUPLICATE KEY UPDATE is_active = !is_active", mappings)
                if result.status:
                    flash(f"Successfully Added/Removed movies for the user/movies {len(mappings)} mappings", "success")
            except Exception as e:
                flash(str(e), "danger")
        else:
            flash("No user/movie mappings", "danger")

    if "users" in args:
        del args["users"]
    if "movies" in args:
        del args["movies"]
    return redirect(url_for("movies.assign", **args))




@movies.route("/profileview", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def profileview():
    id = request.args.get("id")
    if id:
        try:
            result = DB.selectOne(
                "SELECT username,created,modified FROM IS601_Users WHERE id = %s",
                id
            )
            if result.status :
                row = result.row
                print(row)
        except Exception as e:
            flash(str(e),"danger")
            return redirect(url_for("movies.associations"))
    else:
        flash("No id","danger")
        return redirect(url_for("movies.associations"))
    return render_template("profile_view.html",row=row)