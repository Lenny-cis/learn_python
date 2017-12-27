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

list_with_dupes=[1,5,6,8,3,8,3,3,7,9]
set_without_dupes=set(list_with_dupes)
print(set_without_dupes)

first_set=set([1,5,6,2,6,3,6,7,3,9,10,321,54,654,432])
second_set=set([4,6,7,432,6,7,4,9,0])
print(first_set.intersection(second_set))
print(first_set.union(second_set))
print(first_set.difference(second_set))
print(second_set-first_set)
print(6 in second_set)
print(6 in first_set)

import numpy as np
list_with_dupes=[1,5,6,2,5,6,8,3,8,3,3,7,9]
print(np.unique(list_with_dupes,return_index=True))
array_with_dupes=np.array([[1,5,7,3,9,11,23],[2,4,6,8,2,8,4]])
print(np.unique(array_with_dupes))

set_of_lines=set([list(x)[2][1] for x in zipped_data])
uniques=[x for x in zipped_data if not set_of_lines.remove(list(x)[2][1])]
print(set_of_lines)

import re
word='\w+'
sentence='Here is my sentence.'
re.findall(word,sentence)
search_result=re.search(word,sentence)
search_result.group()
match_result=re.match(word,sentence)
match_result.group()

number='\d+'
capitalized_word='[A-Z]\w+'
sentence='I have 2 pets: Bear and Bunny.'
search_number=re.search(number,sentence)
search_number.group()
match_number=re.match(number,sentence)
match_number.group()
search_capital=re.search(capitalized_word,sentence)
search_capital.group()
match_capital=re.match(capitalized_word,sentence)
match_capital.group()

name_regex='([A-Z]\w+) ([A-Z]\w+)'
names="Barack Obama, Ronald Reagan, Nancy Drew"
name_match=re.match(name_regex,names)
name_match.group()
name_match.groups()
name_regex='(?P<first_name>[A-Z]\w+) (?P<last_name>[A-Z]\w+)'
for name in re.finditer(name_regex,names):
    print('Meet {}!'.format(name.group('first_name')))

def get_rows(file_name):
    rdr=reader(open(file_name,'r'))
    return [row for row in rdr]
def eliminate_mismatches(header_rows,data_rows):
    all_short_headers=[h[0] for h in header_rows]
    skip_index=[]
    final_header_rows=[]
    for header in data_rows[0]:
        if header not in all_short_headers:
            index=data_rows[0].index(header)
            if index not in skip_index:
                skip_index.append(index)
            else:
                for head in header_rows:
                    if head[0]==header:
                        final_header_rows.append(head)
                        break
    return skip_index,final_header_rows
def zip_data(headers,data):
    zipped_data=[]
    for drow in data:
        zipped_data.append(zip(headers,drow))
    return zipped_data
def create_zipped_data(final_header_rows,data_rows,skip_index):
    new_data=[]
    for row in data_rows[1:]:
        new_row=[]
        for index,data in enumerate(row):
            if index not in skip_index:
                new_row.append(data)
        new_data.append(new_row)
    zipped_data=zip_data(final_header_rows,new_data)
    return zipped_data
def main():
    data_rows=get_rows('data/unicef/mn.csv')
    header_rows=get_rows('data/unicef/mn_headers.csv')
    skip_index,final_header_rows=eliminate_mismatches(header_rows,
                                                      data_rows)
    zipped_data=create_zipped_data(final_header_rows,data_rows,skip_index)
if __name__=='__main__':
    main()
    

