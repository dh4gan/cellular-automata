
import numpy as np


class CellularAutomata(object):
    
    
    def __init__(self, N):
        self.nside = N
        self.ntot = N*N
        
        self.grid = np.zeros((N,N))
        
        self.nextgrid = np.zeros((N,N))
        
        
    def get_Moore_Neighbourhoud(self, i,j):
        
        indices = []
        
        for iadd in range(i-1,i+1):
            for jadd in range(j-1, j+1):        
                if(iadd==i and jadd == j): continue
                indices.append([i,j])
        
        return indices
    
    def get_von_Neumann_Neighbourhood(self,i,j):
        
        indices = []
        
        for iadd in range(i-1,i+1):
            if(iadd==i): continue
            
            indices.append([i,j])
            
        for jadd in range(j-1,j+1):
            if(jadd==j): continue
            
            indices.append([i,j])
            
        return indices    
    
    def updateGrid(self):
        
        self.grid = np.copy(self.nextgrid)
        self.nextgrid = np.zeros((self.N,self.N))
            
        