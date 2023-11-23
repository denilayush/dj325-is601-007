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
    title_type = StringField('Type', [validators.Length(min=1, max=16)])
    release_date = StringField('Release Date (YYYY-MM-DD)', [validators.Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Invalid date format")])
    image_url = StringField('Image URL', [validators.Length(min=1, max=256)])
    submit = SubmitField("Save")


class movieFilterForm(FlaskForm):
    title = StringField("Title", [Optional()])
    title_type = StringField('Type', [Optional()])
    release_dateStart = DateField('Release Date Start',format='%Y-%m-%d')
    release_dateEnd = DateField('Release Date End',format='%Y-%m-%d', default=datetime.today())
    sort = SelectField("Columns", [Optional()], choices=[("title", "Title"),("title_type","Type"),("release_date","Release Date")])
    order = SelectField("Order", [Optional()], choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Search")