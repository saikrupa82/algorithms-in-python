from timeit import default_timer as timer
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
                        done = False
                else:
                    break
            if done :
                return temp_lst   
            
    def _splitmergesort(self,lst):
        if len(lst) == 1:
            return tuple(lst)
        d=int(len(lst)/2)
        # spilt = lambda lsts: lsts[:d], lsts[d:]
        def split(lsts): return lsts[:d], lsts[d:]
        left, right= split(lst)
        if len(left) == 1 and len(right) == 1:
            print(left,right)
            if left[0]> right[0]:
                return right[0], left[0]
            else:
                return left[0], right[0]
        return self._splitmergesort(left), self._splitmergesort(right)

    # def _mergeingtheMergeSort(self, tup ):
    #     temp_lst = list(tup)
    #     for i in temp_lst:
    #         if len(list())


    def merge(self) :
        temp_lst = self.lst.copy()
        # return self._mergeingtheMergeSort(self._splitmergesort(temp_lst)) 
        return self._splitmergesort(temp_lst)
        # for i in temp_lst:
        #     d=int(len(temp_lst)/2)
        #     spilt = lambda lst: lst[:d],lst[d:]
        #     left,right=split(temp_lst)



givenList = [54,45,90,67,78,10,46,25, 11,12,15,18,20]
lst = SortingAlgo(givenList)
print(givenList)
print("selectionSort of given numbers is",lst.selectionSort())
print("bubbleSort of given numbers is",lst.bubbleSort())
print("MergeSort of given numbers is",lst.merge())
 
                
lst = SortingAlgo([54,45,90,67,78,10])
print([54,45,90,67,78,10])

start_time = timer()
print("selectionSort of given numbers is", lst.selectionSort())
print("Selection Sort took " + str(timer() - start_time) )

start_time = timer()
print("bubbleSort of given numbers is", lst.bubbleSort())
print("Bubble Sort took " + str(timer() - start_time) )





