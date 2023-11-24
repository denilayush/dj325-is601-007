from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, validators, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, URL
from datetime import datetime
from wtforms.validators import ValidationError


#dj325 20/11/23 
class movieSearchForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=10)])
    submit = SubmitField("Find")
class movieForm(FlaskForm):
    id = StringField('ID', render_kw={"disabled": True})
    api_id = StringField('API ID', render_kw={"disabled": True})
    title = StringField('Title', [validators.Length(min=1, max=128)])
    title_type = SelectField('Type' , choices=[('movie',"movie"),("musicVideo","musicVideo"),("podcastEpisode","podcastEpisode"),("podcastSeries","podcastSeries"),("short","short")
                                    ,("tvEpisode","tvEpisode"),("tvMiniSeries","tvMiniSeries"),("tvMovie","tvMovie"),("tvPilot","tvPilot"),("tvSeries","tvSeries"),("tvShort","tvShort"),("tvSpecial","tvSpecial")
                                    ,("video","video"),("videoGame","videoGame")] )
    title_type = StringField('Type', [validators.Length(min=1, max=16)])
    release_date = StringField('Release Date (YYYY-MM-DD)', [validators.Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Invalid date format")])
    image_url = StringField('Image URL', [ URL(message="Invalid URL format")])
    created = StringField('Created Date', render_kw={"disabled": True})
    modified = StringField('Modified Date', render_kw={"disabled": True})
    submit = SubmitField("Save")


class movieFilterForm(FlaskForm):
    title = StringField("Title", [Optional()])
    title_type = StringField('Type', [Optional()])
    release_dateStart = DateField('Release Date Start',format='%Y-%m-%d')
    release_dateEnd = DateField('Release Date End',format='%Y-%m-%d', default=datetime.today())
    sort = SelectField("Columns", [Optional()], choices=[("title", "Title"),("title_type","Type"),("release_date","Release Date")])
    order = SelectField("Order", [Optional()], choices=[("asc","+"), ("desc","-")])
    limit = IntegerField("Limit", [Optional(), NumberRange(min=1, max=100)], default=10)
    submit = SubmitField("Search")