import os
import csv
import requests

API_KEY = os.environ["YOUTUBE_API_KEY"]

CHANNELS = [
    "UCaDqmzanCq4ZYhdEm0Df9Qg",  # YMONKA
    "UC8SRYHgGMqAYZehYdznaqvQ",  # Hedacademy
]

# ------------------------
# Read keywords
# ------------------------

with open("keywords.txt") as f:
    keywords = [line.strip() for line in f if line.strip()]

# ------------------------
# Resume from previous run
# ------------------------

start = 0

if os.path.exists("progress.txt"):
    with open("progress.txt") as f:
        last_keyword = f.read().strip()

    if last_keyword in keywords:
        start = keywords.index(last_keyword) + 1

# ------------------------
# Open output file
# ------------------------

file_exists = os.path.exists("youtube_results.csv")

csvfile = open(
    "youtube_results.csv",
    "a",
    newline="",
    encoding="utf-8"
)

writer = csv.writer(csvfile)

if not file_exists:
    writer.writerow([
        "keyword",
        "channel",
        "title",
        "date",
        "url"
    ])

# ------------------------
# Main loop
# ------------------------

quota_exhausted = False

for keyword in keywords[start:]:

    print(f"\nSearching '{keyword}'")

    for channel in CHANNELS:

        response = requests.get(
            "https://www.googleapis.com/youtube/v3/search",
            params={
                "key": API_KEY,
                "part": "snippet",
                "channelId": channel,
                "q": keyword,
                "type": "video",
                "maxResults": 10,
            },
        )

        data = response.json()

        if "error" in data:
            print("\nAPI error:")
            print(data["error"]["message"])
            quota_exhausted = True
            break

        for video in data["items"]:

            snippet = video["snippet"]

            writer.writerow([
                keyword,
                snippet["channelTitle"],
                snippet["title"],
                snippet["publishedAt"][:10],
                f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            ])

            csvfile.flush()

    if quota_exhausted:
        break

    # Save progress after finishing both channels
    with open("progress.txt", "w") as f:
        f.write(keyword)

csvfile.close()

if quota_exhausted:
    print("\nStopped because the daily quota was exhausted.")
    print("Run the script again tomorrow.")
else:
    print("\nFinished!")
