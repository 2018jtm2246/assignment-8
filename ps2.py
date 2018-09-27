###### this is the second .py file ###########

####### write your code here ##########
group1 = list("abcdefghi")
group2 = list("jklmnopqr")
group3 = list("stuvwxyz_")

gr1=[]
gr2=[]
gr3=[]
gr1new=[]
gr2new=[]
gr3new=[]
a1,a2,a3 = [int(i) for i in input().split()]

word=input()
list(word)

	for i in word[:]:
    		if i in group1:
        		gr1.append(i)
    		elif i in group2:
        		gr2.append(i)
    		elif i in group3:
        		gr3.append(i)

