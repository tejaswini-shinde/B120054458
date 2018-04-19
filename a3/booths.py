def dec_bin(num):
	bin_num = [0]*8
	index = 7
	
	while num and index>=0:
		quotient = num/2
		remainder = num%2
		
		bin_num[index] = remainder
		num = quotient
		index = index-1
	return bin_num
	
def shift_right(arr):
	arr.insert(0, arr[0])
	arr.pop()
	return arr
	
def add(x,y):
	result = [0]*len(x)
	index = len(x)-1
	carry = 0
	
	while index >= 0:
		temp_sum = x[index] + y[index] +carry
		carry = temp_sum/2
		
		result[index] = temp_sum%2
		index = index - 1		

	return result
	
def bin_dec(num):
	flag = 1
	bits = len(num)
	
	if num[0] == 1:
		flag = -1
		for i in range(bits):
			num[i] = 1 - num[i]
		
		one = [0]*(bits-1) +[1]
		num = add(num,one)
	
	power = 0
	dec_num = 0
	index = bits-1
	
	while index >= 0:
		if num[index]==1:
			dec_num = dec_num + 2**power
		power+=1
		index-=1
	print("decimal calculated: ", dec_num)
	return flag*dec_num
			
def booths_mul(n1,n2):
	Q = dec_bin(n1)
	M = dec_bin(n2)
	print("decimal numbers:",n1,n2,"\nBinary numbers:",Q,M)
	Q_1 = 0
	M_1 = dec_bin(-n2)
	A = [0]*8
	
	allbits = []
	allbits.extend(A)
	allbits.extend(Q)
	allbits.append(Q_1)
	
	M = M + [0]*9
	M_1 = M_1 + [0]*9
	
	for i in range(8):
		if (allbits[-2] == 1 and allbits[-1] == 0) :
			allbits = add(allbits,M_1)
			#print(allbits[0:8],"\t",allbits[9:16],"\t",allbits[-1],"-->A=A-M")
		elif (allbits[-2] == 0 and allbits[-1] == 1) :
			allbits = add(allbits,M)
			#print(allbits[0:8],"\t",allbits[9:16],"\t",allbits[-1],"-->A=A+M")
			
		allbits = shift_right(allbits)
		#print(allbits[0:8],"\t",allbits[9:16],"\t",allbits[-1],"-->Right Shift")
	
	allbits.pop()

	return bin_dec(allbits)		


if __name__ == "__main__":
	
	while True:
		a = int(input())
		b = int(input())
	print("Product = ", booths_mul(a,b))
