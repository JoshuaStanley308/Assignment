from operator import itemgetter

print("Songs To Learn 1.0 - by Joshua Stanley")

# get data from a separate file
in_file = open("List of songs.csv", 'r')

# format the data in the file
song_list = [line.split(',')[:] for line in in_file]
song_list.sort(key=itemgetter(1, 0))

# display how many songs were loaded
print(len(song_list), "songs loaded")

MENU = """Menu:
L - List songs
A - add new song
C - Complete a song
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "L":
        songs_learnt = 0
        songs_required = 0
        # list the songs
        for i in range(len(song_list)):
            if "y" in song_list[i][3]:
                print("{}. * {:<30s} - {:<30s} ({})".format(i, song_list[i][0], song_list[i][1], song_list[i][2]))
                songs_required += 1
            else:
                print("{}.   {:<30s} - {:<30s} ({})".format(i, song_list[i][0], song_list[i][1], song_list[i][2]))
                songs_learnt += 1
        # display the number of songs learnt and required
        print("{} songs learned, {} songs still to learn".format(songs_learnt, songs_required))

    elif choice == "A":
        print("A")
        # Get data for the song(Title, artist, year)
        # Add the song into the list and sort by artist name
        # display message stating song has been added

    elif choice == "C":
        print("C")

        # Get input from user for which song to be learnt
        # check to see if is already been learnt
        # if learnt show menu
        # if not, display a message saying it has been learnt

    else:
        print("Invalid menu choice")
    print(MENU)
    choice = input(">>> ").upper()

# save the data to a separate document
# display how many songs have been saved
in_file.close()

print("Goodbye :)")


