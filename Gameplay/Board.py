'''
Created on Jul 21, 2011

@author: Bonual
'''

class Board(object):
    '''
    The board stores all active pieces and spaces.
    
    It controls all information about the spatial
    orientation of Spaces and Pieces, the movement 
    costs based on space characteristic and other 
    spatial information.
    '''


    def __init__(self):
        _map = []
        _pieces = []
        
    def GetSpace(self,xPosition,yPosition):
        invertedY = len(self._map) - yPosition - 1
        return self._map [invertedY][xPosition]
    
    def GetPiece(self,xPosition,yPosition):
        invertedY = len(self._pieces) - yPosition - 1
        #Do something special if there's no piece?
        return self._pieces [invertedY][xPosition]
        
    def LoadMap (self, mapStringMatrix):
        """ """
        #Takes a matrix of strings and sets up the map by filling the
        #_map with Spaces, and loading the space characteristics with the
        #Space class LoadMapString method. Set the _pieces matrix to the
        #size of the _map matrix
        pass
        
    def CalcMoveCost(self, fromLoc, toLoc):
        """ """
        #Use specific movement costs to return the number of movement points
        #required to move from one space to another. Intention - piece movement
        #ranged attack calcs, any other cost driven, movement related calc.
        
        pass 
    
    ##################---Private methods---##################

    
    def __testBoard(self):
        #Check that every point on the map always has a space
        #Check null and bad map string matrices
        #Check null and bad piece string matrices
        pass