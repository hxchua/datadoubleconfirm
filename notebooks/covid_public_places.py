# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:02:25 2020

@author: hxchu
"""

from __future__ import print_function
import numpy as np
import pandas as pd
import gspread_dataframe as gd
import gspread
from google.oauth2.service_account import Credentials
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1KIyCmEaum6YBzlri4vc-aG1EnLhowqv2MelaqtPudVg' ##change this
#SAMPLE_RANGE_NAME = 'Sheet1!A:E' ##change this



credentials = Credentials.from_service_account_file('project-gsheets-c30a9f47e838.json', scopes=SCOPES)
gc = gspread.authorize(credentials)

# Connecting with `gspread` here

ws = gc.open_by_key(SAMPLE_SPREADSHEET_ID).worksheet("Sheet1")
existing = gd.get_as_dataframe(ws)

#scraping the site
site = "https://www.gov.sg/article/covid-19-public-places-visited-by-cases-in-the-community-during-infectious-period"
hdr = {'User-Agent': 'Mozilla/5.0'}
bookpage = requests.get(site)
soup = BeautifulSoup(bookpage.text, "lxml")
#table = soup.find_all('table')[0]
table = soup.find(lambda tag: tag.name=='table') 
rows = table.findAll(lambda tag: tag.name=='tr')

data=[]
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

#cleaning the scraped data
df = pd.DataFrame(np.array(data))
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
df[['Location','Sub-location']] = df['Location (Address)'].str.split('\n\n',expand=True)
#df['Sub-location'] = df['Sub-location'].str.replace('• ','')
df['Sub-location'] = df['Sub-location'].str.replace('\n',', ')
df['Sub-location'] = df['Sub-location'].str.strip()
df['Notes']=""
df['Notes'][df['Date'].str.contains("\*")] = "Added/Updated on " + datetime.today().strftime('%Y-%m-%d')
df['Date'] = df['Date'].str.replace('*','')
df['Source'] = site
df['Time'] = df['Time'].str.replace('to','-')
df = df[['Date','Time','Location','Sub-location','Source','Notes']]
df['Date'] = (df['Date']+' 2020').astype(str)
df['Date'] = df['Date'].str.replace(' ','-')
df['Date'] = pd.to_datetime(df['Date'],format='%d-%b-%Y')

#appending with latest data
#existing['Date'] = (existing['Date']+' 2020').astype(str)
#existing['Date'] = existing['Date'].str.replace(' ','-')
existing['Date'] = pd.to_datetime(existing['Date'],format='%Y-%m-%d')
#existing = existing[existing['Date']<df['Date'].min()]
updated = existing.append(df)
updated = updated[['Date','Time','Location','Sub-location','Source','Notes']]
updated = updated.drop_duplicates(['Date','Time','Location'])
updated = updated.sort_values(by=['Date'], ascending=False)
updated['Date'] = updated['Date'].astype(str)
updated.fillna('', inplace=True)
updated = updated[:-1]
ws.update([updated.columns.values.tolist()] + updated.values.tolist())


#updated.to_csv('covid_public_sg.csv',index=False)

###References:
#https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
#https://stackoverflow.com/questions/31328861/python-pandas-replacing-header-with-top-row
#https://www.graspingdata.tech/solved-the-caller-does-not-have-permission-using-the-api-with-a-private-google-spreadsheet/
#https://gspread.readthedocs.io/en/latest/