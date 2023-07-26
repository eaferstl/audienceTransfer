import gspread


gsheet_client, refr = gspread.oauth_from_dict(creds)
print(refr)
