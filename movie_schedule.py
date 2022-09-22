current_movies = {'The Grinch':'11:00 AM',
                'Rudolph':'1:00 PM',
                'Frosty the Snowman':'3:00 PM',
                'Christmas Vacation':'5:00 PM'}
print("Now Playing: \n")
for key in current_movies:
    print(key)
what_movie =input("What movie do you want to watch?")
showtime = current_movies.get(what_movie)
if showtime == None:
    print("Not a valid movie bro")
else:
    print(what_movie, 'is playing at ',showtime)