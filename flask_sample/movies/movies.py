from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from movies.forms import movieForm, movieSearchForm  # Import your movieForm class
from roles.permissions import admin_permission

movies = Blueprint('movies', __name__, url_prefix='/movies', template_folder='templates')

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
            print(f"Debug: Result: {result}")
            
            if result and result['results']:
                countForNumberOfInsertion = 0
                for movie in result['results']:
                    # Fetching the movie from results
                    print(f"Debug: Movie: {movie}")
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

@movies.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        result = DB.selectAll("SELECT apiId, title, titleType, releaseDate, imageUrl FROM IS601_Movies LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting movie records", "danger")
    print(rows[0])
    return render_template("movies_list.html", rows=rows)
