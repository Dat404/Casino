import matplotlib.pyplot as plt


def stats(wins):
    f, ax = plt.subplots()
    ax.plot(wins, 'o-')
    ax.tick_params(labelcolor = 'r')
    ax.set_xlabel('Attempts', color = 'r')
    ax.set_ylabel('Num of guessed', color = 'r')
    ax.set(facecolor = 'black')
    f.set(facecolor = 'black')
    return plt.show()