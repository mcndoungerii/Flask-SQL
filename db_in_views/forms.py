from logging.config import valid_ident
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ',validators=[DataRequired()])
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove: ',validators=[DataRequired()])
    submit = SubmitField("Remove Puppy")

class AddOwner(FlaskForm):
    
    id = IntegerField("Id of Puppy: ", validators=[DataRequired()])
    name = StringField("Name of Owner: ",validators=[DataRequired()])
    submit = SubmitField("Add Owner")

class UpdateForm(FlaskForm):

    id = IntegerField("Id of Puppy: ",validators=[DataRequired()])
    name = StringField("Name of Puppy: ",validators=[DataRequired()])
    submit = SubmitField("Update Puppy")