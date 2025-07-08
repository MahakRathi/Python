# Count Unique Words
# Input: "my name is mahak and my name is rathi"
# Output: 6 (unique words)
Input= "my name is mahak and my name is rathi";
words=Input.split();
unique_words=set(words);
count=len(unique_words);
print(count);
