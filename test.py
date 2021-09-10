#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:31:01 2021

@author: leonardo
"""

import subprocess
import pathlib
import xlrd


path = str(pathlib.Path(__file__).parent.resolve())
path_main = path.replace('test','')
print(path)
file_path = path+'/automation_groups.xlsx'
#xlsx = subprocess.Popen([file_path])

book = xlrd.open_workbook(file_path)