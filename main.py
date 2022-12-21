import random


wins = answ = []

while -1 not in answ: 
    answ = list(map(int, input('Enter 5 numbers(0 to 5), -2 for stats and exit or -1 for exit/> ').split()))    
    wins.append(sum(elm[0] is elm[1] for elm in zip(list(random.sample(range(5), 5)), answ)))
    
    print('U win(times) ', wins[-1])
    
    if -2 in answ:
        from graphc import stats
        stats(wins)
        break