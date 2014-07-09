# Written 7/7/14 by dh4gan

# supplies patterns to be added to a cellular automaton obeying
# Conway's Game of Life Rules

from CellularAutomata import CellularAutomata2D



def add_block(cell, icentre,jcentre):
    '''
    Adds a 2x2 block into the system, with bottom left corner (icentre, jcentre)
    '''
        
    extent = 2    
    cell.clear(icentre,jcentre,extent)    
    cell.grid[icentre:icentre+2,jcentre:jcentre+2] = 1
    

def add_beehive(cell, icentre,jcentre):
    '''
    Adds a beehive into the system, with (icentre,jcentre) being the inner left blank square
    '''
    
    extent = 7
    cell.clear(icentre,jcentre,extent)
    
    cell.grid[icentre-1,jcentre:jcentre+2] = 1
    cell.grid[icentre+1,jcentre:jcentre+2] = 1
            
    cell.grid[icentre,jcentre-1] = 1
    cell.grid[icentre,jcentre+2] = 1
    
def add_blinker(cell,icentre,jcentre):
    '''
    Adds a vertical line of 3 blocks (period 1)
    '''
        
    extent = 4
    cell.clear(icentre,jcentre,extent)
    cell.grid[icentre,jcentre-1:jcentre+2] = 1
    
def add_loaf(cell,icentre, jcentre):
    '''
    Adds a loaf, with (icentre,jcentre) in the bottom left corner (blank)
    '''
    
    cell.grid[icentre,jcentre+1:jcentre+3] = 1
    cell.grid[icentre+1:icentre+3,jcentre+3] = 1
    cell.grid[icentre+1,jcentre] = 1
    cell.grid[icentre+2,jcentre+1] = 1
    cell.grid[icentre+3,jcentre+2] = 1
    
def add_boat(cell,icentre, jcentre):
    '''
    '''
    extent = 4
    cell.clear(icentre,jcentre,extent)
    
    indices = cell.getVonNeumannNeighbourhood(icentre,jcentre)
    print indices
    for element in indices:
        cell.grid[element[0],element[1]] = 1
        
    cell.grid[icentre+1,jcentre-1] = 1
    
def add_toad(cell,icentre,jcentre):
    extent = 3
    cell.clear(icentre,jcentre,extent)
    
    cell.grid[icentre-1:icentre+2, jcentre]=1
    cell.grid[icentre:icentre+3, jcentre-1]=1
        

def add_beacon(cell,icentre,jcentre):
    '''
    Adds two 2x2 blocks, which repeat a pattern of period 2
    '''
    
    extent = 3
    cell.clear(icentre,jcentre,extent)
    
    add_block(cell,icentre+2,jcentre)
    add_block(cell,icentre,jcentre+2)
    
    
def add_pulsar(cell,icentre,jcentre):
    
    extent = 8
    cell.clear(icentre,jcentre,extent)

    # Start with inner cross
    
    # North
    cell.grid[icentre+2:icentre+5,jcentre+1] = 1
    cell.grid[icentre+2:icentre+5,jcentre-1] = 1
    
    # South
    cell.grid[icentre-4:icentre-1,jcentre+1] = 1
    cell.grid[icentre-4:icentre-1,jcentre-1] = 1
    
    # East
    cell.grid[icentre+1,jcentre+2:jcentre+5] = 1
    cell.grid[icentre-1,jcentre+2:jcentre+5] = 1
    
    # West
    cell.grid[icentre+1,jcentre-4:jcentre-1] = 1
    cell.grid[icentre-1,jcentre-4:jcentre-1] = 1
    
    
    # Now do surrounding bars - quadrant at a time
    
    cell.grid[icentre+6,jcentre+2:jcentre+5] = 1
    cell.grid[icentre+2:icentre+5, jcentre+6] = 1
    
    cell.grid[icentre-4:icentre-1, jcentre+6] = 1
    cell.grid[icentre-6, jcentre+2:jcentre+5] = 1
    
    cell.grid[icentre-6, jcentre-4:jcentre-1] = 1
    cell.grid[icentre-4:icentre-1, jcentre-6] = 1
    
    cell.grid[icentre+2: icentre+5, jcentre-6] = 1
    cell.grid[icentre+6, jcentre-4:jcentre-1] = 1
    