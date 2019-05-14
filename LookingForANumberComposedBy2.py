#This program finds if one given number match the add of two numbers in a vector.

#We need a number: k
#We need a n lenght vector: [_,_,_..._]

k=11
AddVector=[1,6,8,3,10,5,3,8,5,2,9,16]
NumberOfForms=0

def CalculateLength(Vector):
	return len(Vector)
#Solution number one: Substracting one number in the vector to k. If one of the other number in the vector are similar, we have a solution.
for i in AddVector:
	Substraction=k-i
	for h in range(CalculateLength(AddVector)):
		#print (AddVector[h])
		if AddVector[h]==Substraction:
			NumberOfForms=NumberOfForms+1
		
Solution=NumberOfForms/2
print ("There are " + str(int(Solution)) + " forms to build " + str(k) + " with " + str(AddVector))	