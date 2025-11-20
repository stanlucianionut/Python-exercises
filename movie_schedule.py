
current_movies = {"The Grinch": "11:00 am",
                  "Rudolph": "1:00 pm",
                  "Frosty the snowman": "3:00 pm",
                  "Christmas vacation": "5:00 pm"}

print("We're currently showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing.")
else:
    print(movie, "is playing at ", showtime)