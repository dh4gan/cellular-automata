import numpy as np

class CellularAutomata2D(object):    
    '''
    Object that calculates and displays behaviour of 2D cellular automata
    '''
        
    def __init__(self, ni):
        '''
        Constructor reads:
        N = side of grid
        
        produces N x N blank grid
        '''
        
        self.N = ni
        self.Ntot = self.N*self.N        
        self.grid = np.zeros((self.N,self.N))        
        self.nextgrid = np.zeros((self.N,self.N))
        
        
    def getMooreNeighbourhood(self, i,j):
        '''
        Returns a set of indices corresponding to the Moore Neighbourhood
        (These are the cells immediately adjacent to (i,j), plus those diagonally adjacent)
        '''
        
        indices = []
        
        for iadd in range(i-1,i+2):
            for jadd in range(j-1, j+2):        
                if(iadd==i and jadd == j): continue
                
                if(iadd>self.N-1): iadd = iadd - self.N
                if(jadd>self.N-1): jadd = jadd - self.N
                
                indices.append([iadd,jadd])
        
        return indices
    
    def getVonNeumannNeighbourhood(self,i,j):
        '''
        Returns a set of indices corresponding to the Von Neumann Neighbourhood
        (These are the cells immediately adjacent to (i,j), but not diagonally adjacent)
        '''
        
        indices = []
        
        for iadd in range(i-1,i+2):
            if(iadd==i): continue
            if(iadd>self.N-1): iadd = iadd - self.N        
                
            indices.append([iadd,j])
            
        for jadd in range(j-1,j+2):
            if(jadd==j): continue
            if(jadd>self.N-1): jadd = jadd - self.N
            
            indices.append([i,jadd])
            
        return indices    
    
    def randomise(self):
        '''
        Places a random selection of zeros and ones into grid
        '''
        
        for i in range(self.N):
            for j in range(self.N):
                self.grid[i,j] = np.rint(np.random.random())
                
    def clear(self, icentre, jcentre, extent):
        '''
        Clears a space on the grid
        '''
        
        for i in range(icentre-extent, icentre+extent):
            for j in range(jcentre-extent, jcentre+extent):
                if(i>0 and i<self.N and j>0 and j<self.N):
                    self.grid[i,j] = 0
    
    def updateGrid(self):
        '''
        Takes the changes queued up on self.nextgrid, and applies them to self.grid
        '''
        
        self.grid = np.copy(self.nextgrid)
        self.nextgrid = np.zeros((self.N,self.N))
        
                        
    def ApplyGameOfLifeRule(self):
        '''
        Constructs the self.nextgrid matrix based on the properties of self.grid
        Applies the Game of Life Rules:
        
        1. Alive cells with 2 or 3 neighbours survive
        2. Dead cells with exactly 3 neighbours come alive
        3. Cells which do not satisfy 1 or 2 become or remain dead
        '''
        
        for i in range(self.N):
            for j in range(self.N):
                indices = self.getMooreNeighbourhood(i,j)
                counter = 0
                
                # Count number of alive neighbours
                                
                for element in indices:                    
                    
                    if(self.grid[element[0],element[1]] == 1):
                        counter +=1
                
                
                # Rules for live cells
                # if neighbour number either 2 or 3, it lives
                # any other number, it dies
                if(self.grid[i,j]==1):
                    if(counter<2 or counter>3):
                        self.nextgrid[i,j]=0
                    else:
                        self.nextgrid[i,j]=1
                
                # Rules for dead cells
                # If neighbour number exactly 3, it becomes alive
                if(self.grid[i,j]==0):
                    if(counter==3):
                        self.nextgrid[i,j]=1                                                                      
            
        