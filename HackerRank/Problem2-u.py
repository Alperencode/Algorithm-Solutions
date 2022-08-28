class Reverse:
    def __init__(self,arr):
        self.arr = arr
        self.l,self.r = 0,0
            
    def canReverse(self):
        reverse = []
        for index,item in enumerate(self.arr):   
            if index != len(self.arr) - 1:
                if item > self.arr[index+1]:
                    self.l = index
                    arr2 = self.arr[index:]
                    for index2,item2 in enumerate(arr2):
                        if index2 != len(arr2)-1: 
                            if item2 > arr2[index2+1]:
                                reverse.append(item2) 
                            else:
                                reverse.append(item2)
                                self.r = index2
                                break
                        else:
                            reverse.append(item2)
                            self.r = index2
                            break  
                    break
            else:
                return False
        
        self.arr[self.l,self.r] = reversed(self.arr[self.l,self.r])
        return self.arr == sorted(self.arr) 

class Swap:
    def __init__(self,arr):
        self.arr = arr
        self.l,self.r = 0,0
    
    def canSwap(self):
        for index,item in enumerate(self.arr):
            if index != len(self.arr) -1:
                if item > self.arr[index+1]:
                    # Gave up here :D
                    pass 
            else:
                return False
            

def almostSorted(arr):
    if arr == sorted(arr):
        print("yes")
    else:
        # Checks
        pass