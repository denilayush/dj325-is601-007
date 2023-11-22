from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from movies.forms import movieForm, movieSearchForm, movieFilterForm  # Import your movieForm class
from roles.permissions import admin_permission

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
                        
                        if movie['primaryImage'] is not None:  # Checking if primaryImage is not None
                            query = """
                                INSERT INTO IS601_Movies (apiId, title, titleType, releaseDate, imageUrl)
                                VALUES (%s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                apiId = VALUES(apiId),
                                title = VALUES(title),
                                titleType = VALUES(titleType),
                                releaseDate = VALUES(releaseDate),
                                imageUrl = VALUES(imageUrl)
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
@admin_permission.require(http_exception=403)
def list():
    searchForm = movieFilterForm(request.args)
    query = "SELECT id, apiId, title, titleType, releaseDate, imageUrl FROM IS601_Movies WHERE 1 = 1"
    args = {}
    if searchForm.title.data:
        query += " AND title LIKE %(title)s"
        args["title"] = f"%{searchForm.title.data}%"

    if searchForm.titleType.data:
        query += " AND titleType LIKE %(titleType)s"
        args["titleType"] = f"%{searchForm.titleType.data}%"
    

    query += " LIMIT 100"
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
    return render_template("movies_list.html", rows=rows, form=searchForm)

#dj325 20/11/23 
@movies.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = movieForm()
    if form.validate_on_submit():
        try:
            # Create a new movie record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Movies (title, titleType, releaseDate, imageUrl) VALUES (%s, %s, %s, %s)",
                form.title.data, form.titleType.data, form.releaseDate.data, form.imageUrl.data
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
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("movies.list"))
    if form.validate_on_submit() and id:
        try:
            # Update the existing movie record in the database
            result = DB.insertOne(
                "UPDATE IS601_Movies SET title = %s, titleType = %s, releaseDate = %s, imageUrl = %s WHERE id = %s",
                form.title.data, form.titleType.data, form.releaseDate.data, form.imageUrl.data, id
            )
            if result.status:
                flash(f"Updated movie record for {form.title.data}", "success")
        except Exception as e:
            flash(f"Error updating movie record: {e}", "danger")
    try:
        result = DB.selectOne(
            "SELECT title, titleType, releaseDate, imageUrl FROM IS601_Movies WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = movieForm(data=result.row)
    except Exception as e:
        flash("Error fetching movie record", "danger")
    return render_template("movie_form.html", form=form, type="Edit")


#dj325 20/11/23 
@movies.route("/view", methods=["GET"])
def view():
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("movies.list"))
    try:
        result = DB.selectOne(
            "SELECT title, titleType, releaseDate, imageUrl FROM IS601_Movies WHERE id = %s",
            id
        )
        if result.status and result.row:
            return render_template("movie_view.html", movie=result.row)
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
    return redirect(url_for("movies.list", **args))