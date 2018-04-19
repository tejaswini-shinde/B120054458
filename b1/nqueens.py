import json

def attack(board,n,r,c):
	for i in range(r):
		if board[i][c]==1:
			return True
	
	i=r-1
	j=c-1
	
	while(i>=0 and j>=0):
		if board[i][j]==1:
			return True
		i=i-1
		j=j-1
	
	i=r-1
	j=c+1
	
	while(i>=0 and j<n):
		if(board[i][j]==1):
			return True
		i=i-1
		j=j+1


def backtrack(board,n,row):
	i = 0
	
	while(i<n):
		if(not attack(board,n,row,i)):
			board[row][i]=1
			if(row==(n-1)):
				return True
			else:
				if(backtrack(board,n,row+1)):
					return True
				else:
					board[row][i]=0
		i=i+1
	
	if i==n:
		return False


def init_brd(size):
	return [[0 for x in range(size)] for x in range(size)]


def printboard(b,n):
	for i in range(n):
		for j in range(n):
			if(board[i][j]==0):
				print ".  ",
			else:
			   	print str(board[i][j])+"  ",
		print "\n"
		

if __name__ == '__main__':
	size = input("Enter the number of queens : ")
	board = init_brd(size)
	print "Initial Board"
	printboard(board,size)
	data = []
	with open('input.json') as f:
		data = json.load(f)
		
		if (data["start"] <0 or data["start"]>size):
			print "Invalid start position. Exitting"
			exit()
		
		board[0][data["start"]]=1
		
		if(backtrack(board,size,1)):
			print "Solution Found"
			printboard(board,size)
		
		else:
			print "No Solution exists"
			
			
