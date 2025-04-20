class number:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
   
    def sum(self): 
        print(f'Sum of the 3 Numbers {self.num1} \n {self.num1 + self.num2 +self.num3}')        

Numbers =  number(    
    num1 = int(input('Enter num1: ')),
    num2 = int(input('Enter num2: ')),
    num3 = int(input('Enter num3: '))
)







