import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

comet = media.Movie("Comet",
                     "A chance encounter begins a tempestuous love affair that unfolds like a puzzle",
                     "https://upload.wikimedia.org/wikipedia/en/8/87/Comet_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=aUpQhgl9PGQ")

movies = [toy_story, avatar, comet]
fresh_tomatoes.open_movies_page(movies)
