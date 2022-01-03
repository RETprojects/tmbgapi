import requests
from bs4 import BeautifulSoup
import re

# Let's return info about shows for a calendar year.

# Let's assume the schema looks like this:
schema = [  # it's a list of shows
    {   # this is a "show object"
        "date": 0000,
        "venue": "",    # some venues have a subtitle
        "city": "",
        "attendance": {
            "number": 0,
            "names": [  # usernames of ppl who went
                "user1", "user2"
            ]
        },
        "setlist": {
            "set 1": [
                "song1", "song2"
            ]
        },
        "link": ""
    }
]


def scrape_showlist(year):
    '''Scrapes info from the main "Shows" page
    '''
    baseUrl = "http://tmbw.net/wiki/Shows/" # append to this to get a specific year
    url = baseUrl + str(year)
    
    pageData = requests.get(url)    # grab all the HTML using a GET request
    soup = BeautifulSoup(pageData.text, features="html.parser") # create BeautifulSoup object to grab what we want

    # the stuff is in a table with id="showtable". We prefer id bc it's unique.
    showtable = soup.find(id="showtable")
    tablerows = showtable.find_all("tr")    # a list of table rows
    
    # now we're going to get a list of info that we will shove in the schema.
    # it takes the form of an incomplete schema (parts of info are there, some are missing)
    showlist = []   # we'll append to this
    # loop thru table rows
    for row in tablerows[1:]:   # the [1:] is for skipping the header
        # now we need to grab the table datas with the info.
        datas = row.find_all("td")

        link_detail = datas[0].a.get('href')
        if "Template" not in link_detail:
            link = "http://tmbw.net" + link_detail
        else:
            link = link_detail
        
        date = datas[0].a.string

        if datas[1].span is None:
            venue = "Unknown"
        else:
            venue = datas[1].span.a.string
        # sometimes there's a subtitle
        if datas[1].small is not None:
            subtitle = datas[1].small.string
            if subtitle is None:
                subtitle = ""
        else:
            subtitle = ""
        
        venue = venue + " " + subtitle

        city = datas[2].a.string

        attend_num = int("".join(re.findall("\d", datas[3].a.span.b.string)))
        attendees = []
        attend = { "number": attend_num, "names": attendees }
        people = []
        # GET request the page HTML (see above)
        if "Template" not in link and attend_num!=0:
            showPageData = requests.get(link)
            # new soup obj (see above)
            showPageSoup = BeautifulSoup(showPageData.text, features="html.parser")
            # grab the right parent element

            # get parent div (class="showpage-right")
            attend_list = showPageSoup.find(class_="showpage-right")#gets the element w/ class of "showpage-right" (sidebar w/ all atttendees)
            # for each <a> with target="_top"
            for name in attend_list.findAll(target="_top"):#list of elements w/ target="_top" (people's names)
                # get the string, append to the names list
                if name.string is not None and name.string not in "logged in":  # if there are not zero attendees
                    people.append(name.string)#appends a new name to people (a list of names)
            # grab each person's name
        attend["names"] = people

        showlist.append({
            "date": date,
            "venue": venue,
            "city": city,
            "attendance": attend,
            "link": link
        })
        

    return showlist

def Shows(year):
    '''Wrapper function the endpoint will call
    Input: year
    Output: data in format specified by schema
    '''
    # get initial list of shows that year, so pass it to the scrape_showlist function.
    raw_showlist = scrape_showlist(year)
    return raw_showlist