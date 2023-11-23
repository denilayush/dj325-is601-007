from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, validators, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from datetime import datetime

#dj325 20/11/23 
class movieSearchForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=10)])
    submit = SubmitField("Find")
class movieForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=128)])
    titleType = StringField('Type', [validators.Length(min=1, max=16)])
    releaseDate = StringField('Release Date (YYYY-MM-DD)', [validators.Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Invalid date format")])
    imageUrl = StringField('Image URL', [validators.Length(min=1, max=256)])
    submit = SubmitField("Save")


class movieFilterForm(FlaskForm):
    title = StringField("Title", [Optional()])
    titleType = StringField('Type', [Optional()])
    releaseDateStart = DateField('Release Date Start',format='%Y-%m-%d')
    releaseDateEnd = DateField('Release Date End',format='%Y-%m-%d', default=datetime.today())
    sort = SelectField("Columns", [Optional()], choices=[("title", "Title"),("titleType","TitleType"),("releaseDate","ReleaseDate")])
    order = SelectField("Order", [Optional()], choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Search")