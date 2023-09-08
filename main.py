from matplotlib_venn import venn2, venn2_circles
from numpy import array
import element_input as el
import shading as vs
from matplotlib import pyplot as plt

for i in range(1):
    for j in range(80):
        print("-", end='')

print()
print("\t\tWELCOME TO SETT AND VENN DIAGRAM IMPLEMENTATION")
for i in range(1):
    for j in range(80):
        print("-", end='')

print()

print("Choose either one of the following: ")
print("1. Element Input")
print("2. Venn Shadng")
arr= array([1,2])
print()
mod= int(input("Enter choice here: "))

if(mod== arr[0]):
    el.Element_Input().User_Inp()
else:
    inp= input("Enter shading notation: ")
    vs.Venn_Shading().show(exp=inp)
