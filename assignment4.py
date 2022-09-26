#Phil Kirker CSC110 UVIC Fall 2021
# Assignment 3
import doctest



def is_proper_divisor(n1 :int, n2: int)->bool:
    '''this function determines if n1 is proper divisor of n2.
    
    Precondition: n1 and n2 must NOT be negative nubmers
    
    is_proper_divisor (5 ,10)
    True
    
    is_proper_divisor (1 ,10)
    True

    is_proper_divisor (0 ,10)
    False

    is_proper_divisor (0 ,0)
    True

    '''
    
    if n1 == 0 and n2 == 0:
        return True
   
    elif n1 == 0 or n2 == 0:
        return False
    
    else: 
       # print (n2 // n1) 
        return n2 % n1 == 0
        
  
    
def sum_of_proper_divisors(n : int) -> int:
    '''this function returns the sum of all the proper divisors of that number
    as well as itself.
    
    >>> sum_of_proper_divisors( 100)
    117
    
    >>> sum_of_proper_divisors( 1)
    0
    >>> sum_of_proper_divisors( 5)
    1
    >>> sum_of_proper_divisors( 10)
    8
    

    '''
    i = 0
    summation = 0
    
    for i in range(n+1, 1, -1):
        if n % i == 0:
            factor = n // i
            summation = summation + factor
           
    return summation


def get_abundance(n):
    ''' this function takes a non-negative integer 'n' and returns the abundance
    of the number. When the number passed is not an abundant number the function
    returns 0.
    An abundant number defined to be a number which is smaller than the sum
    of its proper divisors. The amount of magnitude the sum exceeds the number 
    is the abundance.
    
    >>> get_abundance (11)
    0
    
    >>> get_abundance (945)
    30
    
    >>> get_abundance (100)
    17
    
    '''
    
    if sum_of_proper_divisors(n) > n:
        
        return sum_of_proper_divisors(n) - n
    
    else:
        return 0
    
    
def get_multiples(begin: int, counter: int, finish:int) ->str:
    ''' This function returns a string containing a sequence of multiples.
    It takes 3 arguments which represent:the starting number for the multiples,
    the number by which to perform multiplication and the amount of times the 
    multiplication should be performed.
    
    >>> get_multiples(8,3,7)
    '8 11 14 17 20 23 26'
    
    >>> get_multiples(0, 1, 3)
    '0 1 2'

    >>> get_multiples(4, 2, 8)
    '4 6 8 10 12 14 16 18'
    

    '''
    
    ml = [0,1]
    i= begin
    string = str(begin)
    
    for i in range (1, finish):
        
        multiples= begin + (counter* i)
        ml.append (multiples)
                
        string = string + ' ' + str(multiples) 
        
    return string
    
               
        
def print_multiplication_table(h_start: int, width: int, v_start: int, height: int):
    '''
    this function prints a multplication table given a horizontal axis start,
    a width of the table, a vertical axis start and a vertical height. 
    It utilizes the previous get_multiples function as a helper
    
    >>> print_multiplication_table(0, 3, 4, 10)
          0    1    2    
    4     0    4    8
    5     0    5   10
    6     0    6   12
    7     0    7   14
    8     0    8   16
    9     0    9   18
   10     0   10   20
   11     0   11   22
   12     0   12   24
   13     0   13   26
   
   >>> print_multiplication_table(1, 5, 2, 10)
          1    2    3    4    5    
    2     2    4    6    8   10
    3     3    6    9   12   15
    4     4    8   12   16   20
    5     5   10   15   20   25
    6     6   12   18   24   30
    7     7   14   21   28   35
    8     8   16   24   32   40
    9     9   18   27   36   45
   10    10   20   30   40   50
   11    11   22   33   44   55 
   
    '''
    print('          ', end = '')
    
    type(get_multiples(h_start, 1, width))
    
    multiples = get_multiples(h_start, 1, width).split()
     
    for j in range (width):
        print(f'{multiples[j]:4s}' , end = ' ') 
    
    print()
         
    for y_axis in range( height): 
        
        print(format(y_axis + v_start, '5d'), end= ' ')
    
        for x_axis in range(width):
                           
            print_mult= (x_axis + h_start) * (y_axis + v_start)
            
            print (format(print_mult, '5d'), sep=' ', end ='')
                
        print ()    