import requests

def search_movie(title):
    API_KEY = "94ce66cc"
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data['Response'] == "True":
        print(f"🎬 Title: {data['Title']}")
        print(f"📅 Year: {data['Year']}")
        print(f"⭐ IMDb Rating: {data['imdbRating']}")
        print(f"🎭 Genre: {data['Genre']}")
        print(f"🖼️ Poster URL: {data['Poster']}")
    else:
        print("❌ Movie not found.")

# Run it
movie_title = input("Enter movie title: ")
search_movie(movie_title)
