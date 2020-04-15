class Solution(object):
  def binarySearch(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if array is None or len(array)==0:
      return -1
    left = 0
    right = len(array)-1
    while left < right-1:
      mid = (left+right)//2
      if array[mid] == target:
        return mid
      if array[mid] < target:
        left = mid
      else:
        right = mid
    if array[left] == target:
      return left
    if array[right] == target:
      return right
    return -1
    
