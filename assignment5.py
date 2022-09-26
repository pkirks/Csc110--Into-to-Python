# Phil Kirker CSC110 Fall 2021
# Assignment 5

import doctest
import random

MIN_DIE = 1
MAX_DIE = 6

def roll_one_die() -> int:
    """ 
    simulates the roll of a single dice between MIN_DIE and MAX_DIE inclusive 
    and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    #generates a random number between MIN_DIE and MAX_DIE inclusive
    
    die = random.randint(MIN_DIE, MAX_DIE)
    
    #for testing to allow you to enter the dice roll you want at the keyboard
    #comment out the line above and uncomment this line:
    #die = int(input('enter a simulated dice roll\n'))
    
    return die 



def get_sum_of_digits(n: int) -> int:
    '''
    This function takes an integer n and returns the sum of each digit of the 
    integer
    
    >>> get_sum_of_digits(0)
    0

    >>> get_sum_of_digits(432)
    9
    '''
    
    my_list= []
    n = abs(n)
    
    while n != 0:
        new_list = n%10
        n=n//10
        
        my_list.append(new_list)
  
    
    return sum(my_list)
    

def is_harshad_number (n: int) -> bool:
    '''this function takes an integer n and returns a boolean expression to determine
    if it is an harshhard number or not
    
    >>> is_harshad_number(432)
    True
    
    >>> is_harshad_number(11)
    False
    
    '''
    
    summation = get_sum_of_digits(n)
    
    if n % summation == 0:
        return True
    
    else: 
        return False
    
def get_first_n_harshad_numbers (n: int) -> str:
    '''this function takes an int n which returns the first n amount of harshad 
    numbers in a string
    
    >>> get_first_n_harshad_numbers(0)
    ''
    
    >>> get_first_n_harshad_numbers(1)
    '1'
    
    >>> get_first_n_harshad_numbers(20)
    '1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42'

    
    '''
    
    numbers = ''
    count = 0
    i = 1
    
    while count != n:
    
        if is_harshad_number(i) == True:
            
            numbers += str(i)
            numbers += ','
            
            count += 1
        i +=1
        
    numbers = numbers[:len(numbers)-1]
        
    return numbers

            
            
            
def play(guess1: int, guess2: int, bet: int) ->int:
    ''' this function simulates playing a game with dice which takes 2 guesses as 
    arguments and one bet. It then calls a roll dice function which randomly generates
    a value between 1 and 6 inclusively for 2 die. If the player correctly guesses 
    all the dice, they triple their bet. If they guess none of them, they lose.
    If they guess 1 right, they get a 'second chance'. On the second chance they
    will re-roll the dice as many times as necessary to either successfully roll
    one of their guesses and win or fail if the sum of their re-rolls matches the
    sum of the 'losing target'. Losing target being the sum of the original 2 rolls
    
    >>> play(1,1,20)
    your guesses are:[1, 1] and you bet: $20
    you rolled:[6, 2]
    bad guesses, you lose
    0
    
    >>> play(1,3,20)
    your guesses are:[1, 3] and you bet: $20
    you rolled:[2, 6]
    bad guesses, you lose
    0
    
    >>> play(5,3,20)
    your guesses are:[5, 3] and you bet: $20
    you rolled:[6, 5]
    One guess was right! Re-rolling for a second chance...
    Do not roll 11 or you will lose!
    your re-rolls are:[1, 5]
    the sum of your re-roll is: 6
    re-rolling again... 

    your re-rolls are:[1, 2]
    the sum of your re-roll is: 3
    re-rolling again... 

    your re-rolls are:[1, 5]
    the sum of your re-roll is: 6
    re-rolling again... 

    your re-rolls are:[3, 2]
    the sum of your re-roll is: 5
    you guessed right! you doubled your money!
    40
    '''
    
    count=0
    good_guess_i = 0
    left_over_guess = 0
    
    dieRolls=[roll_one_die(),roll_one_die()]
    guesses=[guess1,guess2]
    
    print(f'your guesses are:{guesses} and you bet: ${bet}')
    print(f'you rolled:{dieRolls}')
    
    for i in range (0,2):
        for j in range (0,2):

            if dieRolls[i]==guesses[j]:
                count+=1
                good_guess_i = j
                
                break
            
    left_over_guess=guesses[good_guess_i -1]
    
    if count == 0:
        print('bad guesses, you lose')
        return 0 # lose
    
    elif count == 2:
        print('both guesses were right! you tripped your money')
        return bet*3 # huge win
    
    else:
        print('One guess was right! Re-rolling for a second chance...')
        loseNum=sum(dieRolls)
        print('Do not roll',loseNum,'or you will lose!')
        
        m=0
        while m==0:
            dieReRolls=[roll_one_die(),roll_one_die()]
            print(f'your re-rolls are:{dieReRolls}')
            print(f'the sum of your re-roll is: {sum(dieReRolls)}')
                        
            if sum(dieReRolls) == loseNum:
                print('your re-roll sum matches the losing target, you lose')
                return 0  # lose 
            
            else: 
                for n in range(len(dieReRolls)):
                    if dieReRolls[n] == left_over_guess:
                        print('you guessed right! you doubled your money!')
                        return bet*2  # win on 'second chance'
            
            print('re-rolling again... \n')