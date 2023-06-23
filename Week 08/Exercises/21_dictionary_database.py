#Please write a function named add_movie(database: list, name: str,
#director: str, year: int, runtime: int), which adds a new movie object into a
#movie database.

#The database is a list, and each movie object in the list is a dictionary.
#The dictionary should contain the following keys.

    #name
    #director
    #year
    #runtime

#The values attached to these keys are given as arguments to the function.


def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_entry = {}


    new_entry["name"] = name
    new_entry["director"] = director
    new_entry["year"] = year
    new_entry["runtime"] = runtime

    database.append(new_entry)

    print(database)


if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)



