# Phil Kirker UVIC CSC 110 Sept 27 2021
#Assignment 3
import doctest

def get_smallest(num1: int, num2:int, num3: int) ->int:
    '''This function will taking in 3 arguments as integers and return the
    number with the lowest value
    
    >>> get_smallest(3 ,5 ,-2)
    -2
    
    >>> get_smallest(3, 5, 3)
    3
        
    '''

    if num1 == num2 and num1 < num3:
        return num1
    
    elif num2 == num3 and num2 < num1:
        return num2
    
    elif num3 == num1 and num3 < num2:
        return num3
    
    elif num1 < num2 and num1 < num3:
        return num1
    
    elif num2 < num1 and num2 < num3:
        return num2
    
    elif num3 < num1 and num3 < num2:
        return num3
    
    elif num1 == num2 and num2 == num3:
        return num1, 
    
    else :
        return 'error'
    
    
    
# find the best way to return values if some are the same
# which will it be? the last occuring num?
    
    
    
def get_time_in_seconds(days: int, hours: int, minutes: int, seconds: int) -> int :
    ''' this function prints the total number of seconds given 4 arguments in
    the format of days, hours, minutes, seconds all as integers
    
    >>> get_time_in_seconds(1, 1, 1, 1)
    90061
    
    >>> get_time_in_seconds(5, 4, 3, 2)
    446582
    
    The function assumes that all argument values are whole numbers
    (non-negative, no floating 
    point portion).
    '''
    #since we are assuming we could likely leave this whole function as a 
    #return statement ?
    
    tot_seconds = 0
    
    tot_seconds += days * 86400
    
    tot_seconds += hours * 3600
    
    tot_seconds += minutes * 60
    
    tot_seconds += seconds 
        
    return tot_seconds
        


def get_average_speed(distance: int, days: int, hours: int, minutes: int,
    seconds: int) -> float: 
    '''This function calcluates and determines the average speed of a vehicle
    moving over a given distance and period of time. Using the
    get_time_in_seconds function it will determine speed in m/s
    
    Precondition: ALL arguments are whole numbers, not floats, not negatives,
    and at least one value must be greater than 0. 
    >>> 
    
    '''
    time = get_time_in_seconds(days, hours, minutes, seconds)
    #print (time) 
    
    avg_vel = ( distance * 1000) / time
    
    return avg_vel

    


def get_box_charge(boxes: int, cost: float) -> float: 
    '''This function calculates the cost per box of ordered contact lenses.
    It takes in 2 arguments the number of boxes to be purchased as an integer
    and the cost per box as a float.
    The function discounts purchasing after 10 boxes and 20 boxes 10 and 20%
    respectively. 
    
    Precondition: the function assumes that the order is being performed with
    atleat 1 box and at a cost greater than 0
     
     >>> get_box_charge (15, 12.5)
     168.75
     >>> get_box_charge (25, 12.5)
     250.0
    '''
    base_price = boxes * cost
    
    if 20 > boxes >= 10:
        total = base_price - ((base_price) * 0.1)
        return total
    
    elif boxes >= 20:
        total = base_price - ((base_price) * 0.2)
        return total
    
    else: 
        total = boxes * cost
        return total


def get_order_charge(cust_new: bool, presc1_boxes: int, presc1_cost:float, 
    presc2_boxes:int, presc2_cost: float)-> float:
    '''calculates the charge on an order of contact lenses for up to 2 different
    prescriptions ordered. The function takes 5 arguments: determine if the order 
    is from a returning customer(bool), the number of boxes from the 1st prescription
    (int), price of the 1st perscription (float), the number of boxes from the 2nd 
    prescription (int), and the cost of the 2nd prescription (float).
    The function will call the get_box_charge to determine the price at the
    correct intervals. 
    If the customer is new there will be an additional 10% deduction from the
    total price.
    Taxes will also be applied to the cost of the order. As well an additional
    shipping charge will be added after tax. BUT there will be no shipping costs
    if the order is over 100 dollars.
    
    Precondition: The number of boxes ordered is NOT negative, and the price 
    per box is greater than 0
    
    
    '''
    cost_presc1 = get_box_charge (presc1_boxes, presc1_cost)
    #print('cost of presc 1:' , cost_presc1) # test    
    
    cost_presc2 = get_box_charge (presc2_boxes, presc2_cost)
    #print('cost of presc 2:' , cost_presc2) #test
    
    both_cost = cost_presc1 + cost_presc2 
    #print('cart total:', both_cost)
    
    
    if cust_new == True:
        new_cust_discount = both_cost - (both_cost *0.1)
        #print('new customer discount:', new_cust_discount) # test 
        new_w_taxes = new_cust_discount + (new_cust_discount * 0.12)
        #print('new customer discount w/ taxes', new_w_taxes) #test 
                
        if new_w_taxes >= 100:      # don't apply shipping charge
            #print('NEW CUST: NO shipping added, final cost:', new_w_taxes)
            
            return new_w_taxes                       #END 
        
        else:
            new_total_w_shipping = new_w_taxes + 4.50  # apply shipping charge
            #print ('NEW CUST: shipping added final cost:', new_total_w_shipping)
            
            return new_total_w_shipping                  #END
        
            
    else:
        old_cust = both_cost
        #print('old customer:', old_cust)
        
        w_taxes = old_cust + (old_cust * 0.12)
        #print('cost with taxes:', w_taxes)
        
        if w_taxes >= 100:
            #print('old cust: NO shipping added, final cost:', w_taxes)
            
            return w_taxes                     #END
        
        else:
            
            old_total_w_shipping = w_taxes + 4.50 
            
            #print('old cust: shipping ADDED, final cost:', old_total_w_shipping)
            
            return old_total_w_shipping          #END
        
               
        

def place_order(credit: float, cust_new: bool, presc1_boxes: int, presc1_cost:float, 
    presc2_boxes:int, presc2_cost: float) -> bool:
    '''This function determines whether or not there is enough credit to make a
    purchase within the bounds of this assignent / or gourp of functions.
    This function itself takes in 6 arguments reperesenting the following in 
    sequential order: new or old customer(bool), number of boxes for 
    prescription 1(int), price per box of perscription 1 (float), number of 
    boxes for prescription 2 (int), cost of prescription 2 (float), and 
    the amount of credit within the account making the purchase.
    
    Precondition(s): the function assumes that the account balance and number of boxes
    is not negative, as well, the price of boxes must be greater than 0
    >>> place_order( 40.5, False, 1, 12.5, 2, 9.5)
    True
    
    >>> place_order(32.75, False, 1, 12.5, 2, 9.5)
    False
    '''
    total_cost = get_order_charge(cust_new, presc1_boxes, presc1_cost, 
    presc2_boxes, presc2_cost)
    
    return credit >= total_cost
    


def get_middle(string: str) ->str:
    '''This function takes a string and 'slices' the middle character(s) of 
    the inputed string. If the string length is odd it will print the center most
    character if it is even, it will print the 2 centermost characters in the string.
    If the string is empty, it will return the empty string.
       
    '''    
    
    
    if len(string) % 2 ==0:
        
        return string[len(string) //2 -1] + string[len(string)//2]
        
        
    else: 
        
        return string[len(string)//2]