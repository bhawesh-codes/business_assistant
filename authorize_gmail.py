from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.compose"
]

flow = InstalledAppFlow.from_client_secrets_file(
    "tokens.json",
    SCOPES
)

creds = flow.run_local_server(port=0)

with open("tokens.json", "w") as token:
    token.write(creds.to_json())

print("Gmail authorization complete.")