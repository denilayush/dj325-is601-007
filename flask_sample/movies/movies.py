from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from movies.forms import movieForm, movieSearchForm, movieFilterForm  # Import your movieForm class
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
        
        if result.status and result.row:
            #user association Check 
            # dj325 28-11-23
            association = check_association(user_id,id)
            return render_template("movie_view.html", movie=result.row,current_user=current_user, movie_id = id, association = association,page=page)
        else:
            flash("Movie record not found", "danger")
    except Exception as e:
        print(f"Movie error {e}")
        flash("Error fetching Movie record", "danger")
    
    return redirect(url_for("movies.list"))

#dj325 20/11/23 
@movies.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
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

    print(query,args)
    try:
        result = DB.selectAll(query, args)
        print(result.status)
        if result.status and result.rows:
            rows = result.rows
            movies_count = " - "+str(len(rows))+" movies in the list"
            print(rows)
        else:
            movies_count="- No movies to display"
    except Exception as e:
        print(e)
        flash("Error getting movie records", "danger")
    #print(rows[0])
    return render_template("watch_list.html", rows=rows, current_user=current_user,movies_count=movies_count,form=searchForm, page="watch")

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
    if "view" in page:
        return redirect(url_for("movies.view",**args))
    if page == "watch":
        return redirect(url_for("movies.watch",**args))
    query_params = request.referrer
    return redirect(url_for("query_params"))