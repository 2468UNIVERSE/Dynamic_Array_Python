# ctype is a foreign python library that we will use to make c data type that is array of c to create list class in python
import ctypes

class MyList:

    def __init__(self):
        # size is how many max ele i can store
        # n is the no. of element stored at the moment in the list
        self.size = 1
        self.n = 0

        # create a C type array with size = self.size

        self.A = self.__make_array(self.size)

    # to return the length of the array
    def __len__(self):
        return self.n
    
    # printing the list using magic function
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return '['+ result[:-1] + ']'
    
    # getting the index of the item using magic method
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
        
    # deleting the specified position element
    def __delitem__(self,index):
        if self.n == 0:
            return "ValueError list is Empty"
        elif 0<= index < self.n:
            for i in range(index,self.n-1):
                self.A[i] = self.A[i+1]
        
            self.n = self.n-1
    
    # function to define the sum of elements in the list
    def sum(self):
        add = 0
        for i in range(self.n):
            add = add + self.A[i]
        return add


    
    # deleting the last element i.e poping
    def pop(self):
        if self.n == 0:
            return 'Empty list'
        
        print(self.A[self.n-1])
        self.n = self.n - 1

    # function to clear the list i.e to delete all the element at once
    def clear(self):
        self.n = 0
        self.size = 1

    # function to find an element is at what index
    def find(self,item):
        for i in range(self.n):
            if item == self.A[i]:
                return i
        return 'ValueError not in list'
    
    # function to insert an element in the list at specified position
    def insert(self,index,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,index+1,-1):
            self.A[i] = self.A[i-1]
        self.A[index] = item
        self.n = self.n+1
    

    # function to remove an element 
    def remove(self,item):
        index = self.find(item)

        if type(index) == int:
            # delete
            self.__delitem__(index)
        else:
            return index

    
    # defining the append function
    def append(self,item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)
        
        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content from A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    # function to sort and array default in ascending order
    def sort(self,bool=True):
        if bool == True:
            for i in range(self.n):
                for j in range(0, self.n-i-1):
                    if self.A[j] > self.A[j+1]:
                        temp = self.A[j]
                        self.A[j] = self.A[j+1]
                        self.A[j+1] = temp
        else:
            for i in range(self.n):
                for j in range(0, self.n-i-1):
                    if self.A[j] < self.A[j+1]:
                        temp = self.A[j]
                        self.A[j] = self.A[j+1]
                        self.A[j+1] = temp


    # function to max
    def max(self):
        self.sort()
        # print([self.A[i] for i in range(self.n)])
        return self.A[self.n-1]
    
    #function to find the min
    def min(self):
        self.sort()
        return self.A[0]

    # function to extend
    def extend(self,list):
        for i in range(len(list)):
            self.append(list[i])
        return [self.A[i] for i in range(self.n)]
     

    def __make_array(self,capacity):
        # creates a c type array(static or refential) with size capacity
        return (capacity*ctypes.py_object)()
    
l = MyList()
l.append(100)
l.append(90)
l.append(10)
l.append(20)
l.append(30)
l.append(60)

print(l)
print(l.extend([70,200]))
# print(l.sum())
# l.sort()
# print(l)
# print(l.max())
# print(l.min())
    





