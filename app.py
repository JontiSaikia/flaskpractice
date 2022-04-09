import os
import sys
import uuid
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from flask_restful import Api
#from flask_jwt import JWT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
#from guid import GUID
app = Flask(__name__)
# config of DB
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join("E:\Flask 2nd" , 'test.db')



#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite://' + os.path.join(basedir, 'test.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # work as signal emitting
db = SQLAlchemy(app)

    
# Table('sometable', metadata,
#         Column('id', Integer, primary_key=True),
#         sqlite_autoincrement=True)
class test(db.Model):  # creating a class or schema in dbms
    sno = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    #sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(400), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__format_map(self): # is a special method used to represent a class's objects as a string
        return f"{self.sno}- {self.title} "
        # 
    # def autoincrement(sno,self):
    #         sno = 1
    #         loops = int(input("insert: "))
    #         lis = []
    #         for x in range(loops):
    #             lis.append(input("Input: "))    


    @app.route("/")
    def hello_world():
            Test = test(title = "First form", desc="Start investing") #it maps to database's attributes only to title and desc
            db.session.add(Test)
            db.session.commit()
            return render_template('index.html')
    # return "<p>Hello, World!</p>"


@app.route("/show_me")
def products():
    alltest = test.query.all()
    #alltest= test.query.filter_by(title = "First form").first()
    print(alltest)
    return 'This is a prodcut page'
def __init__(self, **kwargs):
        super(Foo, self).__init__(**kwargs)

if __name__ == "__main__":
    app.run(debug=True)  # run in debug mode so that we can see the error
