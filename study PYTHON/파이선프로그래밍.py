# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
mylist = [ 23,78,43,11,94]
# 이 곳에 코드를 넣으세요
mylist2=[]
mylist3=[]
mylist2.append(mylist[2:3])
mylist2.append(mylist[1:4])
mylist2.append(mylist[:])

mylist3.append(mylist2[0][0])
mylist3.append(mylist2[1][0]+mylist2[1][1]+mylist2[1][2])
mylist3.append(mylist2[2][0]+mylist2[2][1]+mylist2[2][2]+mylist2[2][3]+mylist2[2][4])

print(mylist2)
print(mylist3)