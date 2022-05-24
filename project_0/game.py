# Guess the number

import numpy as np

number = np.random.randint(1,101)
count = 0

while True:
    count+=1
    predict_number = int(input('Enter the number: '))
    
    if  predict_number > number:
        print("Number should be less")
    elif predict_number < number:
        print("Number should be bigger")
    else:
        print(f"You're right, number is {number}, you used {count} attempts")
        break