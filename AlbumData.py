import requests
from bs4 import BeautifulSoup

# This function gets the table head and return a list of all the fields in the table head row.
def get_table_head_fields_as_list(table_obj):
    result = []
    table_head = table_obj.find('tr')
    table_head_fields = table_head.find_all('tr')
    for field_obj in table_head_fields:
        result.append(field_obj.getText().strip())
    return result

# This function gets data from a specified album page.
def get_album_data(name):
    return -1

# This function gets the table body and return a list of rows with data fields.
def get_table_body_as_lists(table_obj):
    result = []
    # table_body = table_obj.find('tbody')
    table_rows = table_obj.find_all('tr')
    for row in table_rows:
        curr_row = []
        row_fields = row.find_all('td')
        for field_obj in row_fields:
            curr_row.append(field_obj.getText().strip())
        result.append(curr_row)
    return result

url = 'http://tmbw.net/wiki/Discography'
data = requests.get(url)  # get page data
soup = BeautifulSoup(data.text,features="html.parser")  # parse page data
table = soup.find('table') # get the first (and only) table on the page
#print(table)
table_head = get_table_head_fields_as_list(table)
table_body = get_table_body_as_lists(table)
final_table_data = [table_head] + table_body # join the head data and body data
final_table_data = final_table_data[2:]

# Create an object to represent an album.
#print(final_table_data[0])#.find("a")))
#print(final_table_data[0][1].find("a"))
#details_link = final_table_data[0][1].find("a").get('href')  # get the link
details_link = "http://tmbw.net/wiki/" + str(final_table_data[0][1])
#print(details_link)
d_data = requests.get(details_link)  # get page data
d_soup = BeautifulSoup(d_data.text,features="html.parser")  # parse page data
d_table = d_soup.find('table') # get the first (and only) table on the page
name = final_table_data[0][1]
typ = final_table_data[0][2]
year = final_table_data[0][0]

# Get all releases listed on the Discography page.
for entry in final_table_data:
    name = entry[1]

    details_link = "http://tmbw.net/wiki/" + str(name)
    d_data = requests.get(details_link)  # get page data
    d_soup = BeautifulSoup(d_data.text,features="html.parser")  # parse page data
    d_table = d_soup.find('table') # get the first (and only) table on the page
    d_table_head = get_table_head_fields_as_list(d_table)
    d_table_body = get_table_body_as_lists(d_table)
    d_final_table_data = [d_table_head] + d_table_body # join the head data and body data
    d_final_table_data = d_final_table_data[2:]

    typ = entry[2]
    #date = 
    year = entry[0]
    #length = 
    #num_tracks = 
    #cover = 
    #tracklist = 

