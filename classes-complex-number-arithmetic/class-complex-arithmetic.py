import math
class ComplexNumberArithmetic:
    a = [0,0]
    b = [0,0]
    def __init__(self,a):
        self.a[0]=a[0]
        self.a[1]=a[1]
    def print_val(self,val1,val2):
        if val1 == 0 and val2 == 0:
            print("0.00")
        elif val2 == 0:
            print("%.2f" %(val1))
        elif val1 == 0:
            op2 = '' 
            if val2 < 0:
                op2='-'
            print("%s%.2fi" %(op2,abs(val2)))
        else:
            op2 = '+'
            if val2 < 0:
                op2 = '-'
            print("%.2f %s %.2fi" %(val1,op2,abs(val2)))
    #operator overloading
    def __add__(self,b):
        val1 = self.a[0]+b[0]
        val2 = self.a[1]+b[1]
        self.print_val(val1,val2)
    def __sub__(self,b):
        val1 = self.a[0]-b[0]
        val2 = self.a[1]-b[1]
        self.print_val(val1,val2)
    def __mul__(self,b):
        val1 = self.a[0]*b[0] - self.a[1]*b[1]
        val2 = self.a[0]*b[1] + self.a[1]*b[0]
        self.print_val(val1,val2)
    def div(self,a,b,c,d):
        val1 = (a*c + b*d) / (c*c + d*d)
        val2 = (b*c - a*d) / (c*c + d*d)
        self.print_val(val1,val2)
    def modulo(self,a,b):
        val = ((math.sqrt(pow(a,2)+pow(b,2))))
        print("%.2f" %(val))

        
a1,a2 = map(float,input().split())
b1,b2 = map(float,input().split())

# initializing the list
a = [a1,a2]
b = [b1,b2]

#declaring the objects
cmplxFunc = ComplexNumberArithmetic(a)

#operator over-loading
cmplxFunc+b   # complex numeber addition
cmplxFunc-b   # complex number subtraction
cmplxFunc*b   # complex number multiplication

cmplxFunc.div(a1,a2,b1,b2)
cmplxFunc.modulo(a1,a2)
cmplxFunc.modulo(b1,b2)
