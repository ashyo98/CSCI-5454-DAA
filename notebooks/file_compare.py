import math

nums = [3,3,4,3,3]

if len(nums) % 2 == 0:
    maj_count = len(nums)/2
else:
    maj_count = math.ceil(len(nums)/2)

def count_occurrence(ele):
    return sum(1 for i in range(len(nums)) if nums[i] == ele)


def majority_element_rec(lo, hi):
    # base case; the only element in an array of size 1 is the majority
    # element.
    if lo == hi:
        return nums[lo]

    # recurse on left and right halves of this slice.
    mid = (hi-lo)//2 + lo
    left = majority_element_rec(lo, mid)
    right = majority_element_rec(mid+1, hi)

    # if the two halves agree on the majority element, return it.
    if left == right:
        return left

    # otherwise, count each element and return the "winner".
    left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
    right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

    return left if left_count > right_count else right

ans = majority_element_rec(0, len(nums)-1)
print(count_occurrence(ans), maj_count)
if count_occurrence(ans) > maj_count:   
    print(ans)
else:
    print("Nill")