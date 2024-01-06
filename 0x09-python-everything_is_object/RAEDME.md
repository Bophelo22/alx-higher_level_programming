0x09. Python - Everything is object

Tasks
0. Who am I?
- What function would you use to get the type of an object?

1. Where are you?
- How do you get the variable identifier (which is the memory address in the CPython implementation)?

2. Right count
- In the following code, do a and b point to the same object? Answer with Yes or No.

3. Right count =
- In the following code, do a and b point to the same object? Answer with Yes or No.

4. Right count =
- in the following code, do a and b point to the same object? Answer with Yes or No.

5. Right count =+
- In the following code, do a and b point to the same object? Answer with Yes or No.

6. Is equal
- What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

7. Is the same
- What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

8. Is really equal
- What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

9. Is really the same
- What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

10. And with a list, is it equal
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

11. And with a list, is it the same
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

12. And with a list, is it really equal
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

13. And with a list, is it really the same
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

14. List append
- What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

15. List add
- What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

16. Integer incrementation
- What does this script print?
def increment(n):
    n += 1

a = 1
increment(a)
print(a)

17. List incrementation
- What does this script print?
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

18. List assignation
- What does this script print?
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

19. Copy a list object
- Write a function def copy_list(l): that returns a copy of a list.

20. Tuple or not?

21. Tuple or not?

22. Tuple or not?

23. Tuple or not?

24. Who I am?

- What does this script print?
a = (1)
b = (1)
a is b

25. Tuple or not
- What does this script print?
a = (1, 2)
b = (1, 2)
a is b

26. Empty is not empty
- What does this script print?
a = ()
b = ()
a is b

27. Still the same?
- Will the last line of this script print 139926795932424? Answer with Yes or No.

28. Same or not?
- Will the last line of this script print 139926795932424? Answer with Yes or No.

29. #pythonic
- Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code)

30. Low memory cost
- Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

31. int 1/3
- Assuming we are using a CPython implementation of Python3 with default options/configuration

32. int 2/3
- Assuming we are using a CPython implementation of Python3 with default options/configuration:

33. int 3/3
- Assuming we are using a CPython implementation of Python3 with default options/configuration:
