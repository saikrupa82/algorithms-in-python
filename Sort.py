class SortingAlgo:
    def __init__(self,lis):
        assert type(lis)==list,"Please Enter A List"
        self.lst=lis

    def selectionSort(self):
        temp_lst = self.lst.copy()
        for i in range (len(self.lst)):
           
            index = i
            for j in range(index,len(self.lst)):
                if temp_lst[i] > temp_lst[j]:
                    temp_lst[i] , temp_lst[j] = temp_lst[j] , temp_lst[i]
                index=j
        return temp_lst
    

    def bubbleSort(self):
        temp_lst = self.lst.copy()
        while True:
            done = True
            for i in range (len(self.lst)):
                if i < len(self.lst)-1:
                    
                    if temp_lst[i] > temp_lst[i+1]:
                        temp_lst[i] , temp_lst[i+1] = temp_lst[i+1] , temp_lst[i]
                        print(temp_lst)
                        done = False
                else:
                    break
            if done :
                return temp_lst   
            
               



lst = SortingAlgo([54,45,90,67,78,10])
print([54,45,90,67,78,10])
print("selectionSort of given numbers is",lst.selectionSort())
print("bubbleSort of given numbers is",lst.bubbleSort())





