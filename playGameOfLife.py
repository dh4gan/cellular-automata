import GameOfLife as game
import matplotlib.pyplot as plt

N=10

cell= game(N)


fig1 = plt.figure()
ax = fig1.add_subplot(111)
hist = ax.hist2D(game.grid, bins = game.N)

