import threading
import xml.etree.ElementTree as X
import unittest

def partition(array, low, high):
  i = low
  p = array[high]
  for j in range(low, high):
    if array[j] <= p:
      array[i],array[j] = array[j],array[i]
      i+=1
  array[i],array[high] = array[high],array[i]
  return i

def qsort(array, low, high):
  if low<=high:
    p = partition(array, low, high)
    t1 = threading.Thread(target=qsort, args=(array, low, p-1))
    t2 = threading.Thread(target=qsort, args=(array, p+1, high))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def qsort_handler(array, low, high):
  qsort(array, low, high)
  return array

r = X.parse('input.xml').getroot()
print "INPUT ARRAY = "
print r.text
array = map(int, r.text.split())
qsort_handler(array, 0, len(array)-1)
print "SORTED ARRAY = "
for i in array:
  print i
  
class MyTesting(unittest.TestCase):
  def test_invoker(self):
    self.assertEqual(qsort_handler(array,0, len(array)-1),[1,2,3,5,7,9,11,12,22,24,33,34,36,44,45,48,55,60,66,77,88,90,99,115,118,557,664,776,887,998,999])

print "----------------------------------"
print "DOING TESTING"
unittest.main()

'''
start = time.time()
quicksort(array, 0, len(array)-1)
end = time.time()

print('time needed: ', end-start)
'''
