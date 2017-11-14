import media
import fresh_tomatoes

toy_story = media.Movie("toystory", 
        "A story of a boy and his toys that come to life",
        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
        "https://www.youtube.com/watch?v=LJnlmJ4lqik")

movies = [toy_story]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)