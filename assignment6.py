# Phil Kirker CSC 110 UVIC Fall 2021
# Assignment 6

def multiply_by (loi: list[int],  mult:int) -> list:
    '''this function takes a list and an aditional int as a multiplier, it creates
    a new list and multiplies every value in the orignal list by the multiplier,
    it then returns the new list with the multiplied numbers.
    
    >>> multiply_by( [1,2,3,4], 1)
    [1, 2, 3, 4]
    
    >>> multiply_by( [1,2,3,4], 0)
    [0, 0, 0, 0]
    
    >>> multiply_by( [1,2,3,4], -1)
    [-1, -2, -3, -4]
    
    >>> multiply_by( [0,1,2,3], 2)
    [0, 2, 4, 6]
    
    '''
    
    newlist = []
    
    for i in range(len(loi)):
                
        newlist.append(loi[i]*mult)
    
    return newlist


def remove_multiples (loi:list[int], dev:int)-> list:
    '''
    this function takes a list of ints and an divisor int and returns a new list
    made up of numbers that were not divisible by the divisor
    
    >>> remove_multiples ([2,4,6], 2)
    []
    
    >>> remove_multiples ([2, 4, 6], -2)
    []
    
    >>> remove_multiples ([0,2,4,6], 2)
    []
    
    >>> remove_multiples([0,1,2,3,4,5,6], 2)
    [1, 3, 5]
        
    '''
    
    newlist = []
    
    if dev == 0: 
        newlist = loi
        return newlist
    
    for i in range(len(loi)):
                
        if is_multiple_of(loi[i] , dev) != True:
            newlist.append(loi[i])
    
    return newlist
        
        
'''  orignally made this without the helper func
starting on line 53

        if loi[i] == 0:
            newlist.append(loi[i])
        
        elif loi[i] % dev !=0:
                     
            newlist.append(loi[i])
            
        elif loi[i] < 0 and abs(loi[i]) % dev !=0:
            
            newlist.append(loi[i])
            
    return newlist
        '''                
            
def remove_ends_with (loi:list[ str ],  strang: str) -> list:
    '''This function takes a list of strings and a string argument. The function
    creates a new list and returns only the elements from the original list which
    DO NOT have the 'strang' in them.
    
    >>> remove_ends_with (['bat', 'ratchet', 'BCAT', 'at', 'atlas'], 'at')
    ['ratchet', 'atlas']
        
    '''
    newlist = []
    length = len(strang)
      
    for i in loi:
        
        if strang.lower() in i[:-len(strang)] or strang.upper() in i[:-len(strang)]:
                
            newlist.append(i)
            
    return newlist

'''    
def my_func(list_words, ending): # found this online. works, but it case sensitive
    return [word 
            for word in list_words 
            if word[len(word)-len(ending):] != ending ]            

'''
            
def get_index_of_largest (loi: list[int]) -> int:
    ''' this function takes a list of ints and returns the index of the largest
    value from the list. If the largest number appears twice, it will return the
    index of the last occurence.
    
    >>> get_index_of_largest([1,2,3,4,5,5])
    5
    
    >>> get_index_of_largest([-1, 0, 5])
    2
    
    >>> get_index_of_largest([5, 0, 5])
    2
    
    >>> get_index_of_largest([-1, -2, -3])
    0
    '''
    
    maximum = loi[0]
    max_index = 0
    
    for i in range(len(loi)):
        
        if loi[i] >= maximum:
            max_index = i
            maximum = loi[i]
                        
    return max_index



def does_contain_proper_divisor (loi:list[int], num:int) -> bool:
    ''' This function takes a list of integers and an additional int and determines
    whether the given list contains any values that are proper divisors of the 
    additional int. It uses a helper function called is_proper_divisor which 
    differentiates whether the number is a divisor, but this function iterates over
    each integer within the list.
    
    >>> does_contain_proper_divisor( [12,5,3,1], 2)
    True
    
    >>> does_contain_proper_divisor( [12,5,3,1], 0)
    False
    
    >>> does_contain_proper_divisor( [12,5,3,0], 0)
    True
    
    >>> does_contain_proper_divisor( [-25,2,1], 5)
    True
    '''
     
    count = 0
     
    for i in range(len(loi)):
        
        if is_proper_divisor(loi[i], num):
            count+=1
            
    if count > 0:
        return True
    
    else: 
        return False
            

def are_all_less_than_threshold( loi:list[int], threshold:int) -> bool:
    ''' This function takes a list of ints and a threshold int, and determines
    if the given list ONLY has values that are below the threshold. 
    
    >>> are_all_less_than_threshold( [1,2,3,4,6], 6)
    False

    >>> are_all_less_than_threshold( [1,2,3,4,5], 6)
    True
    
    >>> are_all_less_than_threshold( [1,2,3,4,5], 0)
    False
    
    >>> are_all_less_than_threshold( [-1,-2,-3], 0)
    True
   
    '''
    for i in range (len(loi)):
        if loi[i] >= threshold:
            return False
        
    return True # kinda jank 

    # --------------------HELPER FUNCTIONS HERE!!---------------------------#
    #-----------------------------------------------------------------------#

def is_multiple_of(n1: int, n2: int):
    ''' this function will determine if n1 is a multiple of n2 and will
    print a statement of affirmation or refutation
    >>> is_multiple_of(12, 4)
    True
    
    >>> is_multiple_of(0, 3)
    True
    
    >>> is_multiple_of(5, 3)
    False
    
    >>> is_multiple_of (5, 0)
    False
        
    '''
    if n2 == 0 and n1 == 0:
        return True 
    
    elif n2 ==0:
        return False

    elif n1 % n2 == 0:
        return True    
    
    else:
        return False 

            
def is_proper_divisor(n1 :int, n2: int)->bool:
    '''this function determines if n1 is proper divisor of n2.
    
    Precondition: n1 and n2 must NOT be negative nubmers
    
    is_proper_divisor (5 ,10)
    True
    
    is_proper_divisor (0, 10)
    True

    is_proper_divisor (0 ,0)
    True
    
    is_proper_divisor (5, 0)
    True

    '''
    
    if n1 == 0 and n2 == 0:  
        return True
    
    elif n1 == 0 and n2 > 0:
        return True
        
    elif n1 == 0 or n2 == 0:
        return False
    
    else: 
        return n2 % n1 == 0