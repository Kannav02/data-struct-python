from typing import List

def matrix2DSearch(matrix:List[List[int]],val:int)->bool:
    bottom_row,top_row = 0,len(matrix)-1

    while bottom_row <= top_row:
        correct_row = bottom_row + top_row // 2

        if val > matrix[correct_row][-1]:
            bottom_row = correct_row+1
        elif val < matrix[correct_row][0]:
            top_row = correct_row-1
        else:
            break
    
    if not bottom_row <= top_row:
       return False
    
    l = 0
    r = len(matrix[correct_row])-1

    while l <= r:
        mid = l+r//2

        if val > matrix[correct_row][mid]:
            l = mid + 1
        elif val < matrix[correct_row][mid]:
            r = mid - 1
        else:
            return True

    return False
    
    
