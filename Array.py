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
