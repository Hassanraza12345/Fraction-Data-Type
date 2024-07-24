class Fraction:
    def __init__(self,n,d):
        ''''
        n is numinator
        d is denuminator'''
        self.num=n
        self.den=d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        temp_num=self.den*other.num+other.den*self.num
        temp_den=self.den*other.den
        return '{}/{}'.format(temp_num,temp_den)
    def __sub__(self,other):
        temp_num=self.den*other.num-other.den*self.num
        temp_den=self.den*other.den
        return '{}/{}'.format(temp_num,temp_den)
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return '{}/{}'.format(temp_num,temp_den)



a=Fraction(12,4)
b=Fraction(14,6)
p=a+b
y=a-b
z=a*b
print('Addition',p,'\n Substraction',y,'\n Multiplication',z)