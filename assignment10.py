import doctest

from pet import Pet
from date import Date


# represents a pet as (name, species)
PetNameSpecies = tuple[str,str]

# columns of values within input file row and within PetNameSpecies tuple
NAME    = 0
SPECIES = 1
MONTH   = 2
DAY     = 3
YEAR    = 4


def read_file(filename: str) -> list[Pet]:
    ''' returns a list of Pets populated with data from filename
    
    Preconditions: filename exists.
    If filename is not empty, each row has a single Pet's information
    separated by commas with expected values at columns:
    NAME, SPECIES, MONTH, DAY and YEAR.

    >>> read_file('empty.csv')
    []
    >>> read_file('pet_data.csv')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    '''
    # TODO: complete this function
    total_list= []
    
    filehandle = open(filename, 'r', encoding = 'utf8')
    
    for pet in filehandle:
        pet = pet.strip()
        pet_list = pet.split(',')
        
        if len(pet_list) <= 1:
            return total_list        
        
        dt = Date(pet_list[MONTH],pet_list[DAY],pet_list[YEAR])
                
        current_pet = Pet(pet_list[NAME], pet_list[SPECIES], dt)
        this_pet = repr(current_pet)
        
        total_list.append(current_pet)
    filehandle.close()
    
    return total_list
        

def find_pet(lopets: list[Pet], name: str) -> int:
    ''' returns the position of pet with given name in lopets
    Returns -1 if name not found
    Returns the position of the first found if there >1 Pet with the given name
    
    Precondition: name must match case exactly
    ie. 'rover' does not match 'Rover'

    >>> find_pet([], 'Fred')
    -1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Bowser')
    -1
    >>> find_pet([Pet('Red', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    0
    '''
    # TODO: complete this function
    list_position = 0
    
    for i in lopets:
        if name == i.get_name(): 
            return list_position
            
        list_position +=1
    
    return -1
       

def get_all_of_species(lopets: list[Pet], species: str) -> list[Pet]:
    ''' returns a list of all pets of the given species.
    Result list is not necessarily unique, if >1 Pet in lopets has the same name.
    
    Precondition: species must match case exactly
    ie. 'dog' does not match 'Dog'
    
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_all_of_species([], 'Dog')
    []
    >>> get_all_of_species(pets, 'Dog')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_all_of_species(pets, 'Tiger')
    []
    >>> get_all_of_species(pets, 'Hamster')
    [Pet('Chewie', 'Hamster', Date(1, 23, 2009))]
    '''
    # TODO: complete this function
    spec_list = []
    
    for i in lopets:
        if species == i.get_species():
            spec_list.append(i)
   
    return spec_list
   
   
def get_latest_birthdate(lopets: list[Pet]) -> Date:
    ''' returns the latest Date of all birthdates of Pet instances in lopets
    Precondition: lopets is not empty
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_latest_birthdate([Pet('Rover', 'Dog', Date(12, 31, 2010))])
    Date(12, 31, 2010)
    >>> get_latest_birthdate(pets)
    Date(9, 15, 2016)
    '''
    # TODO: complete this function
    adj= 0
    youngest = lopets[0].get_birthdate()
    y_month = youngest.get_month() 
    y_day = youngest.get_day() 
    y_year = youngest.get_year()
    youngest_final = ( y_year, y_month, y_day)
    
    
    for i in lopets:
        dt= i.get_birthdate()
        dt_month = dt.get_month()
        dt_day = dt.get_day()
        dt_year = dt.get_year()
        date_final = (dt_year, dt_month, dt_day)
        
        
        if date_final > youngest_final:
            youngest_final = date_final
            to_return = Date(dt_month, dt_day, dt_year)
            adj =1
    
    if adj == 0:
        to_return = Date(y_month, y_day, y_year) 
    
    return to_return
    

def get_youngest_pets(lopets: list[Pet]) -> list[PetNameSpecies]:
    ''' returns a list of PetNameSpecies of all the youngest pets in lopets
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_youngest_pets([])
    []
    >>> get_youngest_pets(pets)
    [('Red', 'Cat'), ('Scout', 'Dog')]
    '''
    # TODO: complete this function
    
    PetNameSpecies = []
    
    if len(lopets) == 0:
        return PetNameSpecies        
    
    dt = get_latest_birthdate(lopets)
    
    dt_final = repr(dt) 
    #print(dt_final)
    
    for i in lopets:
        pet_bday = i.get_birthdate()
        bday = repr(pet_bday)  
        
        if bday == dt_final:
            to_append = i.get_name(), i.get_species()
            PetNameSpecies.append(to_append)
         
    
    return PetNameSpecies

