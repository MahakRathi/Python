#2. Remove Duplicates from List

# Input: [1, 2, 2, 3, 4, 4]
# Output: [1, 2, 3, 4]

Input= [1, 2, 2, 3, 4, 4];
print(list(set(Input)));

Output=[];
for num in Input:
    if num not in Output:
        Output.append(num);
print(Output);