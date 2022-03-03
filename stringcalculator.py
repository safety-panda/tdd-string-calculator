from typing import List

def add(string_input: str) -> int:
    if(len(string_input) == 0) : return 0
    else:
        num_comma_split: List[str] = string_input.split(',')   
        sum_result: int = 0

        for i in range(len(num_comma_split)):
            sum_result = sum_result + int(num_comma_split[i])

        return sum_result