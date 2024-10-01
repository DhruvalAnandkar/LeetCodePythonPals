from typing import List, Union
class Array:
    """Modifies the List objects
    """
    def sort(self, nums: List[Union[int,str]], reverse: bool=False)->List[Union[int,str]]:
        """Sorts the array in ascending/descending order

        Args:
            nums (List[Union[int,str]]): A array object to sort out
            reverse (bool, optional): Reverses the order. Defaults to False.

        Returns:
            List[Union[int,str]]: Returns the updated ordered list
        """
        return sorted(nums,reverse=reverse)
arr = Array()
print(arr.sort([0,5,2,7,8],False))
