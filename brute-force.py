import itertools
import string
import time
import random

all = string.ascii_letters + string.digits + string.punctuation

def guess_password(real):
    start_time = time.perf_counter()
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            #time.sleep(.01)	
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                final_time = time.perf_counter()
                time_spent = final_time - start_time
                return f'HTTP REQUEST ACCEPTED [200]! Password is {guess}. Found in {attempts} guesses and {time_spent:0.4f} seconds.'
            print(guess, attempts)

#Generates a 4 char length password.
length = 16
sample = random.sample(all, length)
sample = ''.join(sample)
print(sample)
time.sleep(10)

#Start trying the passwords.
print(guess_password(sample))
