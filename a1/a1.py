import unittest

def binary_srch(arr,size,key):
	low = 0
	high = size-1;
	mid = int((high-low)/2)
	print "Array=",arr, "Element to be searched for=", key
	while low <= high:
		temp = 0;
		if arr[mid] == key:
			print "Element ", key, " found at position ", mid+1, "\n"
			temp = 1
			return mid+1
		elif key < arr[mid]:
			high = mid-1;
			mid = int((high+low)/2)
		
		else: 
			low = mid+1
			mid = int((low+high)/2)
		
	if temp == 0:
		print "Element not found"
		return 0;

class MyTest(unittest.TestCase):
	def test_positive(self):
		self.assertEqual(binary_srch([10,56,22,76,90],5,22),3)
	def test_negative(self):
		self.assertEqual(binary_srch([10,56,22,76,90],5,25),0)


arr = []
size = int(input("Enter number of elements="))
print "Enter elements"

for i in range(0,size):
	arr.append(input())

print "Input Array", arr	
arr.sort()
print "Sorted  Array", arr

x = int(input("Enter element to be searched="))
place = binary_srch(arr,size,x)


print "----Testing----"
unittest.main()


#For accpeting input through a file
'''
def main():
	print "Enter elements."
	a=map(int, raw_input().split())
	print "List is created.\n"
	key=int(raw_input("Enter searching element\n").strip())
	binSearchObj = BinarySearch(a,key)
	binSearchObj.perform_binary_search()
'''

