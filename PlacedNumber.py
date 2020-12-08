#PlacedNumber is a class whose methods + attributes revolve around sorting.
#It's method of sorting is relying on the fact that the proper index of a
#list sorted into increasing order will be the number of times it is greater
#than all the numbers in the list.
class PlacedNumber() : 
    #a list that keeps all of the PlacedNumbers that have been created,
    #so that they can be sorted
    numbers = []
    checks = 0
    #typical instantiation
    def __init__(self, value) : 
        self.value = value
        self.place = self.calculatePlace(self.numbers)
        self.numbers.append(self)
        self.numbers = self.updatePlaces(self.numbers)

    def __str__(self) : 
        return str(self.value) + "," + str(self.place)

    def __repr__(self) : 
        return str(self)

    def __gt__(self, p) : 
        return self.value > p.value

    def __lt__(self, p) : 
        return self.value < p.value

    def __ge__(self, p) : 
        return self.value >= p.value

    def __le__(self, p) : 
        return self.value <= p.value

    def __int__(self) : 
        import warnings
        if type(self.value) == float : 
            warnings.warn("Turning Float Value Into Int")
        return int(self.value)
    
    def __float__(self) : 
        return self.value

    #calculates the PlacedNumber's *place*, or its sorted index in nums
    def calculatePlace(self, nums) : 
        self.count = 0
        count = 0
        for num in nums : 
            if self.value > num.value : 
                count += 1
        return count

    def getPlace(self) : 
        return self.place

    def setPlace(self, place) : 
        self.place = place

    #sorts numbers into the proper place until sorted.
    @staticmethod
    def sortNumbers(nums) : 
        if type(nums[0]) is not None : 
            PlacedNumber.updatePlaces(nums)
        while not PlacedNumber.isSorted(nums): 
            for num in nums : 
                if not PlacedNumber.isSorted(nums) : 
                    num.swapToPlace(nums)
                else : 
                    return nums
        return nums
            
    #helper to sortNumbers, essentailly a garden variety swap.
    def swapToPlace(self, nums) : 
        index = nums.index(self)
        index2 = self.place
        k = nums[index2]
        nums[index2] = nums[index]
        nums[index] = k
        return nums

    #when adding new PlacedNumbers, this function is called to make all the other numbers
    #know that their place may have changed, otherwise multiple (unequal) numbers
    #would be trying to get to the same place, or worse, be in wrong order.
    @staticmethod
    def updatePlaces(nums) : 
        for num in nums : 
            num.place = num.calculatePlace(nums)
        return nums
    
    #used in sortNumbers() to check if the numbers in nums are sorted
    @classmethod
    def isSorted(cls, nums) :
        for i in range(len(nums) - 1) :
            if nums[i] > nums[i+1] : 
                return False
        return True
        

    
    #the following are nice functions to interact with standard objects

    #puts all the numbers in *numbers* and returns the resulting list.
    @classmethod
    def convertNumbersToList(cls) : 
        nums = []
        for num in cls.numbers : 
            nums += num.value
        return nums

    #takes all the numbers in a list of ints and floats and converts them into
    #a list of PlacedNumbers.
    @staticmethod
    def convertListIntoPNs(nums) : 
        numsPN = []
        for num in nums : 
            y = PlacedNumber(num)
            numsPN.append(y)
        return numsPN
    
    #takes PN list and returns a normal list
    @staticmethod
    def convertPNsIntoList(numsPN) : 
        nums = []
        for num in numsPN : 
            nums.append(num.value)
        return nums
        
    
    #takes a garden variety list and sorts is using PN functionality
    @staticmethod  
    def takeListAndSort(nums) : 
        nums = PlacedNumber.convertListIntoPNs(nums)
        nums = PlacedNumber.sortNumbers(nums)
        nums = PlacedNumber.convertPNsIntoList(nums)
        return nums


    



