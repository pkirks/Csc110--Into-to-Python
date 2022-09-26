import doctest
import csv
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

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

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


def read_file(filename: str) -> list[NetflixShow]:
    '''
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    '''
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    list_of_shows= []
    
    file_handle = open(f'{filename}', 'r', encoding="utf8")
    next(file_handle)
    
    for show in file_handle:
        i = show.split(',')
        
        if len(i[3]) > 0:   
            directors = i[3].split(':') 
        
        else:
            directors= []
            
        if len(i[4]) > 0:
            actors = i[4].split(':')
        
        else:
            actors= []
        
        Date = create_date(i[6])
        
        NetflixShow = (i[1], i[2], directors, actors, Date)
        
        list_of_shows.append(NetflixShow)
    
    return list_of_shows
        
        
        

def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    '''
    returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    '''
    # TODO: complete this function according to the documentation
    lot= []
    
    if len(show_data) > 0:
        oldest = show_data[0][DATE]
        
        for show in show_data: # find oldest date
            if show[DATE] <= oldest:
                oldest = show[DATE]
        
        for show in show_data: # select films equal to oldest date
            if show[DATE] == oldest:
                lot.append(show[TITLE])
                
        return lot
    
    else:
        return []
    

def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    '''
    returns a list of actor names that are found in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts)
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers', 'Michael Cera', 'Emma Stone', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Om Puri', 'Jonah Hill']
    '''
    # TODO: complete this function according to the documentation
    
    all_casts = []
    most_popular_actor = []
    most_shows = 0
    test_list = {}
    movie_list= []
    
    if len(shows) <= 0: 
        return []
    
    for show in shows:
        for i in show[CAST]:
            all_casts.append(i)
    
    for j in all_casts:
        test_list[j] = all_casts.count (j)
    
        
    for k in all_casts:
        if test_list[k] > most_shows:
            most_shows = test_list[k]
            
            most_popular_actor.clear()            
            most_popular_actor.append(k)
            
        elif test_list[k] == most_shows:
            
            if k not in most_popular_actor:  
                most_popular_actor.append(k)
                
    return most_popular_actor
    

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]
                                 ) -> list[NetflixShow]:
    '''
    returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, [])
    []

    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword)
    [('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]
    '''
    # TODO: complete this function according to the documentation
    results= []
    
    if len(show_data) == 0 or len(terms) == 0: 
        return []
    
    for term in terms:    
        for show in show_data:
            
            if term.lower() in show[TITLE].lower(): 
                results.append(show)
                
    results.sort()   #there doesn't appear to be a correct order.....
    return results



def query(show_data: list[NetflixShow]) -> list[str]:
    '''
    Returns a list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.
    The returned list is in sorted order and does not contain duplicate entries.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    '''
    # TODO: complete this function according to the documentation
    movie_list= []
    all_casts = []
    most_popular_actor = []
    most_shows = 0
    test_list = {}
    
    if len(show_data) <= 0: 
        return []
    
    for show in show_data:
        for i in show[CAST]:
            all_casts.append(i)
    
    for j in all_casts:
        test_list[j] = all_casts.count (j)
    
        
    for k in all_casts:
        if test_list[k] > most_shows:
            most_shows = test_list[k]
            
            most_popular_actor.clear()            
            most_popular_actor.append(k)
            
        elif test_list[k] == most_shows:
            
            if k not in most_popular_actor:  
                most_popular_actor.append(k)
            
    
    for actors in most_popular_actor:
        for show in show_data:
            if actors in show[CAST] and show[TITLE] not in movie_list:
                movie_list.append(show[TITLE])
    
    movie_list.sort()
    
    return movie_list