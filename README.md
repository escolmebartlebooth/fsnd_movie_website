# Udacity Full Stack Project: Movie Trailer Website

## Basic Information

## Implementation
### Pre-Requisites

This project was built using the **Anaconda** installation of Python 2.7 version 4.1.6, utilisiing the following packages:

+ python 2.7

### Additional python files

The folder structure is:

+     home/

+ entertainment_centre.py: creates the movie database
+ media.py: creates the movie class into which move information can be stored against instances of the class
+ fresh_tomatoes.py: Udacity provided webpage generator which takes in a list of movie objects

### Implementation notes

#### entertainment_centre.py

There will be 2 modes of operation to create the movie list - controlled by the **use_api** variable, whose default value is **False**:

+ mode 1: use_api = False : The movie list is created manually
+ mode 2: use_api = True : Currently, this does not function

#### fresh_tomatoes.py

Some changes have been made to the baseline file provided by Udacity, namely:

+ Imported font from googlefont api (lato)
+ Changed image display size and added title for each image to display movie story line
