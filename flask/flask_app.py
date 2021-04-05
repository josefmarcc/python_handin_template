#!flask/bin/python
from flask import Flask, jsonify, abort, request
import pandas as pd
import random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey



app = Flask(__name__)


import mysql.connector as mysql
cnx = mysql.connect(host = "db", user = "root", passwd = "root", db = "db")


# Laver DB con og tables
con_str = "mysql+mysqlconnector://root:root@db/db"
engine = create_engine(con_str)
metadata = MetaData()
users = Table('user_info', metadata,
Column('id', Integer, primary_key=True),
Column('fname', String(45)),
Column('lname', String(45)),
Column('year', Integer),)
metadata.create_all(engine)

# Laver Dataframe og sætter ind  i SQL
df = pd.DataFrame({'fname': ['Josef', 'Thor', 'Frederik'],
                   'lname': ['Marc', 'Christensen', 'Dahl'],
                   'year': [1995, 1996, 1997]})
df.to_csv('/home/jovyan/flask/csv_output/csv_output.csv', index=False) 

df = df.applymap(str)
df.to_sql('user_info',con=engine, if_exists='append', index = False)

conn = engine.connect()


@app.route('/api/persons/all', methods=['GET'])
def get_task():
    cursor = cnx.cursor()
    query = "SELECT * FROM user_info"
    cursor.execute(query)
    laptops = cursor.fetchall()
    res = []

    for idx, val in enumerate(laptops):
        res.append({"id": val[0], "fname": val[1], "lname": val[2], "year": val[3]})

    return jsonify(res)


@app.route('/')
def hello_world():
    return 'Persons project'

@app.route('/api/person', methods=['POST'])
def create_person():
    if not request.json or not 'fname' in request.json:
        abort(400)
    fname = request.json['fname']
    lname = request.json['lname']
    year = request.json['year']
    person = {
        'fname': request.json['fname'],
        'lname': request.json['lname'],
        'year': request.json['year'],
    }
    cursor = cnx.cursor()
    query = """INSERT INTO user_info (fname, lname, year) VALUES (%s, %s, %s)"""
    val = (fname, lname, year)
    cursor.execute(query, val) 
    cnx.commit()
    cursor.close()
    return jsonify(person), 201




if __name__ == '__main__':
    app.run(debug=True)
