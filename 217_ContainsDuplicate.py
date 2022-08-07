#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
    #o(n), o(n) -> time , space
                      
