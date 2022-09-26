import doctest
from date import Date

class Pet:
    """ Pet: represents a domesticated pet with name, species and birthdate """

    def __init__(self, name: str, species: str, birthdate: Date) -> None:
        """ initializes attributes of Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        """
        self.__name      = name
        self.__species   = species
        self.__birthdate = birthdate

    def get_name(self) -> str:
        """ returns name of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> dog.get_name()
        'Rover'
        """
        return self.__name

    def get_species(self) -> str:
        """ returns species of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> dog.get_species()
        'Dog'
        """
        return self.__species
    
    def get_birthdate(self) -> Date:
        """ returns date of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        
        >>> dog.get_birthdate()
        Date(12, 19, 2020)
        """
        return self.__birthdate
    
    def __str__(self) -> str:
        """ returns a readable string with name, species, birthdate of Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> str(dog)
        'Rover is a Dog. Born: 12-19-2020'
        """
        return f'{self.__name} is a {self.__species}. Born: {self.__birthdate}'
    
    def __repr__(self) -> str:
        """ returns a string representation of self Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> repr(dog)
        "Pet('Rover', 'Dog', Date(12, 19, 2020))"
        """
        return f"Pet('{self.__name}', '{self.__species}', {repr(self.__birthdate)})"






