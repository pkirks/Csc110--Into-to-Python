import doctest
import datetime


# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10


def create_date (date : str) -> tuple:
    '''This function takes a string as an argument in the format of day month
    year, separateed by '-' months being an abreviation i.e. ' Jan'. This string
    will be taken and turned into a tuple of the date, swapping the month
    abreviation with a number. This date tuple uses the type alias Date_Info 
    which can be found at the top of this py file.
    
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    
    >>> create_date('9-Mar-19')
    (2019, 3, 9)

    >>> create_date('9-Dec-20')
    (2020, 12, 9)
    
    '''
      
    as_list = date.split('-')
    
    day = as_list[0]
    month = as_list [1]
    year = as_list[2]

    month_list= ['','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
                     'Sep','Oct', 'Nov', 'Dec']
    
    year = 2000 + int(year) 
        
    for i in range (1,len(month_list)):
            if month in month_list[i]:
                month_as_num= i
                
    date_as_tuple = (int(year), month_as_num, int(day)) 
            
    return date_as_tuple


def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]]):
    '''
    Populates and returns a tuple with the following 3 dictionaries
    with data from valid filename.
    
    3 dictionaries returned as a tuple:
    - dict[show title: date added to Netflix]
    - dict[show title: list of actor names]
    - dict[category: list of show titles]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show title: list of actor names]
    
    Precondition: filename is csv with data in expected columns 
        and contains a header row with column titles.
        NOTE: csv = comma separated values where commas delineate columns
        Show titles are considered unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {})
    
    >>> read_file('11lines_data.csv')
    ({'SunGanges': (2019, 11, 15), \
'PK': (2018, 9, 6), \
'Phobia 2': (2018, 9, 5), \
'Super Monsters Save Halloween': (2018, 10, 5), \
'First and Last': (2018, 9, 7), \
'Out of Thin Air': (2017, 9, 29), \
'Shutter': (2018, 9, 5), \
'Long Shot': (2017, 9, 29), \
'FIGHTWORLD': (2018, 10, 12), \
"Monty Python's Almost the Truth": (2018, 10, 2), \
'3 Idiots': (2019, 8, 1)}, \
\
{'SunGanges': ['Naseeruddin Shah'], \
'PK': ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], \
'Phobia 2': ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], \
'Super Monsters Save Halloween': ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], \
'Shutter': ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], \
'FIGHTWORLD': ['Frank Grillo'], "Monty Python's Almost the Truth": ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], \
'3 Idiots': ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey']}, \
\
{'Documentaries': ['SunGanges', 'Out of Thin Air', 'Long Shot'], \
'International Movies': ['SunGanges', 'PK', 'Phobia 2', 'Out of Thin Air', 'Shutter', '3 Idiots'], \
'Comedies': ['PK', '3 Idiots'], \
'Dramas': ['PK', '3 Idiots'], 'Horror Movies': ['Phobia 2', 'Shutter'], \
'Children & Family Movies': ['Super Monsters Save Halloween'], \
'Docuseries': ['First and Last', 'FIGHTWORLD', "Monty Python's Almost the Truth"], \
'British TV Shows': ["Monty Python's Almost the Truth"]})
    '''
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    date_dict = {}
    actor_dict = {}
    categ_dict= {}
    categ_list = []
    title_list= []
    
    
    file_handle = open(f'{filename}', 'r', encoding="utf8")
    next(file_handle)
    
    for line in file_handle:
        line = line.strip()
        list_of_strings = line.split(',')
    
        title= list_of_strings[INPUT_TITLE]
        cast_list = list_of_strings[INPUT_CAST].split(':')
        date = list_of_strings[INPUT_DATE]
        categ = list_of_strings[INPUT_CATEGORIES].split(':')
        
        Date = create_date(date) 
        date_dict[title] = Date 
        
        if len(cast_list) > 1:  
            actor_dict[title]  = cast_list
        
        for i in categ: # list of all types
            cat=categ_dict.get(i,0)

            if categ_dict.get(i,0)==0:
                title_list=[title]
                categ_dict.update({i:title_list})
            else:
                trans_list=categ_dict[i]
                trans_list.append(title)
                categ_dict.update({i:trans_list})        
        
    file_handle.close()
        
    return (date_dict, actor_dict, categ_dict) 
    

def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[str]:
    '''
    returns a list of sorted show titles of only shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'not found', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'Aamir Khan', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either', 'Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dil Chahta Hai', 'Dil Dhadakne Do', 'PK', 'Zed Plus']
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dangal', 'Dhobi Ghat (Mumbai Diaries)', \
'Dil Chahta Hai', 'Dil Dhadakne Do', 'Lagaan', 'Madness in the Desert', 'PK', \
'Raja Hindustani', 'Rang De Basanti', 'Secret Superstar', 'Shutter', \
'Taare Zameen Par', 'Talaash', 'Zed Plus']
    '''
    # TODO: complete this function according to the documentation

    #returns a list of sorted show titles of only shows that:
    #- are of the given category
    #- have at least one of the actor names in actors in the cast
    #- were added to Netflix before the given date
    
    movies = []
    
    date_info, cast_info, genre_info= read_file(filename) 

    for key in date_info:
        #print(date_info[key])
        if date_info[key] <= date:
            print('yers')
    
    for ley in cast_info:
        if cast_info[ley] in actors:
            print('in actors oui') 
            
    for mey in genre_info:
        if genre_info[mey] is category:
            print('genre is good')