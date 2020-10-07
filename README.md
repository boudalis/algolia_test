# algolia_test
## Algolia project 

this project has for goal to integrate the files downloaded by the provided URL into the Postgres database, this project was developed by python.

## Prerequisites 

1- python should be installed in the environment

2- the files should be copied in the same folder

3- prepare the target database, it should be Postgres database

4- make sure that you have all the access and the privileges to this database

5- pip install the necessary python lib in your environment (pandas , io ,requests, sqlalchemy, datetime, logging, psycopg2)

6- make sure that you have access to the URL

## run the project 

1- copy the project in one folder,

2-create a Postgres database, or use the existing one (

connection: algdb-1.c3kwj6orkqge.eu-west-3.rds.amazonaws.com

user : postgres

pwd : postgres

port : 5432 )

3-run the query.sql file (you can change the table name and schema and tablespaces if you want, but make sure that you have updated the constants.py file

4-prepare constants.py file, you can change the target database connection string, the name of the target table, the range of date, and the URL of the source file.

5- the file alg_main_his.py should be used to load all the files between the start and end date cmd to use is "python alg_main_his.py"

6-the file alg_main_daily.py can be used to load the file of the current day, if we want to schedule the project we should run this file, cmd to use is "python alg_main_daily.py"

7-the file alg_def.py contains all the python functions

## additional information

1- the target database was created in RDS AWS services, it's open to the public you can access using the below information :

connection: algdb-1.c3kwj6orkqge.eu-west-3.rds.amazonaws.com

user : postgres

pwd : postgres

port : 5432

2- the file unit_tests.py was created to display some tests that make us sure that we have loaded the data in the right way and that we have a good result

3- a function was created to display the result of the tests, you can run them all at the same time or you can run them one by one

4- you can add more test if you want, you can use the function display_query( query ), you just the put the right query as an input
