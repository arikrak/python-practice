#wrote code to print all permutations of a string
#modified it so it solves Project Euler problem #24 (though it can be solved by hand also)

num=0

def permute(prev_str, str):
	global num
	if(len(str) == 0 ):
		num +=1
		if(num==1000000):
			print(prev_str)
	else:
		for i in range(len(str)):
			permute( prev_str+str[i], str[:i] + str[i+1:])	

permute("", "0123456789")
#permute("", "abcde")























