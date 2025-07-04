import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 1. Define scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# 2. Load credentials from JSON
creds = ServiceAccountCredentials.from_json_keyfile_name("job-sheet-service-key.json", scope)

# 3. Authorize client
client = gspread.authorize(creds)

# 4. Open Google Sheet
SHEET_NAME = "Job Listings sheet"
sheet = client.open(SHEET_NAME).sheet1

# 5. Read CSV
df = pd.read_csv("output/remoteok_jobs.csv")
df = df.fillna("")  # NaN hata do

# 6. Prepare rows
rows = [df.columns.tolist()] + df.values.tolist()

# 7. Clear and batch update
sheet.clear()
sheet.update(rows)

print("✅ Google Sheet me data upload ho gaya (bulk upload)! ✅")
