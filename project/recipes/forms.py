from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from project import images


class AddRecipeForm(Form):
    recipe_title = StringField('Recipe Title', validators=[DataRequired()])
    recipe_description = StringField('Recipe Description', validators=[DataRequired()])
    recipe_image = FileField('Recipe Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
