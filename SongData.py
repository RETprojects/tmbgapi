import requests
from bs4 import BeautifulSoup

# This function scrapes data from a specific song page on tmbw.net.
def get_song_data(name):
    if name != "They Might Be Giants":
        details_link = "http://tmbw.net/wiki/" + str(name).replace(" ","_")
    else:
        details_link = "http://tmbw.net/wiki/" + str(name).replace(" ","_") + "_(Song)"
    d_data = requests.get(details_link)  # get page data
    d_soup = BeautifulSoup(d_data.text,features="html.parser")  # parse page data
    d_table = d_soup.find('table') # get the first (and only) table on the page
    d_table_head = get_table_head_fields_as_list(d_table)
    d_table_body = get_table_body_as_lists(d_table)
    d_final_table_data = [d_table_head] + d_table_body # join the head data and body data
    #d_final_table_data = d_final_table_data[2:]

    for l in d_final_table_data:
        if "song name" in l[0]:
            name = l[1]
        elif "artist" in l[0]:
            artist = l[1]
        elif "releases" in l[0]:
            releases = l[1]
        elif "year" in l[0]:
            year = l[1]
        elif "first played" in l[0]:
            first_played = l[1]
        elif "run time" in l[0]:
            run_time = l[1]
        elif "sung by" in l[0]:
            singers = l[1]
    
    # Get the lyrics, if any are available.
    lyrics_link = "http://tmbw.net/wiki/Lyrics:" + str(name)


    # Get the credits, if any are available.
    credits_link = "http://tmbw.net/wiki/Credits:" + str(name)


# This function assembles the data from a song page.
def assemble_song_data():


# This function acts as a wrapper for the data from the song page.
def wrap_song_data():


