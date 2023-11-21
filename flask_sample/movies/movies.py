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
            # Create a new movie record in the database
            result = movies.quote(form.title.data)
            if result:
                result = DictToObject(result)
                result = DB.insertOne(
                    """INSERT INTO IS601_Movies (apiId, title, titleType, releaseDate, imageUrl)
                        VALUES (%s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        apiId = VALUES(apiId),
                        title = VALUES(title),
                        titleType = VALUES(titleType),
                        releaseDate = VALUES(releaseDate),
                        imageUrl = VALUES(imageUrl)
                        """,
                    result.title, result.tilteType, result.releaseDate, result.imageUrl
                )
                if result.status:
                    flash(f"Loaded movies record for {form.tilte.data}", "success")
        except Exception as e:
            flash(f"Error loading movies record: {e}", "danger")
    return render_template("movie_search.html", form=form)
