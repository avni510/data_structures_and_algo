class Heap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    # O(N log N)
    def insert(self, data):
        self.heap_list.append(data)
        self.current_size += 1
        self.__perc_up(self.current_size)

    # O(log N)
    def del_min(self):
        minimum = self.heap_list[1]
        self.current_size -= 1
        last_element = self.heap_list.pop()
        self.heap_list[1] = last_element
        self.__perc_down(1)

        return minimum

    def __perc_up(self, i):
        parent = i // 2
        while parent > 0:
            if self.heap_list[i] < self.heap_list[parent]:
                temp = self.heap_list[parent]
                self.heap_list[parent] = self.heap_list[i]
                self.heap_list[i] = temp
            i = parent 
            parent = i // 2

    def __perc_down(self, i):
        next_child = i * 2
        while next_child <= self.current_size:
            min_child = self.__get_min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = temp

            i = min_child
            next_child = i * 2
    

    def __get_min_child(self, i):
        left_child = i * 2
        right_child = i * 2 + 1 

        if right_child > self.current_size:
            return left_child
        elif self.heap_list[left_child] > self.heap_list[right_child]:
            return right_child
        else:
            return left_child
