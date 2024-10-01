from typing import List, Union
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
    
    def dup(self, arr: List[Union[int,str]], action: str='FILTER')-> List[Union[list,int]]:
        """Manipulates duplicates in the list

        Args:
            arr (List[Union[int,str]]): Array to update
            action (str, optional): Dictates on what the output should be. Options: \"FILTER\" | \"GET\". Defaults to 'FILTER'.

        Returns:
            List[Union[list,int]]: The updated array or the length of the updated array
        """
        if action.upper()=='FILTER':
            arr = list(set(arr))
        else:
            arr = len(list(set(arr)))
        return arr
        
# Test executer
print(Array().dup([1,1,2],'FILTER'))
