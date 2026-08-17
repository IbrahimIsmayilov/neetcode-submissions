class Solution:
    # Overview: Replaces every element in an array with the greatest element to its right and replaces the last element with -1.

    # Steps:
    # 1. Create a variable called current_max_val to keep track of the current greatest element to the right of other elements. Set it equal to the last value in the array. Create a variable temp which when an element is greater than current_max_val will store the iterated element before a swap.
    # 2: Start iterating the array from its second last element and check if the current_max_val is greater than the iterated element. If so, replace the element with current_max_val. Else, update temp to be the iterated element, update the iterated element to be equal to the current_max_val, and update current_max_val to be equal to temp. 
    # 3: Update the last element of the array to -1 and return the array
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max_val = arr[-1]
        temp = None
        for index in range(len(arr) - 2, -1, -1):
            if current_max_val > arr[index]:
                arr[index] = current_max_val
            elif current_max_val < arr[index]:
                temp = arr[index]
                arr[index] = current_max_val
                current_max_val = temp
                
        arr[-1] = -1

        return arr

        

        