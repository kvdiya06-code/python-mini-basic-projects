#password generator replica
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['!','@','#','$','%','^','&','*']
letter_needed=int(input("How many letter do u want? "))
numbers_needed=int(input("How many numbers do u want? "))
symbols_needed=int(input("How many symbols do u want? "))
letter_needed_1=[]
#number_needed_1=[]
#symbols_needed_1=[]
for i in range(letter_needed):
    n=len(letter)-1
    letter_index=random.randint(1,n)
    letter_needed_1.append(letter[letter_index])
for i in range(numbers_needed):    
    numbers_index=random.randint(1,(len(numbers)-1))
    letter_needed_1.append(numbers[numbers_index])
for i in range(symbols_needed):  
    symbols_index=random.randint(1,(len(symbols)-1))
    letter_needed_1.append(symbols[symbols_index])
for i in range(len(letter_needed_1)):
    etter_index=random.randint(1,(len(letter_needed_1)-1))
    #v=
    print(letter_needed_1[etter_index],end="")