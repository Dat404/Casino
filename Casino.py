import random


def win(n):
    return f'You win {n} times!' if n>0 else 'Full Loose!'

Lotery_Numbers=[random.randint(1,20) for elm in range(0,5)]
User_Answer=[]
Count=0


print('Input 5 numbers: ')
while True:
    Count+=1
    num=int(input(f'{Count} number:/> '))
    User_Answer.append(num)
    if len(User_Answer)==5:
        Count=0
        break

for elm in Lotery_Numbers:
    if elm in User_Answer:
        Count+=1

print(win(Count)) 