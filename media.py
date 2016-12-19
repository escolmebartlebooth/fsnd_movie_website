# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:39:55 2016
A class to store information about movies
@author: David
"""

# Movie class to store information about movies
class Movie():
    """ A class for depicting moives"""
    
    # constructor
    def __init__(self,movie_title, storyline, 
                 poster_image, youtube_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url