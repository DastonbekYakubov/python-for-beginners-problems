# A(x1,y1) B(x2,y2) C(x3,y3)
import math
print("Uchburchakning uchlari koordinatalarini mos ravishda kiriting:")
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
x3=int(input("x3="))
y3=int(input("y3="))
AB=math.sqrt((x2-x1)**2+(y2-y1)**2)
BC=math.sqrt((x3-x2)**2+(y3-y2)**2)
CA=math.sqrt((x3-x1)**2+(y3-y1)**2)
p=(AB+BC+CA)/2
S=math.sqrt(p*(p-AB)*(p-BC)*(p-CA))
print("Uchburchak perimetri: ",2*p,"ga,\n Yuzasi: ",S)