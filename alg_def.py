# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:02:57 2020

@author: BOUDALIS
"""

import pandas as pd
import io
import requests
from sqlalchemy import create_engine
import psycopg2
from constants import *
import constants
import datetime
import logging
import logging.config

def read_file(url): # this function has as goal to read the file from the url and load it in a dataframe
    try:
        s=requests.get(url).content   # read the url
        df=pd.read_csv(io.StringIO(s.decode('utf-8'))) #load the result in data frame
        return df
    except:
        logging.error(url + " : no file returned with this url")
 
def prepare_data(df,url):  # this function clean and preapre the data to be loaded ti the target
    try:
        df=df[df.application_id.notnull()] #remove null value or application_id
        #made new column has_specific_prefix
        df.loc[df['index_prefix'] == 'shopify_', 'has_specific_prefix'] = 'False' 
        df.loc[df['index_prefix'] != 'shopify_', 'has_specific_prefix'] = 'True'
        #add columns to manage the versionning of the files
        df['date_insert']=pd.to_datetime('now') #add insertion date
        df['file_name']=url # add file name
        return df
    except:
        logging.error(url + " : problem with the expected structure or the file doesn't exist")

def insert_date(df,db_url):
    try:
        #define a connection
        engine = create_engine(db_url)
        conn = engine.raw_connection()
        cur = conn.cursor()
        #preapare the data frame for the insertion in the database
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        #insert the data in the target table
        contents = output.getvalue()
        cur.copy_from(output, 'alg_stg."Shopify_stg"', null="") # null values become ''
        conn.commit()
    except:
        logging.error("problem during the insertion in the database, check the access, the connection string and the target table  ")

def load_all_files(url,db_url,start_date,end_date): #this function load the files between two date 
    try:
        #convert start and end date to format date
        satrt_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        daterange = pd.date_range(satrt_date_obj, end_date_obj) #made a range of date
        for single_date in daterange: #loop the range and load the file of each date
            url_file = url+single_date.strftime("%Y-%m-%d")+".csv"  #define the url
            print(url_file)
            insert_date(prepare_data(read_file(url_file),url_file ),db_url) #insert the data in the database
    except:
        logging.error( "check start_date and end_date parameter" )     

def load_daily_file (url,db_url): #this function load the file of the current date , it can be used for the scheduling . 
    url_cur = url + pd.to_datetime('now').strftime("%Y-%m-%d") +".csv"  #define the url of the file of the current date
    insert_date(prepare_data(read_file(url_cur),url_cur),db_url)    #insert the date in the database
   

