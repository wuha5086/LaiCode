class Solution(object):
  def firstOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    left = 0
    right = len(array)-1
    if right < 0:
      return -1
    while left < right-1:
      middle = left + (right-left)//2
      if array[middle] < target:
        left = middle
      elif array[middle] >= target:
        right = middle
    if array[left] == target:
      return left
    if array[right] == target:
      return right
    return -1
