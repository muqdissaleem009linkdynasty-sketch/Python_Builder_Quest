movies = ["Inception", "Interstellar", "Coco", "The Batman", "Dune"]


def find_movie(movies, wanted):
    for movie in movies:
        if movie.lower() == wanted.lower():
            return f"Found: {movie}"

    return "Movie not found."


wanted = input("Enter movie: ")

result = find_movie(movies, wanted)

print(result)