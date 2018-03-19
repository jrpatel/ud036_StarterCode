import media
import fresh_tomatoes


def create_movies():
	#creates list for movie object   
    jumanji = media.Movie ("Jumanji 2","https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyNDQ1MDc5OV5BMl5BanBnXkFtZTgwOTcyNzI2MzI@._V1_.jpg","https://www.youtube.com/watch?v=2QKg5SZ_35I");
    lion    = media.Movie("Lion", "http://t0.gstatic.com/images?q=tbn:ANd9GcTVuFTo4qf9v0c91rhTcSn25dsQygPhIRdivLe8Z1HdZNiPCj2F","https://www.youtube.com/watch?v=GNrM-wqKMok");
    room    = media.Movie("The Room", "http://t1.gstatic.com/images?q=tbn:ANd9GcSu9dR_6oOzsDvAq76vlBqPsyYNHdLw3jRRrmJVb7EBPTQBryV1" , "https://www.youtube.com/watch?v=PPZqF_TPTGs");
    wonderWoman = media.Movie("Wonder Woman","http://images.thesubtitles.net/movie/wonder_woman_2017.jpg","https://www.youtube.com/watch?v=VSB4wGIdDwo");
    dearzindagi = media.Movie("Dear Zindagi","https://images-na.ssl-images-amazon.com/images/M/MV5BZWQzYWI3ZGMtYzgyYy00OWZkLWEwODYtNGNiMTZhODBkNzUyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_SY1000_CR0,0,750,1000_AL_.jpg","https://www.youtube.com/watch?v=5DkO7ksXY8E");
    queen = media.Movie("Queen","http://t2.gstatic.com/images?q=tbn:ANd9GcRrt1YcpBelyLKnadqLZOHrcFuq_Lt12qEmPshRXKszw3eYWOV8","https://www.youtube.com/watch?v=KGC6vl3lzf0");
    movies = [jumanji , lion ,room ,wonderWoman, dearzindagi, queen];
    # pass movie list to open_movie_page for display.
    fresh_tomatoes.open_movies_page(movies);

# starts execution of program
create_movies()


