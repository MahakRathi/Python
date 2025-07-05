#Write a Python program that takes temperature in Fahrenheit as input and converts it to Celsius 
Fahrenheit_String=input('enter a no. in fahrenheit: ');
Fahrenheit=float(Fahrenheit_String);
Celcius = ((Fahrenheit - 32) * 5)/9;
print("Farenheit converted into celcius" ,Celcius); 
