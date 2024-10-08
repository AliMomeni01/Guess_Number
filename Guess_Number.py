import random
number = random.randint(1,10)
try:
    print('You have five chances')
    guess = int(input('Please enter a number between 1 and 10:' ))
# Error Handling    
except:
    print('Please enter a number')
attempts = 0
if number == guess:
    print('You won!')
# Loop for incorrect guesses    
while number != guess :
    attempts += 1
    print(f'You have guessed {attempts} times')
    if guess > number:
        print('The number is too high')
    else:
        print('The number is too low')
    # Check if max attempts (5) are reached    
    if attempts == 5:
        print('You have lost!')
        break
    try:
        guess = int(input('Please enter a number between 1 and 10:'))
    except:
        print('Please enter a number')
# Win condition after correct guess       
if number == guess:
    print('You won!')



