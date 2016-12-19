# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:46:06 2016
A project to create a single webpage which lists movie information
@author: David
"""

# import the movie class and webpage generator
import media
import fresh_tomatoes

# a switch to determine whether to use the film API
use_api = False

# create a list of film names - for when using the API
film_listing = ['Jungle Book','Three Colours Red','The Lives of Others',
                'A Matter of Life and Death','La Haine','Amelie']

# create an empty list to hold the movie objects
movies = []

# create the movie objects manually or using the API
if use_api:
    pass
else:
    # create the movie list manually
    movies.append(media.Movie(film_listing[0],
    "Meet Mowgli, the man cub. Baloo thinks he'll make a darn good bear. Shere Khan thinks he'll make a darn good meal",
    "https://upload.wikimedia.org/wikipedia/en/1/1d/Thejunglebook_movieposter.jpg",
    "https://www.youtube.com/watch?v=LNVTKXIK7q8"))
    
    movies.append(media.Movie(film_listing[1],
    "Valentine is a young model living in Geneva. Because of a dog she ran over, she meets a retired judge who spies his neighbours' phone calls, not for money but to feed his cynicism",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Three_Colors-Red.jpg",
    "https://www.youtube.com/watch?v=RPLpbDFQZpg"))

    movies.append(media.Movie(film_listing[2],
    "Before the Fall of the Berlin Wall, East Germany's Secret Police Listened to Your Secrets",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
    "https://www.youtube.com/watch?v=n3_iLOp6IhM"))

    movies.append(media.Movie(film_listing[3],
    "Neither Heaven nor Earth could keep them apart!",
    "https://upload.wikimedia.org/wikipedia/en/3/3f/A_Matter_of_Life_and_Death_Cinema_Poster.jpg",
    "https://www.youtube.com/watch?v=JSruSe_m8OI"))
    
    movies.append(media.Movie(film_listing[4],
    "Three Young Friends... One Last Chance.",
    "https://upload.wikimedia.org/wikipedia/en/3/30/Haine.jpg",
    "https://www.youtube.com/watch?v=bXnDH2rd_kQ"))

    movies.append(media.Movie(film_listing[5],
    "She'll change your life",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
    "https://www.youtube.com/watch?v=HUECWi5pX7o"))    
    
# call the webpage generator for the move list
fresh_tomatoes.open_movies_page(movies)