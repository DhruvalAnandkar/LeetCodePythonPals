# Working in process
from typing import List
"""
Sorts numbers be ascending/descending order
"""
def sortNumArr(nums: List[int], reverse: bool=False)->List[int]:
  return sorted(nums,reverse=reverse)
  
print(sortNumArr([1,4,2,0],True))
