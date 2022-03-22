'''

Վարժություն 1.11
f ֆունկցիան սահմանվում է հետևայլ կերպ.
f(n) = n, եթե n < 3
f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3
n-ը կարող է լինել միայն 0 և դրական ամբողջ թիվ։ Իրականացրեք լուծումը
ռեկուրսիվ, իտերատիվ և պոչավոր ռեկուրսիվ տարբերակներով։

'''


def is_int(x):  # Ֆունկցիան ստուգում է արդյոք թիվը ամբողջ է թե թչ
    temp = str(x)
    i = 0
    while i < len(temp):
        if temp[i] == '.':

            while i + 1 < len(temp):
                if temp[i + 1] != '0':
                    return False
                i += 1
            else:
                return True
        i += 1
    else:
        return True


def f_rec(n):  # rekursiv
    if is_int(n):
        if n < 0 :
            return 'Number less than 0'
        elif n < 3 :
            return n
        return f_rec(n - 1) + f_rec(n - 2) + f_rec(n - 3)
    else:
        return 'this number is not an integer'


def f_inter(n):   #  interativ
    if n < 0:
        return 'Number less than 0'
    else:
        a = 0
        b = 1
        c = 2
        if is_int(n):
            while n > 0:
                a, b, c = b, c, a + b + c
                n -= 1
            return a
        else:
            return 'this number is not an integer'

def f_poch_rek(n, a, b, c):   #   pochavor rekursia
    if n < 0:
        return 'Number less than 0'
    else:
        if is_int(n):
            if n == 0:
                return a
            else:
                return f_poch_rek(n - 1, b, c, a + b + c)
        else:
            return 'this number is not an integer'


'''
Վարժություն 1.12
Ստորև պատկերված աղյուսակը կոչվում է Պասկալի եռանկյունի (Pascal’s
triangle)
Եռանկյան կողմերում գտնվող բոլոր թվերը հավասար են 1-ի, իսկ եռանկյան
ներսում գտնվող թվերից յուրաքանչյուրը հավասար է նրա վերևի երկու թվերի
գումարին։ Գրեք ռեկուրսիվ ֆունկցիա, որը հաշվում է Պասկալի եռանկյունու
անդամի արժեքը
'''
#   [[1], [1, 1], [1, 2, 1]...]

num = int(input("Enter the number: "))
list1 = [] # դատարկ լիստ
for i in range(num):
  list1.append([])
  list1[i].append(1)
  for j in range(1, i):
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
  if(num != 0):
    list1[i].append(1)
for i in range(num):
  print(" " *(num - i), end = " ", sep = " ")
  for j in range(0, i + 1):
    print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")
  print()
