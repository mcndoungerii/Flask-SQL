from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField("Name of Puppy: ",validators=[DataRequired()])
    breed = StringField("Breed: ",validators=[DataRequired()])
    submit = SubmitField("Add Puppy")


class DelForm(FlaskForm):

    id = IntegerField("Id of Puppy: ",validators=[DataRequired()])
    submit = SubmitField("Delete Puppy")


class UpdateForm(FlaskForm):

    id = IntegerField("Id of Puppy: ", validators=[DataRequired()])
    name =  StringField("Puppy new name: ", validators=[DataRequired()])
    breed = StringField("Breed: ")
    submit = SubmitField("Update Puppy")

class AddOwner(FlaskForm):

    name = StringField("Owner's Name: ", validators=[DataRequired()])
    id = IntegerField("Puppy's Id: ", validators=[DataRequired()])
    submit = SubmitField("Add Owner")