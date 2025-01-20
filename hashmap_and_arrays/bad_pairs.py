from typing import List


def bad_pairs(array:List[int])->int:
    # normal solution is finding all the bad pairs naively, which is o(n^2)
    # condition for bad pair is nums[j] - nums[i] != j-i i<j
    # we change the condition a bit nums[i] - i != nums[j] - j , which means if key[i] = nums[i] -1 , key[i] != key[j] should be the case
    # total pairs = n(n-1)/2

    n = len(array)
    total_pairs = n*(n-1)//2
    count_map = {}
    good_pairs = 0

    for i, num in enumerate(array):
        key = num-i
        if key in count_map:
            good_pairs+= count_map[key]
            count_map[key]+=1
        else:
            count_map[key]=1
    
    return total_pairs - good_pairs