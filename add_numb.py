#This is a comment line
from adding import add_three

def add_two(a,b):
	print("adding 2 nums")
	return a+b

def main():
	print ("2+3=", add_two(2,3))
	print ("2+2+5=", add_three(2,2,5))

if __name__ == "__main__":
	main()
