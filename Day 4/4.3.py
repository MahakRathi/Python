#Find Union and Intersection of Two Lists
# Input: list1 = [1, 2, 3], list2 = [2, 3, 4]
# Output: Union: [1, 2, 3, 4], Intersection: [2, 3]
list1 = [1, 2, 3];
list2 = [2, 3, 4];
set1=set(list1);
set2=set(list2);
print(list(set1.union(set2)));
print(list(set1.intersection(set2)));
