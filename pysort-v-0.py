#PlacedNumber is a class to help sort arrays of numbers into increasing order.
#Each PlacedNumber has two attributes, place and value, and the class has a value, numbers.
#numbers is a list of all the current instances of PlacedNumber
#Value is just the value of the number, but place is where the magic happens.
#Place is calculated by counting how many times the PlacedNumber's value is 
#Bigger than all the others' values (see calculatePlace())
#That place is the its index in numbers if it was sorted, and with duplicates, it... sorts itself out
#With some assurance to protect against edge cases (updatePlaces()),
#And some swapification, (swapIntoPlace(), sortNumbers()), 
#Numbers can be sorted and formed into a normal list.
class PlacedNumber() : 
    numbers = []

    def __init__(self, value) : 
        self.value = value
        self.place = self.calculatePlace()
        self.numbers.append(self)
        self.numbers = self.updatePlaces()

    def __str__(self) : 
        return str(self.value)

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

    def calculatePlace(self) : 
        count = 0
        for num in self.numbers : 
            if self.value > num.value : 
                count += 1
        return count

    def getPlace(self) : 
        return self.place

    def setPlace(self, place) : 
        self.place = place

    @classmethod
    def sortNumbers(cls) : 
        cls.updatePlaces()
        while not cls.numbersIsSorted() : 
            for num in cls.numbers : 
                num.swapToPlace()
                print(cls.numbers)
                if cls.numbersIsSorted() : 
                    print("Done!")
                    return
        print("Done!")

    def swapToPlace(self) : 
        nums = self.numbers #for clarity and cleanliness
        index = nums.index(self)
        index2 = self.place
        k = nums[index2]
        nums[index2] = self
        nums[index] = k

    @classmethod
    def updatePlaces(cls) : 
        for num in cls.numbers : 
            num.place = num.calculatePlace()
        return cls.numbers
    
    @classmethod
    def numbersIsSorted(cls) : 
        for i in range(len(cls.numbers) - 1) :
            if cls.numbers[i] > cls.numbers[i+1] : 
                return False
        return True
    

for i in range(10) : 
    x = input("Enter a number: ")
    y = PlacedNumber(x)
print(PlacedNumber.numbers)
PlacedNumber.sortNumbers()


