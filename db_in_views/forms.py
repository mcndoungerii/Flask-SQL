from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField("Remove Puppy")

class AddOwner(FlaskForm):
    
    id = IntegerField("Id of Puppy: ")
    name = StringField("Name of Owner: ")
    submit = SubmitField("Add Owner")

class UpdateForm(FlaskForm):

    id = IntegerField("Id of Puppy: ")
    name = StringField("Name of Puppy: ")
    submit = SubmitField("Update Puppy")