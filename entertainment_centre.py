# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:46:06 2016
A project to create a single webpage which lists movie information
@author: David
"""

# import the movie class and webpage generator
import media
import fresh_tomatoes
import httplib
import json

# api key for tmdb - if this is not provided, then it won't work...
API_KEY = None

# a switch to determine whether to use the film API
use_api = True

# override use_api if API_KEY is None
if API_KEY is None:
    use_api = False
    
# function to create a movie object using TMDB - if use_api=True
def create_movie_from_tmdb(movie_id):
    # do get_details against tmdb
    conn = httplib.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    rq_string = "/3/movie/"+movie_id+"?language=en-US&api_key=" + API_KEY
    conn.request("GET", rq_string, payload)
    res = conn.getresponse()
    data = json.loads(res.read())
    
    # parse response and extract overview and title and poster path
    movie_title = data["original_title"]    
    movie_storyline = data["tagline"]
    movie_image = "https://image.tmdb.org/t/p/w500"+data["poster_path"]
    # use get_videos to get youtube url
    rq_string = "/3/movie/"+movie_id+"/videos?language=en-US&api_key=" + API_KEY
    conn.request("GET", rq_string, payload)
    res = conn.getresponse()
    data = json.loads(res.read())
    
    movie_video = "https://www.youtube.com/watch?v="+data["results"][0]["key"]
   # create a movie object
    movie = media.Movie(movie_title,movie_storyline,movie_image,
                        movie_video)
                        
    print movie_title, movie_storyline, movie_image, movie_video
    
    return movie

# create an empty list to hold the movie objects
movies = []

# create the movie objects manually or using the API
if use_api:
    # Ids for movies were pre-checked...
    movies.append(create_movie_from_tmdb("194"))
    movies.append(create_movie_from_tmdb("110"))
    movies.append(create_movie_from_tmdb("28162"))
    movies.append(create_movie_from_tmdb("278927"))
    movies.append(create_movie_from_tmdb("582"))
    movies.append(create_movie_from_tmdb("406"))

else:
    # create the movie list manually
    movies.append(media.Movie("Jungle Book",
    "Meet Mowgli, the man cub. Baloo thinks he'll make a darn good bear. Shere Khan thinks he'll make a darn good meal",
    "https://upload.wikimedia.org/wikipedia/en/1/1d/Thejunglebook_movieposter.jpg",
    "https://www.youtube.com/watch?v=LNVTKXIK7q8"))
    
    movies.append(media.Movie("Three Colours Red",
    "Valentine is a young model living in Geneva. Because of a dog she ran over, she meets a retired judge who spies his neighbours' phone calls, not for money but to feed his cynicism",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Three_Colors-Red.jpg",
    "https://www.youtube.com/watch?v=RPLpbDFQZpg"))

    movies.append(media.Movie("The Lives of Others",
    "Before the Fall of the Berlin Wall, East Germany's Secret Police Listened to Your Secrets",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
    "https://www.youtube.com/watch?v=n3_iLOp6IhM"))

    movies.append(media.Movie("A Matter of Life and Death",
    "Neither Heaven nor Earth could keep them apart!",
    "https://upload.wikimedia.org/wikipedia/en/3/3f/A_Matter_of_Life_and_Death_Cinema_Poster.jpg",
    "https://www.youtube.com/watch?v=JSruSe_m8OI"))
    
    movies.append(media.Movie("La Haine",
    "Three Young Friends... One Last Chance.",
    "https://upload.wikimedia.org/wikipedia/en/3/30/Haine.jpg",
    "https://www.youtube.com/watch?v=bXnDH2rd_kQ"))

    movies.append(media.Movie("Amelie",
    "She'll change your life",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
    "https://www.youtube.com/watch?v=HUECWi5pX7o"))    
    
# call the webpage generator for the move list
fresh_tomatoes.open_movies_page(movies)