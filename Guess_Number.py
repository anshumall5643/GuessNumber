import random
import math

n=int(input("Enter the second range :"))
num = random.randint(m,n)
chance=round(math.log(n-m+1, 2))
print("\n\tYou've only ",chance," chances to guess the integer!\n")
count=0
while count<chance:
     count=count+1
     guess =int(input('Guess a number:-'))
     if guess== num:
         print('Congratulations! you won the match in', count,'try')
         break     
     elif guess>num:
       print('You Guessed bigger number! ')
     elif guess<num:
         print('You Guessed smaller number!')
     if count>=chance:
         print('\n The number is:-',num)
         print('\nYou lose! & Better luck next time')'''





  
