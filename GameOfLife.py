
from CellularAutomata import CellularAutomata
import numpy as np

class GameOfLife(CellularAutomata):
    
    
    def __init__(self, N):
        CellularAutomata.__init__(N)
        
        
    def get_Moore_Neighbourhoud(self, i,j):
        
        indices = CellularAutomata.get_Moore_Neighbourhood(i,j)
        
        return indices
    
    def get_von_Neumann_Neighbourhood(self,i,j):
        
        indices = CellularAutomata.get_Moore_Neighbourhood(i,j)
        
        return indices
    
    
    def ApplyRule(self,i,j):
        
        for i in range(self.N):
            for j in range(self.N):
                indices = self.get_Moore_Neighbourhood(i,j)
                counter = 0
                for element in indices:
                    if(self.grid[element[0],element[1]] == 1):
                        counter +=1
                
                if(counter<2 or counter >3):
                    self.nextgrid[i,j]=0
                else:
                    self.nextgrid[i,j]=1