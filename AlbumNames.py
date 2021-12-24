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
print(final_table_data[0][1])