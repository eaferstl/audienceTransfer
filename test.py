import gspread as gs
import numpy as np
import pandas as pd
from gspread_pandas import Spread, Client
import time
import math
import schedule
from pytz import timezone


def transfer():
	print('Flag2')
	with open("2audience.py") as f:
    		exec(f.read())


print('Flag0')
schedule.every().monday.at("15:20", timezone("America/New_York")).do(transfer)
print('Flag1')

while True:
	schedule.run_pending()
	time.sleep(90)
