#this is a part of series of programs for sorting file with an an arbitrarily long
#(base: 1000) amount of words, and returning a file with the words sorted.
import numpy as np

#counts number of lines in file
def countlines(f = "words.txt") : 
    fl = open(f, "r")
    count = 0
    for line in fl :
        count+= 1
    fl.close()
    return count

#retrieves all lines from file into a list and returns the list.... terrible memory-consuming,
#but this is v0
def retrieve(f = "words.txt") :
    fl = open(f, "r")
    arr = np.array([0])
    lines = []
    numlines = countlines()
    for i in range(numlines) :
        line = str(fl.readline().strip().lower())
        lines.append(line)
        print(i + 1 ," out of ", numlines, " lines processed... ", ((i + 1)/numlines) * 100, "% completeled", flush = True)
    return lines

#takes a list and swaps the indices a and b
def swap(givenlist, a, b) :
    k = givenlist[a]
    givenlist[a] = givenlist[b]
    givenlist[b] = k
    return givenlist

#takes lines, a list, and copies the values into a list of PlacedObjects 
def createEquavalentObjects(lines) : 
    linesOfPlacedObjects = []
    for line in lines: 
        currentPlacedObject = PlacedObject(line, lines)
        linesOfPlacedObjects.append(currentPlacedObject)
    print(linesOfPlacedObjects)
    return linesOfPlacedObjects


#PlacedObject is an interesting tool for sorting. Each PlacedObject has a "place"
#that is generated by looking at all other values in the list (arr), and counting
#how many times it was bigger. Incidentally, if there are no repeats, this will be 
#the sorted index of the PlacedObject, along with all the other values.

class PlacedObject : 
    place = 0
    value = ""
    immutable = False
    def __init__(self, value, arr, arrIsOfPlacedObjects = False) :
        self.setValue(value)
        if arrIsOfPlacedObjects == False :
            self.place = self.findPlaceNormally(arr)
        else : 
            self.place = self.findPlaceInArrayOfPlacedObjects(arr)

    def setValue(self, value) :
        self.value = value

    def getValue(self) : 
        return self.value 

    def getPlace(self) : 
        return self.place

    def findPlace(self, arr, normalProcess = True) : 
        if normalProcess : 
            self.place = self.findPlaceNormally(arr) 
        else :
            self.place = self.findPlaceInArrayOfPlacedObjects(arr)

    def findPlaceNormally(self, arr) : 
        count = 0
        for i in range(len(arr)) : 
            if self.compareWithRegularObject(arr[i]) == 1 : 
                count += 1
        return count

    def findPlaceInArrayOfPlacedObjects(self, arr) :
        count = 0
        for i in range(len(arr)) : 
            if self.compareWithPlacedObject(arr[i]) == 1 :
                count += 1
        return count
    
    def setImmutable(self) : 
        self.immutable = True
    
    def isImmutable(self) : 
        return self.immutable

    def compareWithPlacedObject(self, otherobject) :
        if (otherobject.getValue() < self.value) : 
            return 1
        else :
            return 0

    def compareWithRegularObject(self, regobject) : 
        if (regobject < self.value) : 
            return 1
        else : 
            return 0

    def swapIntoPlace(self, arr) : 
        if not(arr[self.place].isImmutable()) : 
            arr = swap(arr, arr.index(self), self.place)
        else :
            print("Unable to switch PlacedObject with value: ", self.value, "into ", self.place)
        return arr
    
    def __repr__(self) : 
        returned = ""
        returned += "\n"
        returned += "Value: "; returned += self.value; returned += "\n"
        returned += "Place: "; returned += str(self.place); returned += "\n"
        returned += "Immutable: "; returned += str(self.immutable)
        return returned

lines = retrieve()
linesobjects = createEquavalentObjects(lines)
print(type(linesobjects[0]))
linesobjects[0].findPlace(linesobjects, False)
for i in range(len(linesobjects)) : 
    linesobjects = linesobjects[i].swapIntoPlace(linesobjects)
print(linesobjects)