import os
from flask import Flask, url_for,redirect,render_template,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import AddForm,UpdateForm,DelForm, AddOwner

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = "mysecret"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)


########################################
####### Models #########################

class Puppy(db.Model):

    __tablename__ = "puppies"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    breed = db.Column(db.Text)
    owner = db.relationship('Owners',backref='puppy',uselist=False)

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        if self.owner:
            return f"Puppy's name is {self.name} of Breed {self.breed} and Owner's name is {self.owner.name}"
        else:
            return f"Puppy's name is {self.name} of Breed {self.breed} and has no owner yet!"

class Owners(db.Model):
    
    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id


db.create_all()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET','POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        breed = form.breed.data

        pup_model = Puppy(name,breed)

        db.session.add(pup_model)
        db.session.commit()
        flash(f"Puppy {name} have been added successful")

        return redirect(url_for('list_pup'))
    
    return render_template('add.html',form=form)

@app.route('/list',methods=['GET'])
def list_pup():
    
    puppies = Puppy.query.all()
    # flash(f"Here are the puppies")

    return render_template('list.html',puppies=puppies)

@app.route('/update',methods=['GET','POST'])
def update_pup():

    form = UpdateForm()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        breed = form.breed.data

        print(f"Breed is {breed}")

        puppy = Puppy.query.get(id)

        print(f"Puppy is {puppy}")

        puppy.name = name

        if len(breed) > 0:
            puppy.breed = breed
        

        
        db.session.commit()
        flash(f"Puppy {name} have been updated successful")
        return redirect(url_for('list_pup'))
    return render_template('update.html',form=form)

@app.route('/delete',methods=['GET','POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        puppy_to_delete = Puppy.query.get(id)
        db.session.delete(puppy_to_delete)
        db.session.commit()
        flash(f"Puppy of Id {id} have been deleted successful")
        return redirect(url_for('list_pup'))
    
    return render_template('delete.html',form=form)

@app.route('/add_owner', methods=['GET','POST'])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data

        owner_model = Owners(name,id)

        db.session.add(owner_model)
        db.session.commit()
        flash(f"Owner {name} have been added successful")
        return redirect(url_for('list_pup'))
    
    return render_template('owner.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)