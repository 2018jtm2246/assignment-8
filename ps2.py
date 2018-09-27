
def rot(x1,x2):       #rot function is defined here for rotation
    copy = list(x1)
    for i in range(len(x1)):
        if x2<0:
            x1[i+x2] = copy[i]
        else:
            x1[i] = copy[i-x2]



group1="abcdefghi"   #Creating 3 groups
group2="jklmnopqr"
group3="stuvwxyz_"

gr1 =[]
gr2 =[]
gr3 =[]
gr1new=[]
gr2new=[]
gr3new=[]


a1,a2,a3 = list(map(int,input().split()))   #geting the key value from user


word = input()   #geting the string
word_list = list(word)



for i in range(0,len(word)):   #now compairing g1 in string and copy similaar char into s1
	if word_list[i] in group1:
		gr1.append(word_list[i])
		gr1new.append(i)
		
	elif word_list[i] in group2:
	    gr2.append(word_list[i])
	    gr2new.append(i)
	elif word_list[i] in group3:
	    gr3.append(word_list[i]) 
	    gr3new.append(i)




rot(gr1,a1)   #rotating  gr1,gr2,gr3 by calling rot function
rot(gr2,a2)
rot(gr3,a3)




x=y=z=0
for i in range(0,len(word)+1):     #geting back the decrypted word
	if i in gr1new:
		word_list[i]=gr1[x]
		x+=1
	elif i in gr2new:
		word_list[i]=gr2[y]
		y+=1
	elif i in gr3new:
		word_list[i]=gr3[z]
		z+=1	


for i in word_list[:]:
	print (i, end ='')

print("")
