from matplotlib_venn import venn3, venn3_circles
from numpy import array
from matplotlib import pyplot as plt


class Element_Input:
    """description of class"""
    def _init_(self):
        self.universal= None
        self.A= None
        self.B= None
        self.C= None
        self.AnBnC= None
        self.AnB= None
        self.AnC= None
        self.BnC= None


    def User_Inp(self):
        self.universal=int(input("Enter Universal set: "))
        self.A=int(input("Enter A value: "))
        self.B=int(input("Enter B value: "))
        self.C=int(input("Enter C value: "))
        self.AnBnC=int(input("Enter A and B and C value: "))
        self.AnB=int(input("Enter A and B value: "))
        self.AnC=int(input("Enter A and C value: "))
        self.BnC=int(input("Enter B and C value: "))

        self.Operation()

    def Operation(self):

        #if any of the intersections is greater than universal set,
        #generate an error
        if((self.AnB>self.universal) or (self.AnBnC>self.universal) or (self.AnC> self.universal)):
            print("Your intersection should not be greater than universal value!! ")
        elif((self.A>self.universal)):
            print("A set should not be greater than universal set")
        elif((self.B>self.universal)):
            print("B set should not be greater than universal set")
        elif((self.C>self.universal)):
            print("C set should not be greater than universal set")
        elif((self.AnB>self.AnB) or (self.AnBnC>self.AnC) or (self.AnC> self.BnC)):
            print("AnBnC should not be greater than either of the intersenctions")
        else:
            self.AnB-= self.AnBnC
            self.BnC-= self.AnBnC
            self.AnC-= self.AnBnC
            self.A-=(self.AnB+self.AnBnC+self.AnC)
            self.B-=(self.AnB+self.AnBnC+self.BnC)
            self.C-=(self.AnC+self.AnBnC+self.BnC)
            self.universal-=(self.A+self.B+self.C+self.AnB+self.BnC+self.AnC)

            self.Value_Put(self.A, self.B, self.C, self.AnB, self.BnC, self.AnC, self.AnBnC)

    def Value_Put(self, A, B, C, AnB, BnC, AnC, AnBnC):

        v=venn3(subsets=(A, B, AnB, C, AnC, BnC, AnBnC), set_labels=('A','B','C'))
        venn3_circles(subsets=(A, B, AnB, C, AnC, BnC, AnBnC))

        plt.show()
