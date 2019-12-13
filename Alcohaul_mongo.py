
import pymongo


client = pymongo.MongoClient()


# connect to local mongo db:

client = pymongo.MongoClient('mongodb://localhost:3000/',
	username='root',
	password='Mark1234',
	#authsource='admin',
	authMechanism='SCRAM-SHA-1'
	)

db = client["sales-records"]
sale = {'name': 'red', 'price': '100'}
transactions = db["transaction"]


def insert_sale(dic):
	result = transactions.insert_one(dic)


# search for sale records with key and value

def search_sale(key, value):

	records=[]
	for e in transactions.find():
		records.append(e)
	return records


insert_sale(sale)
print search_sale("red", "Rose")
