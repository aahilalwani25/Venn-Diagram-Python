from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from numpy import array
from matplotlib import pyplot as plt

class Venn_Shading:
    
    def __init__(self):
        self.A=1
        self.B=2
        self.C=3
        self.AandB=4
        self.AandC=5
        self.BandC=6


    def show(self, exp):
        
        #if we get A and B in that string
        if ("A" in exp) and ("B" in exp):
                #if we found union symbol in the string
                if 'u' in exp:
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('red')
                    v.get_patch_by_id('01').set_color('red')
                    v.get_patch_by_id('11').set_color('red')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('white')
                    plt.gca().set_axis_on()
                if 'n' in exp:
                    #this is for interssection
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('white')
                    v.get_patch_by_id('01').set_color('white')
                    v.get_patch_by_id('11').set_color('red')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('white')
                    plt.gca().set_axis_on()

        #this is for complements
        # (A n B)'= A' u B'
        if (("A\'" in exp) and ("B\'" in exp)) or(("(AnB)\'" in exp)) or (("(AuB)\'" in exp)):

                if ("(AnB)\'" in exp) or ("A\'uB\'" in exp):
                    # (A n B)'= A' u B'
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('blue')
                    v.get_patch_by_id('01').set_color('blue')
                    v.get_patch_by_id('11').set_color('white')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('blue')
                    plt.gca().set_axis_on()
                else:
                    # (A u B)'= A' n B'
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('white')
                    v.get_patch_by_id('01').set_color('white')
                    v.get_patch_by_id('11').set_color('white')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('blue')
                    plt.gca().set_axis_on()
                    
        if (("A\'" in exp) and not("B\'" in exp))or("B-A" in exp):
                #A'nB= B-A
                if ("n" in exp) or("B-A" in exp):
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('white')
                    v.get_patch_by_id('01').set_color('red')
                    v.get_patch_by_id('11').set_color('white')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('white')
                    plt.gca().set_axis_on()

                else:
                    #A'U B
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('white')
                    v.get_patch_by_id('01').set_color('blue')
                    v.get_patch_by_id('11').set_color('blue')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('blue')
                    plt.gca().set_axis_on()

                    
        if (not("A\'" in exp) and ("B\'" in exp)) or("A-B" in exp):
                #AnB'= A-B
                if 'n' in exp or("A-B" in exp):
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('red')
                    v.get_patch_by_id('01').set_color('white')
                    v.get_patch_by_id('11').set_color('white')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('white')
                    plt.gca().set_axis_on()

                else:
                    #AUB'
                    v=venn2(subsets=(self.A, self.B, self.AandB), set_labels=('A','B'), alpha=0.8)
                    v.get_patch_by_id('10').set_color('blue')
                    v.get_patch_by_id('01').set_color('white')
                    v.get_patch_by_id('11').set_color('blue')
                    venn2_circles(subsets=(self.A, self.B, self.AandB))
                    plt.gca().set_facecolor('blue')
                    plt.gca().set_axis_on()
        
        plt.title("VENN DIAGRAM")
        plt.show()
