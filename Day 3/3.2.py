#2. Count Vowels in a String

value=input("Enter the String: ");
Vowels="aeiouAEIOU";

count=0;
for char in value:
    if char in Vowels:
        count+=1;

print("Number of Vowels in ",value," :",count);
