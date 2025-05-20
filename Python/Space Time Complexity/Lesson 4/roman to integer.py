def romeToInt(romeInp):
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    result = 0
    
    for i in range(0, len(romeInp) - 1):
        if roman[romeInp[i]] < roman[romeInp[i+1]]:
            result -= roman[romeInp[i]]
        else:
            result += roman[romeInp[i]]
    
    return result + roman[romeInp[-1]]

romeNum = input("Enter roman number: ")
print(romeToInt(romeNum))