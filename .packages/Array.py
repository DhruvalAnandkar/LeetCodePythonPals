from typing import List, Union
from collections import Counter
class Array:
    """Modifies the List objects
    """
    def sort(self, arr: List[Union[int,str]], reverse: bool=False)->List[Union[int,str]]:
        """Sorts the array in ascending/descending order

        Args:
            arr (List[Union[int,str]]): A array object to sort out
            reverse (bool, optional): Reverses the order. Defaults to False.

        Returns:
            List[Union[int,str]]: Returns the updated ordered list
        """
        return sorted(arr,reverse=reverse)
    def dup(self, arr: List[Union[int,str]], repeat: int=1, action: str='FILTER')-> List[Union[list,int]]:
        """Manipulates duplicates in the list

        Args:
            arr (List[Union[int,str]]): Array to update
            repeat (int): Restricts how many times the number can repeat. Default to 1 
            action (str, optional): Dictates on what the output should be. Options: \"FILTER\" | \"GET\". Defaults to 'FILTER'.

        Returns:
            List[Union[list,int]]: The updated array or the length of the updated array
        """
        updated_arr = []
        if action.upper()=='FILTER':
            for x in range(len(arr)):
                if(updated_arr.count(arr[x]) < repeat): updated_arr.append(arr[x])
            arr = updated_arr
        else:
            for x in range(len(arr)):
                if(updated_arr.count(arr[x]) < repeat): updated_arr.append(arr[x])
            arr = len(updated_arr)
        return arr
    def max(self, arr: List[Union[int,str]], common: bool=True)->int:
        """Returns the most common number or highest number in the array

        Args:
            arr (List[Union[int,str]]): Array to check for
            common (bool): Gets the common number. Default to 'True'
            
        Returns:
            int: The common number in array
        """
        return max(Counter(arr).keys(), key=Counter(arr).get) if common else max(arr)
    def min(self, arr: List[Union[int,str]], common: bool=True)->int:
        """Returns the least common number or lowest number in the array

        Args:
            arr (List[Union[int,str]]): Array to check for
            common (bool): Gets the least common number. Default to 'True'

        Returns:
            int: The least common number in array
        """
        return min(Counter(arr).keys(), key=Counter(arr).get) if common else min(arr)
    def rotate(self, arr: List[Union[int,str]], steps=1)-> List[Union[int,str]]:
        """Rotates the array by x of steps

        Args:
            arr (List[Union[int,str]]): Array to rotate
            steps (int, optional): How many steps to rotate. Defaults to 1.

        Returns:
            List[Union[int,str]]: Rotated array
        """
        arr[:] = arr[-(steps%len(arr)):] + arr[:-(steps%len(arr))]
        return arr
