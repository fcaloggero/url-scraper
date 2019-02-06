# -*- coding: utf-8 -*-

#Load packages
from lxml import html
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
from pandas import read_csv
import os
import json


#import url
variable_name = "URL"                   #retrieve the web page of interest
page = urllib2.urlopen(variable_name)
soup = BeautifulSoup(page)              #pull all code from the page

soup.title                              #check title of page, ensure it works
soup.title.string

#find 'p' where content is
soup.p
variable_name = soup.find_all('p')      #find all instances of 'p' in the code, this is where we pull text from
variable_name=pd.DataFrame(list(variable_name)) #push all 'p' test into a dataframe for analysis

#set txt for analysis
variable.to_csv ('~/Desktop/Work/example.txt')
