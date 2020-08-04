import pymysql

def save_events():
  result=[]
  conn=pymysql.connect('flaskappdb.cp0cwgczn9ur.us-east-1.rds.amazonaws.com',user='admin',passwd='Superman',db='flaskdb')
  conn.execute


save_events()
