from CellularAutomata import CellularAutomata2D
import GameOfLifePatterns as game
import matplotlib.pyplot as plt
from time import sleep

N=50
nsteps = 100


# Create the cellular automaton, and give it an initially random distribution

cell= CellularAutomata2D(N)
cell.randomise()
#game.add_beehive(cell, 1, 1)
#game.add_block(cell, 1, 1)
#game.add_blinker(cell, 1,1)
#game.add_toad(cell, 2, 2)
#game.add_beacon(cell, 3, 3)

game.add_pulsar(cell, 25, 25)

# Set up interactive plotting

plt.ion()

fig1 = plt.figure()

istep= 0
while istep < nsteps:    

    # Draw the automaton
    ax = fig1.add_subplot(111)
    hist = ax.pcolor(cell.grid,edgecolors='black', cmap='binary')
    #hist = ax.pcolor(cell.nextgrid,edgecolors='black', cmap='binary')

    plt.draw()
    
    # Apply the Game of Life Rule, and update the grid
    cell.ApplyGameOfLifeRule()
    cell.updateGrid()
    
    # Clear axes for next drawing
    
    sleep(0.01)
    ax.clear()
    
    istep+=1

