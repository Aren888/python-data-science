#Քառակուսի արմատ հաշվելու ալգորիթմ ՛Նյուտոնի մեթոդով։


def sqrt(x):
            #Նախ անհրաժեշտ է հայտարարել ենթադրյալ արմատը, ինչից հետո գրել,
            #քանի դեռ բավարար չենք մոտեցել արմատին,  նորից մոտենալ արմատին
    def sqrtIter(res):
        if guess_enough(res):
            return res
        else:
            return sqrtIter(improve(res))
            
    #improve-ը բարելավում է մոտարկումը, և բարելավված արդյունքը վերագրում է ենթադրյալ արմատին
    
    def improve(res):
        return average(res, x/res)
    
    def average(x, y):
        return (x+y)/2
        
    #Շեղման չափի ստուգում
    
    def guess_enough(res):
        if(abs(res**2-x)<0.001):
            return 1
        else:
            return 0
        
    return sqrtIter(1.0)

#       ստեղծել ֆունկցիա, որը հաշվում է թվի խորանարդ արմատը

def get_cube_root(x):
    cube_root = x**(1/3)
    return cube_root

'''
        Վարժություն 1.8
        n = ((m / (n ** 2)) + (2 * n)) / 3
        Այս բանաձևով ստեղծեք ֆունկցիա, որը հաշվում է թվի խորանարդ արմատը։
'''

def third_sqrt(n):
    res = 1
    while not guess_enough(res, n):
        res = improve(res, n)
    return res


def guess_enough(x, y):
    if abs(x ** 3 - y) < 0.0000000001:
        return True
    else:
        return False


def improve(n, m):
    return ((m / n ** 2) + (2 * n)) / 3


print(third_sqrt(10))

