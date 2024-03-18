#Create a function to input the weather in celcius and convert it to farenheit
user_input = int(input("Input celcius: "))
def celsius_to_farenheit(cel):
    return (cel * 9/5) + 32
print("Output farenheit: ",int(celsius_to_farenheit(user_input)))