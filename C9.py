# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:28:50 2017

@author: Lenny
"""

import xlrd
import agate
workbook=xlrd.open_workbook('data\\unicef\\unicef_oct_2014.xls')
workbook.nsheets
workbook.sheet_names()
sheet=workbook.sheets()[0]
sheet.nrows
sheet.row_values(0)
for r in range(sheet.nrows):
    print(r,sheet.row(r))
title_rows=zip(sheet.row_values(4),sheet.row_values(5))
titles=[t[0]+' '+t[1] for t in title_rows]
titles=[t.strip() for t in titles]
titles
country_rows=[sheet.row_values(r) for r in range(6,114)]

from xlrd.sheet import ctype_text
text_type=agate.Text()
number_type=agate.Number()
boolean_type=agate.Boolean()
date_type=agate.Date()
example_row=sheet.row(6)
print(example_row)
print(example_row[0].ctype)
print(example_row[0].value)
print(ctype_text)
types=[]
for v in example_row:
    value_type=ctype_text[v.ctype]
    if value_type=='text':
        types.append(text_type)
    elif value_type=='number':
        types.append(text_type)
    elif value_type=='xldate':
        types.append(text_type)
    else:
        types.append(text_type)
table=agate.Table(country_rows,titles,types)
table.print_table(max_columns=7)
def remove_bad_chars(val):
    if val=='-':
        return None
    return val
cleaned_rows=[]
for row in country_rows:
    cleaned_row=[remove_bad_chars(rv) for rv in row]
    cleaned_rows.append(cleaned_row)
    
def get_new_array(old_array,function_to_clean):
    new_arr=[]
    for row in old_array:
        cleaned_row=[function_to_clean(rv) for rv in row]
        new_arr.append(cleaned_row)
    return new_arr
cleaned_rows=get_new_array(country_rows,remove_bad_chars)