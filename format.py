import gspread as gs
import numpy as np
import pandas as pd
from gspread_pandas import Spread, Client
import time
import math
import hashlib



#authenticate and connect to gspread
gp = gs.oauth()



def read_audience(name):
	global gp
	sh1 = gp.open(name)
	wk1 = sh1.worksheet('Sheet1')
	arr = np.array(wk1.get_all_values())
	return arr


def format_audience(array):
	df = pd.DataFrame(array)
	first = df.pop(df.columns[3])
	df.insert(0, 'SHA256_EMAIL', first)
	second = df.pop(df.columns[4])
	df.insert(1, 'CELL_PHONE_1', second)
	five = df.pop(df.columns[13])
	df.insert(4, 'ZIP_CODE', five)
	df.insert(4, 'COUNTRY', 'US')
	df.drop(df.columns[[6,7,8,9,10,11,12,13,14,15,16,17,18,19]], axis=1, inplace=True)
	a = df.to_numpy()
	a = np.delete(a, 0, 0)
	for i in a:
		for j in range(4):
			if (j==1 or j==2 or j==3):
				if (i[j] != 0):
					i[j] = \
						hashlib.sha256(i[j].encode()).hexdigest()
	a = np.array_split(a, 18)
	return a	
	

def write_audience(audience, tot):
	spread = Spread('NewFluency')
	for i in range(18):
		time.sleep(4)
		data = pd.DataFrame(audience[i])
		spread.df_to_sheet(data, index=False, headers=False, start=(int(tot), 1), replace=False)
		tot = tot + math.ceil(audience[i].size / 6) 
#		tot = tot + math.ceil(np.argmax(audience[i]) / 1.9)
	return tot



#clear fluency spreadsheet to prepare for new data
sh2 = gp.open('NewFluency')
wk2 = sh2.worksheet('Sheet1')
wk2.clear()
wk2.update('A1:F1', [['Email', 'Phone', 'First Name', 'Last Name', 'Country', 'Zip']])
wk2.format('A1:F1', {'textFormat': {'bold': True}})


#Premade Seller
ps = read_audience('NewFormat')
f1 = format_audience(ps)
row = write_audience(f1, 2)


#Premade Buyer
#pb = read_audience('Audiencelab Export - Premade Search Buyer')
#row = write_audience(pb, row)

#Keyword Seller
#ks = read_audience('Audiencelab Export - Keyword Search Seller')
#row = write_audience(ks, row)

#Keyword Buyer
#kb = read_audience('Audiencelab Export - Keyword Search Buyer')
#row = write_audience(kb, row)
