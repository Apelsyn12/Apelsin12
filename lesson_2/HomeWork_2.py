Q1 = int(input("Enter a number"))
import string
B1 = (Q1%10)
B2 = ((Q1%100)//10)
B3 = ((Q1%1000)//100)
B4 = ((Q1%10000)//1000)
B5 = ((Q1%100000)//10000)
Main = (str(B1) + str(B2) + str(B3) + str(B4) + str(B5))
print(Main)