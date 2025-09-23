set={1,2,2,4,3,"Hello","Hello","World"}
print(set)
#store the duplicated value once and print in not a sorted manner as set values are not bound by an index
#and all values store in set must be im mutable

set.add(10)#it will add an elemnt in the set
set.add("yoyoyo")
print(set)

set.remove("yoyoyo")#remove he elment
print(set)

set.pop()#it will remove a random element
print(set)

set.clear()#clear every element from the set
print(set)

set1={1,2,3,4,3,2,1,5,6,7}
set2={4,3,2,1,1,}
#its basic math union and intersaction so google it dumbo!!!!!
print(set1.union(set2))
print(set1.intersection(set2))
