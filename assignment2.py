# Phil Kirker CSC 110 UVIC Fall 2021 Assignment2
# September 20 2021

import doctest

def add_to_cart(item_price: int, cart_total: int, available_credit: int):
    ''' this function takes 3 arguments, the price of the purchasing item
    the price of the items already being purchased and the total available 
    money for purchasing goods. The function will act to ensure purchasing
    of items stays under the available credit.
    >>> add_to_cart( 10, 20, 25)
    Not enough funds! You need an additional $ 5
    
    >>> add_to_cart( 10, 20, 50)
    cart balance $ 30
    '''
    
    if (item_price + cart_total) > available_credit:
        
        short = (item_price + cart_total) - available_credit 
        
        print('Not enough funds! You need an additional $', short)
    
    elif (item_price + cart_total) <= available_credit:
        
        cart_balance = item_price + cart_total
        
        print('cart balance $', cart_balance)


    
def print_smallest (num1: int, num2: int, num3: int):
    ''' this function will compare 3 integer arguments and print the smallest
    of the 3
    >>> print_smallest( 3, 5, 0)
    0
    >>> print_smallest( 3, 5, -3)
    -3
    '''
    if num1 < num2 and num1< num3:
        print(num1)
        
    elif num2 < num1 and num2 < num3:
        print (num2)
    
    else:
        print(num3)
    
    
def is_multiple_of(n1: int, n2: int):
    ''' this function will determine if n1 is a multiple of n2 and will
    print a statement of affirmation or refutation
    >>> is_multiple_of(12, 4)
    12 is a multiple of 4
    
    >>> is_multiple_of(0, 3)
    0 is a multiple of 3
    
    >>> is_multiple_of(5, 3)
    5 is not a multiple of 3
    '''
    if n2 == 0 or n1 == 0:
        print(f'{n1} is a multiple of {n2}')    

    elif n1 % n2 == 0:
        print(f'{n1} is a multiple of {n2}')
        #i believe there is an issue w even numbers?
        #as seen in lecture... look back
        
    else:
        print(f'{n1} is not a multiple of {n2}')
        
        
def print_triangle_type(angle1: int, angle2: int, angle3: int):
    ''' this function will determine the type of triangle given the 
    angles of each corner
    >>> print_triangle_type( 10, 90, 80)
    right
    >>> print_triangle_type( 110, 60, 10)
    obtuse
    >>> print_triangle_type( 89, 89, 2)
    acute
    '''
    
    if (angle1 + angle2 + angle3) == 180 and (angle1 > 0 and angle2 > 0 and angle3 > 0):
                                             
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print('right')
            
        elif angle1 >= 91 or angle2 >= 91 or angle3 >= 91 :
            print('obtuse')
            
        elif angle1 and angle2 and angle3 < 91: 
            print('acute')
          
    else:
        print('invalid triangle')
        
        
        
def print_time_in_seconds(days: int, hours: int, minutes: int, seconds: int):
    ''' this function prints the total number of seconds given 4 arguments in
    the format of days, hours, minutes, seconds
    
    >>> print_time_in_seconds(1, 1, 1, 1)
    total time: 90061
    
    >>> print_time_in_seconds(1, 1, 1, -1)
    invalid time

    '''
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        print('invalid time')
    
    else: 
        tot_seconds = 0
    
        tot_seconds += days * 86400
    
        tot_seconds += hours * 3600
    
        tot_seconds += minutes * 60
    
        tot_seconds += seconds 
    
        print('total time:', tot_seconds)
    