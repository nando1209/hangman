# importing imdb the module  
import imdb
import random

import os
os.system('clear')
  
# creating instance of IMDb  
movies = imdb.IMDb()  
# print(dir(movie_obj))

movies_lst = []

lis1 = movies.get_popular100_movies()
for movie in lis1:
    movies_lst.append(str(movie))
    
print(movies_lst)
