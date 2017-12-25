# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:01:13 2017

@author: Lenny
"""

import csv
csvfile=open('data-text.csv','r')
reader=csv.reader(csvfile)
for row in reader:
    print(row)

import json
json_data=open('data-text.json').read()
data=json.loads(json_data)
for item in data:
    print(item)

from xml.etree import ElementTree as ET
tree=ET.parse('data-text.xml')
root=tree.getroot()
data=root.find('Data')
all_data=[]
for observation in data:
    record={}
    for item in observation:
        lookup_key=list(item.attrib.keys())[0]
        if lookup_key=='Numeric':
            rec_key='NUMERIC'
            rec_value=item.attrib['Numeric']
        else:
            rec_key=item.attrib[lookup_key]
            rec_value=item.attrib['Code']
        record[rec_key]=rec_value
    all_data.append(record)
print(all_data)

import xlrd
book=xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet=book.sheet_by_name('Table 9 ')
data={}
for i in range(14,sheet.nrows):
    row=sheet.row_values(i)
    country=row[1]
    data[country]={
        'child_labor':{
        'total':[row[4],row[5]],
        'male':[row[6],row[7]],
        'female':[row[8],row[9]]
        },
        'child_marriage':{
        'marriage_by_15':[row[10],row[11]],        
        'marriage_by_18':[row[12],row[13]]
        }
    }
    if country=='Zimbabwe':
        break
import pprint
pprint.pprint(data)

from csv import DictReader
data_rdr=DictReader(open('data/unicef/mn.csv','r'))
header_rdr=DictReader(open('data/unicef/mn_headers.csv','r',encoding='utf-8'))
data_rows=[d for d in data_rdr]
header_rows=[h for h in header_rdr]
new_rows=[]
for data_dict in data_rows:
    new_row={}
    for dkey,dval in data_dict.items():
        for header_dict in header_rows:
            if dkey in header_dict.values():
                new_row[header_dict.get('Label')]=dval
    new_rows.append(new_row)

from csv import reader
data_rdr=reader(open('data/unicef/mn.csv','r'))
header_rdr=reader(open('data/unicef/mn_headers.csv','r',encoding='utf-8'))
data_rows=[d for d in data_rdr]
header_rows=[h for h in header_rdr if h[0] in data_rows[0]]
print(len(header_rows))
all_short_headers=[h[0] for h in header_rows]
skip_index=[]
final_header_rows=[]
for header in data_rows[0]:
    if header not in all_short_headers:
        index=data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0]==header:
                final_header_rows.append(head)
                break
new_data=[]
for row in data_rows[1:]:
    new_row=[]
    for i,d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)
zipped_data=[]
for drow in new_data:
    zipped_data.append(zip(final_header_rows,drow))
for x in enumerate(list(zipped_data[0])[:20]):
    print(x)