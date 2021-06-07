import random
import string
import itertools
import time

#ASCII TABLE
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
sum=0

#PASSWORD GENERATOR
def pwGen(length,all):
    
    
    temp = random.sample(all,length)
    
    password = "".join(temp)
    return password

#BRUTE-FORCE ATTACK
def bruteforce(length,pw,list):
    for x in itertools.product(list, repeat=int(length)): 
        bf= "".join(x)
        if bf == pw:
            print("\r Brute Force Attack: ".format(bf)+str(bf),end="")
            break;
        else:
            print("\r Brute Force Attack: ".format(bf)+str(bf),end="")

#MAIN PROGRAM    
print(' Brute Force Attack\n')
length = int(input(" Please enter the length of the password: "))
print('\n')

#LOOP 10 TIMES
counter=1
while counter<11:
    start = time.time()
    pw = pwGen(length,all)
    print('\n Sample ',counter,': ','\n Generated password:'+pw)
    bruteforce(length,pw,all)    
    end = time.time()
    diff = end  - start 
    sum=diff+sum
    diffstring = "Time used: {} s"
    print("\n",diffstring.format(diff),'\n')
    counter=counter+1

#AVERAGE TIME USED
print('The average time used is: ',sum/10,'s')

input()
