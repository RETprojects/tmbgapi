# tmbgapi
This is an API that scrapes data from [tmbw.net](http://tmbw.net/wiki/Main_Page), the official wiki for the iconic alternative rock duo They Might Be Giants. So far, the API allows users to access data about every live TMBG show that has been recorded on the wiki.

## Endpoints
There are several endpoints that are intended to be covered in the development of this API.

- Shows: Information about live shows, such as date, venue, city, the wikians who attended, and the setlist.

- Albums: Information about studio albums, singles, EPs, and other releases. Returns name, type of release, date released, length, record label, number of tracks, tracklist, and cover image.

- Songs: Information about songs, such as name, date released, length, releases the song was featured on, singer(s), lyrics, date first played as part of a live performance, and credits.

## Schemas
Here are the schemas that are used or may be used for this API.

### Show Schema

```
{
  "Date": 0000,
  "Venue": "", 
  "City": "",
  "Attendance": {
    "Number": 0,
    "Names": [
      "user1", "user2"
    ]
    
  },
  
  "Setlist": {
  
    "Set 1": [
    
      "song1", "song2"
      
    ]
    
  },
  
  "Link": ""
  
}
```

### Album Schema

```
{

	"Name": "",
  
	"Type": "",
  
	"Date": {Date Object},
  
	"Year": #,
  
	"Length": "",
  
	"Label": "",
  
	"Number of Tracks": #,
  
	"Cover": {Image File},
  
	"Tracklist": [
  
		{Song Object},...
    
	]
  
}
```

### Credits Schema

```
{

	"Credits": {
  
		key:value,...
    
	}
  
	"Vocals": {
  
		key:value,...
    
	}
  
	"Instruments": {
  
		key:value,...
    
	}
  
	"Production": {
  
		key:value,...
    
	}
  
}
```

### Date Schema

```
{

	"Month": "" or #,
  
	"Day": #,
  
	"Year": #
  
}
```

### Song Schema

```
{

	"Name": "",
  
	"Date": {Date Object},
  
	"Year": #,
  
	"Length": "",
  
	"Releases": [
  
		{Album Object},...
    
	],
  
	"First Played": {Date Object},
  
	"Singer(s)": "",
  
	"Lyrics": "",
  
	"Credits": {Credits Object}
  
}
```

## Roadmap for future endpoints

- [X] `/Shows/<year>`
- [ ] `/Song/<title>`
- [ ] `/Discography`
- [ ] `/Album/<title>`

## How the API works
For the Shows endpoint, for example, the API can be used by calling the Shows() wrapper function using a particular year as a parameter. Let's say you want to see information about the live TMBG shows that occurred in 1992. You would call Shows(1992). The API would then access the page http://tmbw.net/wiki/Shows/1992, which contains a table recording all known live TMBG shows that occurred in 1992. The API scrapes information from this table, accessing each show entry one by one. The values for Date (e.g., "1992-10-05"), Venue (e.g., "Modjeska Theatre (The infamous stage collapse show)", including any possible subtitle), and City (e.g., "Milwaukee, WI") are grabbed immediately. For Attendance, the API grabs the number of wikians who attended the show (e.g., 3 for "Attendance (3)"). The API then seeks to get the names of the wikians who may have attended. This is accomplished by accessing the existing page for the show (e.g., http://tmbw.net/wiki/Shows/1992-10-05). The API then finds and scrapes the section of the page containing the names of the wikians who attended the show and grabs each name sequentially (e.g., "Airrun95", "Jowley", "ToddMightBeOld"). All show entries are scraped in this fashion and processed according to the show schema (see above). The Shows() function returns a JSON-formatted dataset of shows using this schema for every known live TMBG show in 1992.

Thanks for checking out this API!
