'''
Created on Jul 21, 2011

@author: Bonual
'''
import re

#This function is used in the Space class definition
#it finds the next map string starting position in the
#list, otherwise (if the map string is the last in the list) it returns the map string length
def _calcMapStringRight(mapStringLeft, mapStringList, mapStringLength):
        '''Finds the next map string starting position in the list or returns the length of the map string'''
        SmallestLargerPosition=mapStringLength
        for mapStringPos in mapStringList:
            if mapStringPos>mapStringLeft:
                SmallestLargerPosition = min(SmallestLargerPosition,mapStringPos)
        return SmallestLargerPosition
            


class Space:
    '''
    The Space class represents a single space in a map/on a board.
    
    Includes all information about the definition and state of a space,
    but it does not include any information about location, pieces etc.
    '''
    
    #########---Static validation constants---##########
    #These constants are used to validate Space setup inputs
    #the terrain list is also distributed as the master to
    #validate movement cost data.
    _sListTerrain = frozenset(['R','M','P','F','S','W'])
    _iListOccupiable = frozenset([0,1])
    _iListAltitude = frozenset(range(0,31))
    
    ##########---Map string characteristics---##########
    #The map string is a code that stores Space characteristics.
    #The Space class can also create a Map string describing itself.
    _iMapStringLength = 5
    
    _iMapStringLeftTerrain = 0
    _iMapStringLeftAltitude = 2
    _iMapStringLeftOccupiable = 4
    
    _iMapStringPositionList = [_iMapStringLeftTerrain,
                           _iMapStringLeftAltitude,
                           _iMapStringLeftOccupiable]
    
    

    _iMapStringRightTerrain = _calcMapStringRight(_iMapStringLeftTerrain, 
                                                  _iMapStringPositionList, 
                                                  _iMapStringLength)
    
    _iMapStringRightAltitude = _calcMapStringRight(_iMapStringLeftAltitude, 
                                                   _iMapStringPositionList, 
                                                   _iMapStringLength)
    
    _iMapStringRightOccupiable = _calcMapStringRight(_iMapStringLeftOccupiable, 
                                                     _iMapStringPositionList, 
                                                     _iMapStringLength)
    ##################---Constructor---##################
    def __init__(self):
        ''' '''
        self._sTerrain = "P"
        self._iAltitude = 15
        self._bOccupiable = True

    ##################---Accessors---##################
    def setTerrain(self, newTerrain):
        ''' '''
        if newTerrain in self._sListTerrain:
            self._sTerrain = newTerrain
        else:
            print("I'm a setTerrain problem! Illegal entry: "+str(newTerrain)) #TODO add exception
    
    #Set the altitude of the space. Force the new altitude
    #to be in bounds. Consider adding exception instead.
    def setAltitude(self, newAltitude):
        ''' '''
        if newAltitude in self._iListAltitude:
            self._iAltitude = newAltitude
        else:
            print("I'm a setAltitude problem! Illegal entry: "+str(newAltitude)) #TODO add exception

    def setOccupiable(self, newOccupiable):
        ''' '''
        if newOccupiable in self._iListOccupiable: 
            self._bOccupiable = newOccupiable
        else:
            print("I'm a setOccupiable problem! Illegal entry: "+str(newOccupiable)) #TODO add exception #TODO exception
        
    def getTerrain(self):
        ''' '''
        return self._sTerrain
    
    def getAltitude(self):
        ''' '''
        return self._iAltitude
    
    def getOccupiable(self):
        ''' '''
        if self._bOccupiable:
            return 1
        else:
            return 0
    
    #Primarily for the Piece class.  Piece has a movement cost associated with each terrain type.
    def getTerrainList(self):
        ''' '''
        return self._sListTerrain
    
    ##################---Map string handlers---##################
    def toMapString(self):
        ''' '''
        TerrainWidth = self._iMapStringRightTerrain - self._iMapStringLeftTerrain
        AltitudeWidth = self._iMapStringRightAltitude - self._iMapStringLeftAltitude
        OccupiableWidth = self._iMapStringRightOccupiable - self._iMapStringLeftOccupiable
        
        return "{0:>{3}}{1:>{4}}{2:>{5}}".format(self.getTerrain(),
                                                    self.getAltitude(),
                                                    self.getOccupiable(),
                                                    TerrainWidth,
                                                    AltitudeWidth,
                                                    OccupiableWidth)
 
    def loadMapString(self,mapString):
        ''' '''
        #Check that map string is the expected length
        if len(mapString) != self._iMapStringLength:
            print("I'm a mapString problem! Illegal entry: '" +
                str(mapString)+"' is the wrong length.  Should be " + str(self._iMapStringLength) + 
                " characters") 
                #TODO Exception - final exception feed back should be passed
                #upwards to show invalid Map string, location in file
        else:
            try:
                terrain = re.sub(" ","",mapString[self._iMapStringLeftTerrain:self._iMapStringRightTerrain])
                altitude = int(re.sub(" ","",mapString[self._iMapStringLeftAltitude:self._iMapStringRightAltitude]))
                occupiable = int(re.sub(" ","",mapString[self._iMapStringLeftOccupiable:self._iMapStringRightOccupiable]))
                
                self.setTerrain(terrain)
                self.setAltitude(altitude)
                self.setOccupiable(occupiable)
            except:
                print("I could be exception handling for a map string") #TODO add exception handling, see above comment

    
    ##################---Private methods---##################

    
    def __testSpace(self):
        """Test routine for the space class"""
        print("\n--Begin Space class test routine--\n ")
        print("\nInitial space values:\n ")
        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
        print("Valid terrain list:",self.getTerrainList())
        
        initialMapString = self.toMapString()
        print("Map string:",initialMapString)
        
        self.loadMapString(initialMapString)
        print("Map string after reload:",initialMapString)
        
        print("\nAfter reloading initial map string:\n ")
        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
        
        #Valid changes
        self.setTerrain("S")
        self.setAltitude(1)
        self.setOccupiable(0)
        
        print("\nAfter making valid changes:\n ")
        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
        
        newMapString = self.toMapString()
        print("Map string:",newMapString)
        self.loadMapString(initialMapString)
        
        print("\nAfter reloading initial map string:\n ")
        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
        
        #Terrain
        print("\nCheck legal terrain values:\n ")
        for t in self._sListTerrain:
            self.setTerrain(t)
            print("Terrain:",self.getTerrain())
    
        #Altitude
        print("\nCheck legal altitude values:\n ")
        for t in self._iListAltitude:
            self.setAltitude(t)
            print("Altitude:",self.getAltitude())
            
        #Occupiable
        print("\nCheck legal occupiable values:\n ")
        for t in self._iListOccupiable:
            self.setOccupiable(t)
            print("Occupiable:",self.getOccupiable())
            
        print("Map string:",self.toMapString())
        

        print("\nAfter trying to load some invalid Map strings:\n ")
        self.loadMapString(" Q300") #Invalid terrain
        self.loadMapString(" P400") #Invalid altitude
        self.loadMapString(" P309") #Invalid occupiable
        self.loadMapString("  P151") #Too long
        
        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
    
        print("Map string:",self.toMapString())
        
        print("\nAfter trying to set invalid strings:\n ")
        #Invalid strings
        self.setTerrain("V")
        self.setAltitude("real high")
        self.setOccupiable("watermelon")
        
        
        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
    
        print("Map string:",self.toMapString())
        
        #invalid numerics
        print("\nAfter trying to set invalid numerics:\n ")
        self.setTerrain(1)
        self.setAltitude(12.5)
        self.setOccupiable(7)


        print("Terrain:",self.getTerrain())
        print("Altitude:",self.getAltitude())
        print("Occupiable:",self.getOccupiable())
    
        print("Map string:",self.toMapString())
        print("\n--End of Space class test routine--\n ")
    