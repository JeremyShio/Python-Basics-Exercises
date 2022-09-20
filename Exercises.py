# ------- Week: 2 Day: 1 Homework -------




# ------- Exercise: 1 -------
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

def cubed_up_to_one_thousand():
    i = 0
    while i ** 3 <= 1000:
        print(i, i ** 3)
        i += 1

print('')
print('Numbers cubed up to one-thousand (1000)!')        
print(cubed_up_to_one_thousand())




# ------- Exercise: 2 -------
# Get first prime numbers up to 100

def prime_up_to_one_hundred(i):
    if (i == 1 or i == 0):
        return False
    
    for j in range(2, i):
        if (i % j == 0):
            return False
    
    return True

print('')
print('First prime numbers up to one-hundred (100)!')

for i in range (1, 100):
    if(prime_up_to_one_hundred(i)):
        print(i)
    
 
 
 
# ------- Exercise 3 -------
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors. Gracefully log the error if the user doesn't enter a number.

def ticket_age_checker(i):
    if (i <= 17):
        print(f'An age of {i} requires a kid ticket for admission!')
    elif (i in range(18, 65)):
        print(f'An age of {i} requires an adult ticket for admission!')
    else:
        print(f'An age of {i} requires a senior ticket for admission!')

print('')
print('Museum age checker for ticket admission pricing!')
i = 11
print(ticket_age_checker(i))
i = 47
print(ticket_age_checker(i))
i = 71
print(ticket_age_checker(i))