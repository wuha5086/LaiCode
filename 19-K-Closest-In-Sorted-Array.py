class Solution(object):
  def closest(self, array, target):
    if not array:
      return -1
    left = 0
    right = len(array)-1
    while left < right -1:
      mid = (left+right)//2
      if array[mid] < target:
        left = mid
      elif array[mid] > target:
        right = mid
      else:
        return mid
    if abs(array[left]-target) < abs(array[right]-target):
      return left
    else:
       return right
    
  def kClosest(self,array,target,k):
    res = []
    if len(array) == 0 or k==0:
      return res
    close = self.closest(array,target)

    res.append(array[close])
    left = close -1
    right = close + 1
    total = len(array)
    while len(res) < k and (left >= 0 or right < total):
      if right < total and (left < 0 or abs(array[left]-target) > abs(array[right] - target)):
        res.append(array[right])
        right += 1
      elif left >= 0:
        res.append(array[left])
        left -= 1
    return res
  


