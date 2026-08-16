class Solution:
    # Steps:
    
    # 1. Create 2 variables, one that tracks the list from the beginning of the list, the other from the end. The variable that starts from the beginning of the list will be incremented where as the variable that starts from the end of the list will be decremented as the main while loop of the function continues.
    # 2. Set the main while loop of the function that continues based on the condition that the variable that is being incremented is not greater than the variable that is being decremented. 
    # 3. If the variable being incremented equals val, do not increment it that iteration, go to the last element from the end of the list not checked and replace it with val. If the variable being incremented is not val, keep incrementing it.
    # 4. If the val value was swapped, check if it was swapped with an another val value and swap again if so. Return the number of elements represented by the variable being decremented after the while loop finishes.

    # Time Complexity: O(n), where n represents the total number of elements in the list 
    # Given an integer array nums and an integer val, removes all occurences of val in-place and returns the number of element not equal to val
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n


                    
                

        


        