# OMDb-API-Movie-Data-Script
This Python script fetches movie data from the OMDb (Open Movie Database) API. It searches for "Justice League" and saves the titles and release years of the matching movies to a text file.
## Prerequisites
Python installed on your system.
The requests library:
pip install requests


## How to Use
Make sure the requests library is installed.
Run the script from your terminal:
python omdb.py


The script will print the title of each movie found to the console and save a list of movie titles and release years to a file named search-results.txt.
Note: The script uses a hard-coded API key. For production applications, you should handle API keys more securely (e.g., using environment variables).
