x = int(input('Enter a number: '))
x1 = int(input('Enter a number: '))
x2 = (input('Enter a number: (+,-,*,/,) '))
if x2 == '/' and x1 != 0:
    print(x/x1)
else:
    print('На нуль ділити не можна')
if x2 == '+':
    print( x + x1 )
elif x2=='-':
    print( x - x1 )
elif x2=='*':
    print( x * x1 )