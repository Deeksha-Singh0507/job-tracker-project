# main.py

import requests
import pandas as pd
import os

# Step 1: RemoteOK API endpoint
url = "https://remoteok.com/api"

# Step 2: Send request with headers
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Step 3: If request is successful
if response.status_code == 200:
    data = response.json()

    # Step 4: Skip the first item (it's metadata)
    jobs = data[1:]

    # Step 5: Extract all job details (NO FILTERING)
    job_list = []
    for job in jobs:
        job_list.append({
            "date": job.get("date", ""),
            "company": job.get("company", ""),
            "position": job.get("position", ""),
            "location": job.get("location", ""),
            "tags": ", ".join(job.get("tags", [])),
            "url": "https://remoteok.com" + job.get("url", "")
        })

    # Step 6: Convert to DataFrame
    df = pd.DataFrame(job_list)

    # Step 7: Create output folder if not exists
    os.makedirs("output", exist_ok=True)

    # Step 8: Save to CSV
    df.to_csv("output/remoteok_jobs.csv", index=False)
    print(f"✅ Saved {len(df)} jobs to output/remoteok_jobs.csv")

else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
