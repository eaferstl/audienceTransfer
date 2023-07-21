import gspread as gs
import numpy as np
import pandas as pd
from gspread_pandas import Spread, Client
import time
import math



#authenticate and connect to gspread
gp = gs.oauth()



def read_audience(name):
	global gp
	sh1 = gp.open(name)
	wk1 = sh1.worksheet('export')
	arr = np.array(wk1.get_all_values())
	for i in range(3):
		arr = np.delete(arr, 0, 1)
	arr = np.delete(arr, 3, 1)
	arr = np.delete(arr, 0, 0)
	a = np.array_split(arr, 18)
	return a
	

def write_audience(audience, tot):
	spread = Spread('New spreadsheet')
	for i in range(18):
		time.sleep(4)
		data = pd.DataFrame(audience[i])
		spread.df_to_sheet(data, index=False, headers=False, start=(int(tot), 1), replace=False)
		tot = tot + math.ceil(np.argmax(audience[i]) / 2.1)
	return tot



#clear fluency spreadsheet to prepare for new data
sh2 = gp.open('New spreadsheet')
wk2 = sh2.worksheet('Sheet1')
wk2.clear()
wk2.update('A1:C1', [['SHA256_Email', 'City', 'State']])
wk2.format('A1:C1', {'textFormat': {'bold': True}})

print('Flag 1')

#Premade Seller
ps = read_audience('Audiencelab Export - Premade Search Seller')
row = write_audience(ps, 2)

print('Flag 2')

#Premade Buyer
pb = read_audience('Audiencelab Export - Premade Search Buyer')
row = write_audience(pb, row)

#Keyword Seller
ks = read_audience('Audiencelab Export - Keyword Search Seller')
row = write_audience(ks, row)

#Keyword Buyer
kb = read_audience('Audiencelab Export - Keyword Search Buyer')
row = write_audience(kb, row)


#for i in range(row):
#	if len(wk2.cell(i+1, 1).value) == 0:
#		time.sleep(1)
#		wk2.delete_row(i)
#		i = i - 1

