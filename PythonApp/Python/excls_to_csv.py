#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-28 09:05:43
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io

import xlrd
import csv
import codecs
import argparse
import os
import time
 
def args_parse():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", 
                    required=True,
                    help="excel file name")
    args = vars(ap.parse_args()) 
    return args
 
def xlsx_to_csv_pd(filepath):
    (filedir, filename) = os.path.split(filepath)
    (fn, ext) = os.path.splitext(filename)
    workbook = xlrd.open_workbook(filepath)
    sheets = workbook.sheet_names()
    for i in range(len(sheets)):
        table = workbook.sheet_by_index(i)
        sht = fn + '_' + sheets[i] + '.csv'
        with codecs.open(sht, 'w', encoding='UTF-8') as f:
            write = csv.writer(f)
            for row_num in range(table.nrows):
                row_value = table.row_values(row_num)
                write.writerow(row_value)
        print(sht," created!")
        
if __name__=='__main__':
    st = time.time()
    args = args_parse()
    filepath = args['file']
    xlsx_to_csv_pd(filepath)
    print("Completed to convert ",filepath," to csv files!")
    nd = time.time()
    tm = nd - st
    print("Spend time: ",tm,"s")