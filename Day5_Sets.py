# Declaring Set - We cannot have duplicate in set, sets are mutable
a = {1,2,3,4,5,6}
print(a)
print(len(a))

b = {1,2,3,4,5,6,5,7,8,9,3,5,5,7,6}
print(b)
print(len(b)) # diuplicates will be removed

c= {1,100,20,40,20,50,80}

# We cannot index / slice a sets
# print(a[0])

# Membership operartor is possible in set
print(8 in a)

a.add(7) # we dint have method append in set.
print(a)

d = a.union(b) # {1,2,3,4,5,6,7,8,9}
print(d)

e = a.union(b,c)
print(e) #{1,2,3,4,5,6,7,8,9,100,20,40,50,80}

f = a.intersection(b) # Common elements
print(f) # {1,2,3,4,5,6}

g = a.intersection(b, c) # Common elements
print(g) # {1}


h = a.difference(b) # 'a' diff 'b' - non common elements of 'a'
print(h) # set()

x = {1,2,3}
y = {1,3,5}

# elements of x 
x.isdisjoint(y)

