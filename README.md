# Mini Project3
## SQL
SQL database is used for structured data, where every data recond inside a table has the same attributes. Data records from different tables can have relationship with each other, thus sql is relational database.

## NOSQL
NoSQL database is good for storing non-structure data, where each record can have any number attributes, and records don't need to relate to each other. Searching inside NoSQL is faster than in SQL.

## User Story
Mark runs a online alchol delivery site called "Alcohaul", he needs to use a database to store inventory. He needs records for wines to always get sorted by Categories, origin and price. But Mark also needs a database that can process insertion or deletion of sales records very fast in real-time, because the sites has attracted lots of customers. Also, when a sale happends, not all informations about the product has to be inputed, because if all information is entered into the database, Mark will evetually run out of local storage space (He's too poor to pay for AWS EBS). 
He can run two type databases, with SQL storing informations about the product his store has, and NoSQL for sales and inventory. 


### Script
*Note: for Alcohaul_mongo.py, it's assumed that you have mongo server setup on your local machine*

* Alcohaul_sql.py 
  * records are loaded into local sql datebase from the json file
  * provides search function to search with a key/value combination
  * privides a insertion function to add new products

* Alcohaul_mongo.py
  * provides search function to search with a Python dictionary as input, with keys/values in the dictionary
  * provides a function to insert a single record. 