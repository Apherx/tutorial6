def f(x):
    y = float(-x**2 + 3*x -2)
    return y
#Q3
h = 0.1
g = 1
while  g <= 2.0000001:
    print(g)
    print("when x =",g,"f(x) = ",f(g))
    g = g + h

#Q4
first= f(1)
last = f(2)
print ("first height",first)
print("last height", last)

#Q5
sums = 0
for initial in [1.1, 1.2 , 1.3 , 1.4 , 1.5 , 1.6 , 1.7 , 1.8 , 1.9]:
    sums += f(initial)
print("Middle sum:",sums)

#Q6
Trapezium_Rule = (h/2)*((first) + (last) + (2*sums))
print("Integration is approximately:",Trapezium_Rule)

#Q7
print("True value of integration is 1/6")
Error_Percentage = (((1/6)-(Trapezium_Rule)) / (1/6)) * 100
if Error_Percentage < 0:
    Error_Percentage * -1
else:
    print("Error percentage is",Error_Percentage,"%")




