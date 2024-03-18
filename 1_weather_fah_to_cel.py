#Create a function to input the weather in farenheit and convert it to celcius
user_input = int(input("Input farenheit: "))
def fahrenheit_to_celsius(farenheit):
    return  (farenheit - 32) * 5/9
print("Output celcius: ",int(fahrenheit_to_celsius(user_input)))