'''
Project Euler problem #31
use recursion to check every possibility
to avoid extra checks, check in order
this is fast enough, but
to make even more efficeint, could save values (memoization)
'''

def coin_sum(possib_vals, up_to_i, sum_left):
	global total
	if(sum_left<0):
		return
	elif(sum_left==0):
		total+=1
	elif(up_to_i==0): #short_circuit
		if sum_left % possib_vals[0] == 0:
			total+=1
	else:
		while(up_to_i>=0 ):		
			coin_sum(possib_vals, up_to_i, sum_left - possib_vals[up_to_i] ) #xtra
			up_to_i -= 1

total = 0
pound_ar =[1,2,5,10,20,50,100,200]
coin_sum(pound_ar,len(pound_ar)-1,200);
print(total)


