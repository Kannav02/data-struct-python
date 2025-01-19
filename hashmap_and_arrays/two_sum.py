from typing import List,Tuple,Optional

# linear approach takes o(n^2) time and o(1) space
# this approach has a space complexity of o(n) and time as o(n)
def two_sum(array:Optional[List[int]],sum:int)->Tuple[int,int]:
    if array is None:
        return (-1,-1)

    hash_maps = {}

    for idx,element in enumerate(array):
        left_over = sum-element

        if left_over in hash_maps:
            return (idx,hash_maps[left_over])
        hash_maps[element] = idx
    return (-1,-1)

        