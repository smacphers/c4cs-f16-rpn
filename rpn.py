#!/usr/bin/env python3

def calculate(myarg):
	print(myarg)

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()