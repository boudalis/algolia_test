# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:07:09 2020

@author: BOUDALIS
"""

from alg_def import *
from constants import *
import constants


print(' first test, check a sample of data')
print(display_query('select * from '+tgt_table + ' limit 10').head())

print(' check that all the files are loaded successfuly') 
print(display_query('select distinct file_name from '+tgt_table))

print(' check the count of all the loaded files')
print(display_query('select count(*) as cnt, export_date,  file_name from '+tgt_table + ' group by export_date,  file_name  order by export_date,  file_name '))

print(' check that there is no dupplicated file')
print(display_query('select export_date, date_insert, count(*) as cnt from '+tgt_table + ' group by export_date, date_insert order by export_date , date_insert '))

print(' check that all the application_id are not null ')
print(display_query('select *  from '+tgt_table + ' where application_id is null'))

print(' check the rule of  the column "has_specific_prefix" ')
print(display_query('select has_specific_prefix,index_prefix, count(*) as cnt  from '+tgt_table + ' group by  has_specific_prefix,index_prefix order by  has_specific_prefix,index_prefix'))

print(' check rows based on id filter')
print(display_query('select * from '+tgt_table + ' where id = \'134d5c2e-9a04-4f8d-9a15-efdcfe34b167\''))

print(' check rows based on application_id filter')
print(display_query('select * from '+tgt_table + ' where application_id = \'B9899PT0J3\''))

print('check all the install_channel')
print(display_query('select install_channel , count(*) as cnt from '+tgt_table +  'group by install_channel'))

