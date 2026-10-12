movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
def rat (ratings):
    """Return the average of a list of ratings."""
    return round(sum(ratings) / len(ratings), 2)

def filter_movies(movies):
    result = []
    for title, year, ratings in movies:
        average = rat(ratings)
        if average > 6.0:
            result.append((title, year, average))
    return result

def get_average(movie):
    return movie[2]

def display_movies(good_movies):
    sorted_movies = sorted(good_movies, key=get_average, reverse=True)
    number = 1
    for title, year, average in sorted_movies:
        print (f"{number}. {title} ({year}) - Average rating: {average: .2f} ")
        number += 1

display_movies (filter_movies(movies))