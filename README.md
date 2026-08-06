# Vidéos pour la maturité professionnelle

Collects and publishes YouTube math videos organized by topic, for the "maturité professionnelle".

Visit the following link to see the list of videos :

[http://www.cyrraz.com/videos-maths-matu-pro](http://www.cyrraz.com/videos-maths-matu-pro)

## Files

- **index.md** — Page listing the videos by topic (generated from `youtube_results.csv`), published as the repo's page.
- **keywords.txt** — List of topics/keywords used to search for videos.
- **search.py** — Queries the YouTube API for each keyword across given channels and saves results to `youtube_results.csv` (resumes where it left off via `progress.txt`).
- **youtube_results.csv** — Raw search results (keyword, channel, title, date, URL).
- **from_csv_to_md.py** — Converts `youtube_results.csv` into `index.md`, grouped by keyword.
- **LICENSE** — Repository license.
