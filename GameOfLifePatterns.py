# Written 7/7/14 by dh4gan

# supplies patterns to be added to a cellular automaton obeying
# Conway's Game of Life Rules

from CellularAutomata import CellularAutomata2D



def add_block(cell, icentre,jcentre):
    
    extent = 7
    
    cell.clear(icentre,jcentre,extent)
    
    cell.grid[icentre,jcentre] = 1
    cell.grid[icentre,jcentre+1] = 1
    cell.grid[icentre+1,jcentre] = 1
    cell.grid[icentre+1,jcentre+1] = 1

def add_beehive(cell, icentre,jcentre):
    
    extent = 7
    cell.clear(icentre,jcentre,extent)
    
    cell.grid[icentre-1,jcentre] = 1
    cell.grid[icentre+1,jcentre] = 1
    
    cell.grid[icentre+1,jcentre+1] = 1
    cell.grid[icentre-1,jcentre+1] = 1
    
    cell.grid[icentre,jcentre-1] = 1
    cell.grid[icentre,jcentre+2] = 1
    
def add_blinker(cell,icentre,jcentre):
        
    extent = 4
    cell.clear(icentre,jcentre,extent)
    cell.grid[icentre,jcentre-1:jcentre+2] = 1
    
def add_toad(cell,icentre,jcentre):
    extent = 3
    cell.clear(icentre,jcentre,extent)
    
    cell.grid[icentre-1:icentre+2, jcentre]=1
    cell.grid[icentre:icentre+3, jcentre-1]=1