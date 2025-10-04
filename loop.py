# fruits=["apple","grape","kiwi"]
# for i in fruits:
#     print(i)

scores=[12,55,78,35,3,65,48,24]
#SUM FUNCTION
# total=sum(scores)
# print(total)

# sum=0
# for i in scores:
#     sum+=i
# print(sum)
# print(max(scores))
# print(min(scores))
#MAX & MIN WITHOUT BUILT IN
# i=0
# for j in scores:
#     if j>i:
#         i=j
# print(i)
# i=12
# for j in scores:
#     if j<i:
#         i=j
# print(i)

#RANGE FUNCTION
#range(start,stop,step)
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)
import random
Letters=["A","B","C","D","E","F","G","H","I","J","K","L","a","b","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Symbols=["!","@","#","$","%","^","&","*","("]
Numbers=["1","2","3","4","5","6","7","8","9","0"]
print("Welcome to Password Generator")
no_letter=int(input("how many letters you want?"))
no_symbols=int(input("how many symbol you want?"))
no_numbers=int(input("how many numbers you want?"))
# password=""
# for i in range(0,no_letter):
#     random_letter=random.choice(Letters)
#     password+=random_letter
# for j in range(0,no_symbols):
#     random_symbol=random.choice(Symbols)
#     password+=random_symbol
# for k in range(0,no_numbers):
#     random_number=random.choice(Numbers)
#     password+=random_number
# print(password)
password=[]
for i in range(0,no_letter):
    random_letter=random.choice(Letters)
    password.append(random_letter)
for j in range(0,no_symbols):
    random_symbol=random.choice(Symbols)
    password.append(random_symbol)
for k in range(0,no_numbers):
    random_number=random.choice(Numbers)
    password.append(random_number)
print(password)
random.shuffle(password)
print(password)
p="" 
for i in password:
    p+=i
print(p)