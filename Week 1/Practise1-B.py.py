#Assignment1 (abedalaziz khalaf)
# Question 1 (b)
x= float(input("Enter your number:"))
if x < -100:
    result= x*-1
elif -100 <= x and x <= -25 :
    result= x**4
elif 0 < x and x <= 100 :
    result= 22/14 *x + 3**x
else:
    result= x
print(result)
#Practise1-D
# If f(x) has to be an integer number, we should rewrite x as x=int(input("Enter your number:"))
