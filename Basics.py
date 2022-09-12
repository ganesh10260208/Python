#Python 
print("Hello World")

#This is a comment
"""This is also a comment"""

#DataTypes--->str,int,float,complex,list,tuple,dict,bool
#strings---->slicing,index,upper(),lower(),x.strip()y.replace('1','2'),\",len(),find()
#boolen--->True,False,0,None
#Operators---->Arthmetic(+-*%/**//),Assignment(=,+=,=+),Comparision(==,!=,<,>=)
                #Logical(and,or,not),Identity(is, isnot),Membership(in,notin),
                #Bitwise(&,|,^,<<,>>)
import random
print(random.randrange(1,10))


x=1
X=2
y="DG"
Y="tdg"
a1,a2,a3=int(3),str(3),float(3)

print(x,y,y[1],Y[0:1],X,Y,a1,a2,a3)
print(type(a1))

#if
if(x>X):
    print("x is greater")
elif(x==y):
    print("Equal")
else:
    print("X is greater")

#loops--->while and for ---->Break,continue,pass

#list--->a.append().insert().extend(b).remove(a1).pop(),del,a.clear().sort(reverse=True/False)
        #key,.copy().count()
list1=[1,2,3,4,5,6,7,8,9,0]
list2=[ab for ab in range(10)]

#tuple--->len,type
tuple1=(1,2,3,4,5,6,7,8,9,0)

#set--->not ordered,add,a.update(b),remove,.discard(a1),pop,clear,del,a.union(b)
set1={1,2,5}
#dict--->len,a.keys().values().items().update().pop(k1)popitem(),del,.cleear,.copy,
dict1={"k1":"v1","k2":"v2"}


#NESTED***

print(list1,list2,tuple1,set1)

def DurgaGanesh(argument1="Default1"):
    global g
#lambda(only one argument)
DurgaGanesh()
