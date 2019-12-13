import mysql.connector
import sqlite3
import unicodedata
import json

wines=[]
limit=0
with open("wines.json", "r") as read_file:
    wines = json.load(read_file)
    limit=limit+1

wines = wines[:30]


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mark1234"

)

c = mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS Alcohol_db ")
#c = mydb.connect('Alcohol_db').cursor()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mark1234",
  db="Alcohol_db"	 
)

c = mydb.cursor()
c.execute("CREATE TABLE IF NOT EXISTS WineList(id VARCHAR(255) ) ")


def laod_json_into_db(jsonfile):
	
	with open(jsonfile, "r") as read_file:
		wines = json.load(read_file)

	wines = wines[:100]
	for w in wines:
		info=[]
		for key in w:
			
			if key!="price" and key!="description":
				if w[key]==None:
					info.append("N/A")
				else:

					filtered =  w[key].replace("\\","")
					info.append(filtered)

		vals = str(tuple(info))

		vals=vals.replace("u","")

		c.execute("INSERT INTO WineList VALUES %s"%vals)


laod_json_into_db("wines.json") 


def search_for_wine( keys, values):
	if len(keys)<1:
		print "please add search key"
		return

	clause=""

	for i in range(len(keys)):
		k = keys[i]
		if k not in wines[0]:
			print("please enter a valid keyword")
			return
		if len(clause)>0:
			s="'%s'='%s'"%(k,v)
			clause=clause+"AND "+s
		else:
			v = values[i]
			s="'%s'='%s'"%(k,v)
			clause=clause+s
	print clause
	ks = str(tuple(keys))
	vs = str(tuple(values))
#	q = "SELECT * FROM WineList WHERE %s"%clause
	q = "SELECT * FROM WineList"
	print q
	c.execute(q)
	results = c.fetchall()
	print results
#print wines[0]
search_for_wine( ["province"], ["u'California'"])








