# algolia_test
test pour algolia

this project has for goam to integrate the file downloaded by the provided url into postgres database, this project was developed by python so to run please make sure that python is installed in your invironement.

Prerequest :

1- python should be installed in the enviroenemnt 

2- the files should be copied in the same folder 

3- prepare the target database, it should be postgres database

4- make sure that you have all the access and the privileges to this database 

5- pip install the necessary python lib in your environement (pandas , io ,requests, sqlalchemy, datetime, logging, psycopg2)

6- make sure that you have access to the URL 



run the project :

1- copy the project in one folder,

2-create a postgers database, or use the existing one (

connection : algdb-1.c3kwj6orkqge.eu-west-3.rds.amazonaws.com

user : postgres

pwd : postgres

port : 5432 )

3-run the query.sql file (you can change the table name and schema and tablespaces if you want , but make sure that you have updated the constants.py file

4-prepare constants.py file, you can change the target database connection string, the name of the target table , the range of date and the url of the source file.

5- the file alg_main_his.py should be used to load all the files between the start and end date

6-the file alg_main_daily.py can be used to load the file of the current day, if we want to schedule the project we should run this file.

7-the file alg_def.py containt all the python functions




