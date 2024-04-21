import math

class SearchAlgorithms:
    # Initialize the list for searching and item to search
    def __init__(self,searching_list,searching_item):
        self.searching_list = searching_list
        self.searching_item = searching_item
        # Initilize length of the searching list
        self.length = len(self.searching_list)
        # Check list and search item are valid before passing them into the functions
        if not self.searching_list:
            raise ValueError("An empty list is given")
        if self.searching_item is None:
            raise ValueError("Searching item is not given")
        if not all(isinstance(self.searching_item, type(element)) for element in self.searching_list):
            raise ValueError("Searching item and list elements must be in same type. Please check !")
        print(f"Searching list is  {self.searching_list}")
        print(f"Searching item in the list is : {self.searching_item}")

    # Define linear search algorithm
    def LinearSearch(self):
        try:
            for index in range(self.length):
                if self.searching_list[index] == self.searching_item:
                    return index
            print(f"The item {self.searching_item} is not in the list.")
            return None
        except Exception as e:
            print(f"An error occurred. Please check the inputs again. Error : {e}")
            return None
    # Define linear search algorithm to return list of repeated search values in the given list
    def LinearSearchList(self):
        try:
            return [index for index in range(self.length) if self.searching_list[index] == self.searching_item]
        except Exception as e:
            print("Error")

    # Define binary search algorithm
    def BinarySearch(self):
        try:
            # Check the given list is sorted or not
            if not sorted(self.searching_list) == self.searching_list:
                print("Given list is not sorted. To perform Binary search, it is sorted.")
                self.searching_list.sort()
                left,right = 0,self.length-1

            while left<=right:
                # Decide middlie point of the looking section of the sorted list
                searching_position = (left+right)//2
                # Check middle element of the list if it is searching item or not
                if self.searching_item == self.searching_list[searching_position]:
                    return (self.searching_list,searching_position)
                # Check searching item if it is near to the left or not
                elif self.searching_item < self.searching_list[searching_position]:
                    right = searching_position - 1
                else:
                    left = searching_position + 1

            # If the item is not found, return this
            print(f"{self.searching_item} is not in the list.")
            return (self.searching_list, None)
        except Exception as e:
            print(f"An error occurred: {e}")
            return (self.searching_list, None)

    def JumpSearch(self):
        # Check the given list is sorted or not
        if not sorted(self.searching_list) == self.searching_list:
            print("Given list is not sorted. To perform JumpSearch, it is sorted.")
            self.searching_list.sort()
        step = jump = int(math.sqrt(self.length))

        # Search the list by jumping to find sublist contains the element
        while step<self.length:
            # If looking smaller than target, go further
            if self.searching_list[step] < self.searching_item:
                step += jump
            # If looking larger than targe, go back
            elif self.searching_list[step] > self.searching_item:
                break
            # If jumped item is searching item, return the index
            elif self.searching_list[step] == self.searching_item:
                return (self.searching_list,step)

        # Doing a linear search for searching item in the block beginning with prev
        for item in range(step-jump, min(step + jump, self.length)):
            if self.searching_list[item] == self.searching_item:
                return (self.searching_list,item)
        # If item not in the list, return None
        return (self.searching_list,None)
