import gspread

creds = {"web":{"client_id":"853011972181-5c18vhui0t8b2jbjt35pidkl406a5aob.apps.googleusercontent.com","project_id":"audience-lab","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["https://localhost/","http://localhost/"]}}

gsheet_client, refr = gspread.oauth_from_dict(creds)
print(refr)
