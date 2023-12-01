from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, validators, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, URL
from datetime import datetime
from wtforms.validators import ValidationError


#dj325 20/11/23 
class movieSearchForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=3, max=128)])
    submit = SubmitField("Find")
class movieForm(FlaskForm):
    id = StringField('ID', render_kw={"disabled": True})
    api_id = StringField('API ID', render_kw={"disabled": True})
    title = StringField('Movie Name', validators=[Length(min=3, max=128, message="Title is required"),DataRequired(message="Movie name is required")])
    title_type = SelectField('Type' , choices=[('',"Select"),('Movie',"Movie"),("Music Video","Music Video"),("Podcast Episode","Podcast Episode"),("Podcast Series","Podcast Series"),("Short","Short")
                                    ,("TV Episode","TV Episode"),("TV Mini Series","TV Mini Series"),("TV Movie","TV Movie"),("TV Pilot","TV Pilot"),("TV Series","TV Series"),("TV Short","TV Short"),("TV Special","TV Special")
                                    ,("Video","Video"),("Video Game","Video Game")] , validators=[DataRequired(message="Movie type is required")])
    # title_type = StringField('Type', [validators.Length(min=1, max=16)])
    release_date = DateField('Release Date', format='%Y-%m-%d', validators=[DataRequired(message="Missing Date")])
    image_url = StringField('Image URL', validators=[ URL(message="Invalid URL format")])
    created = StringField('Created Date', render_kw={"disabled": True})
    modified = StringField('Modified Date', render_kw={"disabled": True})
    submit = SubmitField("Save")


class movieFilterForm(FlaskForm):
    title = StringField("Name", [Optional()])
    title_type = SelectField('Type',[Optional()] ,choices=[('',"Select"),('Movie',"Movie"),("Music Video","Music Video"),("Podcast Episode","Podcast Episode"),("Podcast Series","Podcast Series"),("Short","Short")
                                    ,("TV Episode","TV Episode"),("TV Mini Series","TV Mini Series"),("TV Movie","TV Movie"),("TV Pilot","TV Pilot"),("TV Series","TV Series"),("TV Short","TV Short"),("TV Special","TV Special")
                                    ,("Video","Video"),("Video Game","Video Game")])
    release_dateStart = DateField('Release Date Start',format='%Y-%m-%d')
    release_dateEnd = DateField('Release Date End',format='%Y-%m-%d', default=datetime.today())
    sort = SelectField("Sort", [Optional()], choices=[('', 'Not Selected'), ("title", "Title"),("title_type","Type"),("release_date","Release Date")] , default="")
    order = SelectField("Order", [Optional()], choices=[("asc","Low to High"), ("desc","High to Low")])
    limit = IntegerField("Limit", [Optional(), NumberRange(min=1, max=100)], default=10)
    submit = SubmitField("Search")

class associationsFilterForm(FlaskForm):
    title = StringField("Title", [Optional()])
    user_name = StringField("User Name", [Optional()])
    submit = SubmitField("Search")