import gspread as gs
import numpy as np
import pandas as pd
from gspread_pandas import Spread, Client
import time
import math
import schedule
from pytz import timezone


def transfer():
	print('In Function')
	with open("audience.py") as f:
    		exec(f.read())


print('Flag0')
schedule.every().day.at("09:30", timezone("America/New_York")).do(transfer)
print('Flag3')

while True:
	schedule.run_pending()
	time.sleep(60)
