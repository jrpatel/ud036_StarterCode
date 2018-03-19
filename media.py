class Movie():
    " " "Creates Movies with title, imageUrl and trailerUrl. """

    def __init__ (self , title , postUrl , trailerUrl):
    	" " "Inits Movie class with title , postUrl, trailerUrl. """
    	self.title = title;
    	self.poster_image_url = postUrl;
    	self.trailer_youtube_url = trailerUrl;
