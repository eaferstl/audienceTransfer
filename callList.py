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
	if (name != 'Audiencelab Export - Premade Search Seller'):
		arr = np.delete(arr, 0, 0)
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
	a = np.array_split(a, 18)
	return a	
	

def write_audience(spreadsheet, audience):
	spread = Spread(spreadsheet)
	time.sleep(4)
	data = pd.DataFrame(audience)
	spread.df_to_sheet(data, index=False, headers=False, start=(int(tot), 1), replace=False)


def clearSheet(name):
	sh2 = gp.open(name)
	wk2 = sh2.worksheet('main')
	wk2.clear()
	wk2.update('A1:S1', [['Cell Phone 1', 'Cell 1 DNC Flag', 'Cell Phone 2', 'Cell 2 DNC Flag', 'First Name', 'Last Name', 'Email', 'Business Email', 'Birth Year', 'Address Line 1', 'Address Line 2', 'City', 'State', 'Zip Code', 'Household Income', 'Origin of Lead', 'Alternative Emails', 'Job Title']])
	wk2.format('A1:S1', {'textFormat': {'bold': True}})




clearSheet('Baltimore MC Database Leads')
clearSheet('Russ Call List')

main = read_audience('Audiencelab Export - Premade Search Seller')
main = main + read_audience('Audiencelab Export - Premade Search Buyer')
main = main + read_audience('Audiencelab Export - Keyword Search Seller')
main = main + read_audience('Audiencelab Export - Keyword Search Buyer')

balt = format_audience(main, 'Baltimore')
cincy = format_audience(main, 'Cincinnati')

write_audience('Baltimore MC Database Leads', balt)
write_audience('Russ Call List', cincy)
