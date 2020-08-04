import os
from flask import Flask,session,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
app=Flask(__name__)


conn=pymysql.connect('flaskappdb.cp0cwgczn9ur.us-east-1.rds.amazonaws.com',user='admin',passwd='Superman',db='flaskdb')
# app.secret_key='12394'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://admin:Superman@flaskappdb.cp0cwgczn9ur.us-east-1.rds.amazonaws.com/flaskdb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db=SQLAlchemy(app)

# class users(db.Model):
# 	_id=db.Column('id',db.Integer,primary_key=True)
# 	name=db.Column('name',db.String(100))
# 	email=db.Column('email',db.String(100))

# 	def __init__(self,name,email):
# 		self.name=name
# 		self.email=email
    

@app.route("/")
def home():
    result = []
    with conn.cursor() as cur:
            # cur.execute("""create table test(id int,name text)""")
            cur.execute("""insert into test (id, name) values( %s, '%s')""" % (1, 'ketan'))
            cur.execute("""select * from test""")
            conn.commit()
            cur.close()    
            for row in cur:
                    result.append(list(row))
    
    return result[0][1]
    
if __name__=='__main__':
    app.run(host=os.getenv('IP','127.0.0.1'),port=int(os.getenv('PORT',8080)))        
