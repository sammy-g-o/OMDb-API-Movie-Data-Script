import requests
import  json

response = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=5105bd23&s=justice+league')
data = response.json()
list_ofData = data['Search']

with open('search-results.txt', 'w') as file:
    for movie in list_ofData:
        print(movie['Title'])
        file.write("movie name: " + movie['Title'] + '\n' + "date released: " + movie['Year'] +'\n')