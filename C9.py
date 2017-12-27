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
print(titles)