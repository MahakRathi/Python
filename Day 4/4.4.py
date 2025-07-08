# Swap First and Last Element in a Tuple

# Input: (1, 2, 3, 4)
# Output: (4, 2, 3, 1)

Input1=(1, 2, 3, 4);
Input=list(Input1);
Input[0],Input[-1]=Input[-1],Input[0];
Input1=tuple(Input);
print(Input1);