#Write a function in python fun_calc(num1, num2, operator) that receives 3 arguments (num1, num2 and operator). The first two arguments are operands (integers) and the third argument (character) that receives symbols of operators (+ (or) – (or) * (or) /). The function should calculate and return the result to the caller and the type of operation must be defined with the third argument. The function should also print the result and also the calculation process.
def fun_calc(num1,num2,operator):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return int(num1/num2)
print(fun_calc(10,5,"/"))