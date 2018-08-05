#making max heap
class heap(object):

    def __init__(self,l):
        self.heap=[0]*len(l)
        self.index=0
        self.heap[0]=l[0]
        self.insert(l)


    def insert(self,l):
        for i in l[1:]:

            self.index=self.index+1
            self.heap[self.index]=i
            self.heapify_up(self.index)

    def heapify_up(self,index):

        parent_index=(index-1)//2
        while (parent_index>=0) and (self.heap[index]>self.heap[parent_index]):
            temp=self.heap[parent_index]
            self.heap[parent_index]=self.heap[index]
            self.heap[index]=temp

            index=parent_index
            parent_index=(index-1)//2

    def show_heap(self):
        print(self.heap)

    def  max_element(self):
        print(self.heap[0])
#pop always take place from top_most element of heap(ie max element if heap)
    def pop(self):

        self.heap[0]=self.heap[self.index]
        del self.heap[self.index]
        self.index=self.index-1
        print(self.index)


        left_child_index=1
        right_child_index=2


        while(left_child_index<=self.index):
            if(left_child_index<=self.index):
                swap_with=0
                if(right_child_index > self.index):
                    swap_with=left_child_index
                else:
                    if self.heap[right_child_index]>self.heap[left_child_index] and self.heap[right_child_index]>self.heap[swap_with] :
                        swap_with=right_child_index
                    elif self.heap[right_child_index]<self.heap[left_child_index] and self.heap[left_child_index]>self.heap[swap_with] :
                        swap_with=left_child_index
                    else:
                        swap_with=swap_with
                        break

            temp=self.heap[swap_with]
            self.heap[swap_with]=self.heap[0]
            self.heap[0]=temp

            print(self.heap)
            left_child_index=2*swap_with+1
            right_child_index=2*swap_with+2
