
class Movie():
  """
    The class represents a movie which will be displayed on the movie portal 
  """  
  def __init__(self, movie_title, movie_storyline, movie_trailer_url, poster_image):
   """
     Intializes the Movie class. Arguments are displayed in order

     title - displays the movie title.
     storyline - displays the movie storyline
     trailer - url of the movie trailer
     poster image - image location of the movie poster.
     
   """
   self.title = movie_title
   self.trailer = movie_trailer_url
   self.storyline = movie_storyline
   self.poster_image = poster_image
