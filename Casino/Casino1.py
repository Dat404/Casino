import random


wins = num = []

while True: 
    nums = [random.randint(0, 10) for x in range(0,5)]
    answ = list(map(int, input('Enter 5 numbers(0 to 10) or -1 for exit/> ').split()))
    if -1 in answ:
        break

    wins.append(sum(elm[0] == elm[1] for elm in zip(nums, answ)))
    print('U win(times) ', wins[-1])

q = input('Wanna see stats?(Y/N)> ')
if q.lower() in ('y', '1'):
    try:
        import matplotlib.pyplot as plt
        f, ax = plt.subplots()
        ax.plot([5 for x in range(0, len(wins))], 'g--', label = 'example')
        ax.plot(wins, 'o-', label = 'You')
        ax.tick_params(labelcolor = 'r')
        ax.set_xlabel('Attempts', color = 'r')
        ax.set_ylabel('Number of guessed (out of 5)', color = 'r')
        ax.set(facecolor = 'black')
        f.set(facecolor = 'black')
        ax.legend()
        plt.show()
    except: print('Try install matplotlib')