from feedo import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
## , UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name     = db.Column(db.String(20), unique=False, nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    bio = db.Column(db.String(20), default='Tell people about yourself.')
    password = db.Column(db.String(60), nullable=False)
    #feedback = db.relationship('Feedback', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.name}', '{self.email}')"


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    #sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender_username = db.Column(db.String(20), nullable=False)                 #= current_user.name      #f_key
    recevier_username = db.Column(db.String(20), nullable=False)               #= name                   #f_key
    message =  db.Column(db.String(20), nullable=False)       
    message_time =  db.Column(db.DateTime, nullable=False, default= datetime.utcnow)           

    def __repr__(self):
        return f"Feedback('{self.sender_username}', '{self.recevier_username}', '{self.message}')"
    

class Rate(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True) #easy
    sender_username = db.Column(db.String(20), nullable=False)
    recevier_username = db.Column(db.String(20), nullable=False)
    confidence = db.Column(db.Integer, default=None)
    nature = db.Column(db.Integer, default=None)
    outspoken = db.Column(db.Integer, default=None)
    avg = db.Column(db.Float, default=None)

    def __repr__(self):
        return f"Rate('{self.sender_username}', '{self.recevier_username}', '{self.avg}')"


'''
these two databses are not related to each other but have same parent.
so any change in parent must affect both. we must not allow any change in here.
in child DBs.
i have to see how these changing_things feature work and how to control it.
otherwise its easy except the f_key part. but lets see...
'''

