###### this is the second .py file ###########

####### write your code here ##########
def rot(lst,x):
    copy = list(lst)
    for i in range(len(lst)):
        if x<0:
            lst[i+x] = copy[i]
        else:
            lst[i] = copy[i-x]




group1 = list"abcdefghi"
group2 = list"jklmnopqr"
group3 = list"stuvwxyz_"
gr1=[]
gr2=[]
gr3=[]
gr1new=[]
gr2new=[]
gr3new=[]
a1,a2,a3 = list(map(int,input().split()))

word=input()
word_list = list(word)
print(word_list)


for i in range(0,len(word)):
    if word_list[i] in group1:
        gr1.append(word_list[i])
        gr1new.append(i)
       
    elif word_list[i] in group2:
        gr2.append(word_list[i])
        gr2new.append(i)
    elif word_list[i] in group3:
        gr3.append(word_list[i])
        gr3new.append(i)

rot(gr1,a1)
rot(gr2,a2)
rot(gr3,a3)

