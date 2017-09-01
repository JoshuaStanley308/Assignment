
# imports the item getter operator to help sort the songs
from operator import itemgetter

# displays program title
print("Songs To Learn 1.0 - by Joshua Stanley")

# sets the menu
MENU = """Menu:
    L - List songs
    A - add new song
    C - Complete a song
    Q - Quit"""


def main():

    # get data from a separate file
    in_file = open("songs.csv", 'r')

    # format the data in the file
    song_list = reformat_data(in_file)

    # display how many songs were loaded
    print("{} songs loaded".format(len(song_list)))
    # creates the menu

    # print the menu and get an input
    choice = menu_input()

    while choice != "Q":
        if choice == "L":

            list_songs(song_list)

        elif choice == "A":

            add_song(song_list)

        elif choice == "C":

            complete_song(song_list)

        # display message if input is invalid and get another input
        else:
            print("Invalid menu choice")
        choice = menu_input()

    # save the data to a separate document
    save_data(song_list)
    # display how many songs have been saved
    print("{} songs saved to songs.csv".format(len(song_list)))
    # close the original file
    in_file.close()
    print("Goodbye :)")


def save_data(song_list):
    out_file = open("songs.csv", 'w')
    for i in range(0, len(song_list)):
        out_file.write("{}, {}, {}, {}\n".format(song_list[i][0], song_list[i][1], song_list[i][2], song_list[i][3]))
    out_file.close()


def complete_song(song_list):
    # check to see how many songs have been learnt
    songs_required = songs_required_counter(song_list)

    # check to see if all the songs have been learnt
    if songs_required != 0:

        # Get input from user for which song to be learnt
        print("Enter the number of a song to mark as learned")
        song_number = input(">>> ")

        # check to see if there are any errors in the input
        song_number = error_check_input(song_list, song_number)

        # check to see if is already been learnt
        if "y" not in song_list[int(song_number)][3]:
            print("You have already learned {}".format(song_list[int(song_number)][0]))
        else:
            song_list[int(song_number)][3] = "n"
            print("{} by {} learned".format(song_list[int(song_number)][0], song_list[int(song_number)][1]))
    else:
        print("No more songs to learn!")


def error_check_input(song_list, song_number):
    correct_input = False
    while not correct_input:
        try:
            if len(song_list) == 0:
                print("Input can not be blank")
                song_number = input(">>> ")
            elif int(song_number) >= len(song_list):
                print("Invalid song number")
                song_number = input(">>> ")
            elif int(song_number) < 0:
                print("Number must be >= 0")
                song_number = input(">>> ")
            else:
                correct_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
            song_number = input(">>> ")

    return song_number


def songs_required_counter(song_list):
    songs_learnt = 0
    songs_required = 0
    for i in range(len(song_list)):
        if song_list[i][3] == "y":
            songs_required += 1
        else:
            songs_learnt += 1

    return songs_required


def add_song(song_list):

    # get the title
    song_title = get_title()

    # get the artist
    song_artist = get_artist()

    # get the release year
    song_year = get_year()

    # Add the song into the list
    new_song = [song_title, " {}".format(song_artist), " {}".format(song_year), "y"]
    song_list.append(new_song)
    # sort the list by artist
    song_list.sort(key=itemgetter(1, 0))

    # display message stating song has been added
    print("{} by {} {} added to song list".format(song_title, song_artist, song_year))


def get_year():
    correct_input = False
    while not correct_input:
        try:
            # get the release year
            song_year = input("Year: ")

            # check to see if there are any errors in the input
            if len(song_year) == 0:
                print("Input can not be blank")
            elif int(song_year) < 0:
                print("Number must be >= 0")
            else:
                correct_input = True
        except ValueError:
            print("Invalid input; enter a valid number")

    return song_year


def get_artist():
    song_artist = input("Artist: ")
    # check to see if there is any errors in the input
    while len(song_artist) == 0:
        print("Input can not be blank")
        song_artist = input("Artist: ")
    return song_artist


def get_title():
    # Get the song title
    song_title = input("Title: ")
    # check to see if there is any errors in the input
    while len(song_title) == 0:
        print("Input can not be blank")
        song_title = input("Title: ")

    return song_title


def list_songs(song_list):

    # sort songs by artist
    song_list.sort(key=itemgetter(1, 0))

    # create variables to keep track of how many songs have been learned
    songs_learnt = 0
    songs_required = 0

    # create blank lists for the length of the titles and artists
    title_length = []
    artist_length = []

    # find the longest character length to help line up the data
    max_artist_length, max_song_length = max_length(artist_length, song_list, title_length)

    # list the songs
    songs_learnt, songs_required = display_song_list(max_artist_length, max_song_length, song_list, songs_learnt,
                                                     songs_required)
    # display the number of songs learnt and required
    print("{} songs learned, {} songs still to learn".format(songs_learnt, songs_required))


def display_song_list(max_artist_length, max_song_length, song_list, songs_learnt, songs_required):
    for i in range(len(song_list)):
        # sort between learned and need to learn
        if "y" in song_list[i][3]:
            print("{:2}. * {:{}} - {:{}} ({})".format(i, song_list[i][0], max_song_length,
                                                      song_list[i][1], max_artist_length, song_list[i][2]))
            songs_required += 1
        else:
            print("{:2}.   {:{}} - {:{}} ({})".format(i, song_list[i][0], max_song_length,
                                                      song_list[i][1], max_artist_length, song_list[i][2]))
            songs_learnt += 1

    return songs_learnt, songs_required


def max_length(artist_length, song_list, title_length):
    # find the length of the titles and artist + put them in the lists
    for i in range(len(song_list)):
        title_length += [len(song_list[i][0])]
        artist_length += [len(song_list[i][1])]

    # find the longest length
    max_song_length = max(title_length)
    max_artist_length = max(artist_length)
    return max_artist_length, max_song_length


def menu_input():

    print(MENU)
    choice = input(">>> ").upper()

    return choice


def reformat_data(in_file):

    # spilt the data up into a list form
    song_list = [line.split(',')[:] for line in in_file]

    # change the "y\n" or "n\n" to just "y" and "n"
    for i in range(len(song_list)):
        if "y" in song_list[i][3]:
            song_list[i][3] = "y"
        else:
            song_list[i][3] = "n"

    return song_list


main()


