# Phil Kirker CSC110 Fall 2021
# Assignment 7 
import calendar
import doctest


#Type Alias'
Date_Info = tuple[int,int,int]
YEAR=0
MONTH=1
DAY=2

Netflix_Info = tuple[str, str, list[str], list[str], Date_Info]
TYPE= 0
TITLE = 1
DIRECTORS= 2
ACTORS = 3
Date_Info = 4


def multiply_by (list1 : list[int], list2: list[ int]) -> None:
    '''This function takes 2 lists of ints as arguments. It multiplys list1 
    by the respective element in list2, the produce changes the values stored 
    in list1. If list2 is longer than list1 only the length of elements in list1
    will be multiplied from list2. If list2 is shorter than list1 a one is added
    onto the end of list to so multiplication continues 
    
    >>> multiply_by([0,0,0,0,0], [1,2,3,4])
    [0, 0, 0, 0, 0]
  
    >>> multiply_by([-1,-2,-3,-4], [1,2,3,4])
    [-1, -4, -9, -16]
    
    >>> multiply_by([1,2,3,4], [1,2,3,4])
    [1, 4, 9, 16]
    
    >>> multiply_by([1,2,3], [1,2,3,4])
    [1, 4, 9]
    
    '''
    list3 = list2
    
    length_diff =len(list1) - len(list2)
    
    if len(list1) > len(list2):
        
        for j in range(length_diff):

            list3.append(1)
    
    for i in range(len(list1)):
        
        list1[i] = list1[i] * list3[i]
        
    
    return list1


def create_date (date : str) -> tuple:
    '''This function takes a string as an argument in the format of day month
    year, separateed by '-' months being an abreviation i.e. ' Jan'. This string
    will be taken and turned into a tuple of the date, swapping the month
    abreviation with a number. This date tuple uses the type alias Date_Info 
    which can be found at the top of this py file.
    
    >>> create_date('10-Jan-18')
    (2018, 0, 10)
    
    >>> create_date('9-Mar-19')
    (2019, 2, 9)

    >>> create_date('9-Dec-20')
    (2020, 11, 9)
    
    '''
       
    as_list = date.split('-')
    day = as_list[0]
    month = as_list [1]
    year = as_list[2]
        
    month_list= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
                     'Sep','Oct', 'Nov', 'Dec']
    
    year = 2000 + int(year) 
        
    for i in range (len(month_list)):
            if month in month_list[i]:
                month_as_num= i
                
    date_as_tuple = (int(year), month_as_num, int(day)) 
            
    return date_as_tuple
    
    
def create_show(Type: str, Title: str, Directors: str, Actors: str, Date: str)-> Date_Info: 
    ''' 
    This function takes a string of 5 arguments and creates a netflix show tuple
    as outlined by the Netflix_Info type alias found at the top of this .py file
    The string format for this are as follows:
    

    >>> create_show('Movie', 'The Invention of Lying', 'Ricky Gervais:Matthew Robinson', 'Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey', '02-Jan-18')
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 0, 2))
    
    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09')
    ('TV Show', 'The Mind Explained', [''], ['Emma Stone'], (2009, 8, 12))
    
    '''
    
    Date = create_date(Date)
    
    Netflix_Info = (Type, Title, Directors.split(':'), Actors.split(':'), Date)
    
    return Netflix_Info


def get_titles( netflix_list:list[Netflix_Info] ) -> list:
    ''' This function takes a list of Netflix shows' Netflix_Info type alias / 
    tuples and returns a list of all the titles of the shows in order of their
    input.
    
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))])
    ['The Invention of Lying', 'The Mind Explained']
    
    
    '''
    
    titles = []
    
    for i in netflix_list:
        
        titles.append(i[TITLE])
        
    print (titles)


def is_actor_in_show (showinfo: Netflix_Info, name: str) -> bool:
    ''' This function takes in a netflix shows' type alias / tuple and returns
    a boolean value determining if the show contains the name of the other 
    argument ( a string).
    
    >>> is_actor_in_show (('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Rob Lowe')
    True
    
    >>> is_actor_in_show (('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'rob lowe')
    True

    >>> is_actor_in_show (('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'lob rowe')
    False
    
    '''
    
    actors = str(showinfo[ACTORS])
        
    if name.casefold() in actors.casefold():
        
        return True
    
    else:
        return False
    

def count_shows_before_date (showlist: list[Netflix_Info], Date: Date_Info) -> int:
    ''' This function takes a list of netflix info type alias' and a specified
    date tuple, it then returns the count of the amount of netflix tuples within
    the list were added before the supplied date. 
    
    >>> count_shows_before_date ([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)),('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], (2018, 12,12))
    2
        
    '''
    count = 0
    
    for i in showlist:
        
        if i[Date_Info] < Date:
            count +=1
            
    return count
    
    
    
def get_shows_with_actor (showlist: list[Netflix_Info], actor:str) -> list:
    ''' This function takes a list of netflix show tuples and an actors name
    as a string. The function determines and returns only the netflix tuples
    which contain the specified actor.
    
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)),('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)),('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], 'Emma Stone')
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]

    
    '''
    
    staring_shows = []
    
    for i in showlist:
        for j in showlist[ACTORS]:
        
            if is_actor_in_show(i, actor) and i not in staring_shows:
                
                staring_shows.append(i)
    
    return staring_shows