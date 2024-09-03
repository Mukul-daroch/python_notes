# ________________________________________________________________________________________________
# Join Sets
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.
# ________________________________________________________________________________________________
# union()
# ____________________________
# Returns a new set that contains all elements from both sets. Duplicates are removed.
# Time Complexity: O(len(set1)+len(set2))
print("_______________________________________________0")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
set4 = set1.union(set2, set3)
# set1.union(set2) or set1 | set2
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
print(set4)  # 1=true

# ________________________________________________________________________________________________
# update()
# ____________________________
# Updates the set it is called on with elements from another set, effectively performing an in-place union.
# Time Complexity: O(len(set2)) # because it's modifying set1 in place, only the size of the second set matters.
print("_______________________________________________1")
set1, set2 = {4, 5, 6}, {1, 2, 3}
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
set1.update(set2)
# set1.update(set2) or set1 |= set2
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
print(set1)

# ________________________________________________________________________________________________
# intersection()
# ____________________________
# Returns a new set that contains only the elements that are present in both sets.
# Time Complexity: O(min(len(set1),len(set2))) #iterates through the smaller set and checks membership in the other set.
print("_______________________________________________2")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
set1.intersection(set2)
# set1.intersection(set2) or set1 & set2
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
print(set1)

# ________________________________________________________________________________________________
# difference()
# ____________________________
# Description: Returns a new set that contains elements that are in the first set but not in the second set.
# Time Complexity: O(len(set1)) – iterates through the first set and checks membership in the second set.
print("_______________________________________________3")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
result = set1.difference(set2)
# set1.difference(set2) or set1 - set2
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
print(result)
# ________________________________________________________________________________________________
# symmetric_difference()
# Description: Returns a new set that contains elements that are in either of the sets but not in both (i.e., elements that are unique to each set).
# Time Complexity: O(len(set1)+len(set2)) #must check all elements from both sets.
print("_______________________________________________4")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
result = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
# Usage: set1.symmetric_difference(set2) or set1 ^ set2
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
print(result)
print("________________________________________________")

# ________________________________________________________________________________________________
# Summary of Differences:
# ------------------------------------------------------------------------------------------------
# union()                      : Creates a new set with all elements from both sets.(the union of sets)
# update()                     : Adds elements from another set to the original set.(modifying it in place)
# intersection()               : Creates a new set with common elements between sets.(the intersection)
# intersection_update()        : Keeps only common elements in the original set.
# difference()                 : Creates a new set with elements unique to the first set.
# difference_update()          : Removes elements from the original set that are in the second set.
# symmetric_difference()       : Creates a new set with elements unique to either set.
# symmetric_difference_update(): Updates the original set with elements unique to either set.
# ________________________________________________________________________________________________
# Time Complexities:
# ------------------------------------------------------------------------------------------------
# union(), symmetric_difference(): O(len(set1)+len(set2))
# update()                       : O(len(set2))
# intersection()                 : O(min(len(set1),len(set2)))
# difference()                   : O(len(set1))
# intersection_update             : O(min(len(A), len(B)))
# difference_update               : O(len(B))
# symmetric_difference_update     : O(len(A) + len(B))

# These operations are efficient for typical set operations and modify the set in place, which helps to avoid creating new sets and thus saves memory.
