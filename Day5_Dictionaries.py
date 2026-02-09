# Declaration of Dictionaries
points = {"a": 1, "b": 2, "c": 3, "d": 4 }
print(points)
print(points["a"])

# Iterating Dictionary using for loop
for key, value in points.items():
    print(f"{key},{value}")


tempratures = {"banglore": (1 , 2), "chennai":(2,4)}

print(tempratures["banglore"])
# Dictionary lookup for missing element
# print(tempratures["kolkata"])  # we will get KeyError: 'kolkata'

for temps in tempratures.values():
    print(temps)


locations = {"country": "India", "states": ["karnataka", "andrapradesh","chennai"]}

# Dictionary lookup for list inside a dictionary
print(locations["states"][1])

prices = {"IBM": {"low" : 24, "high": 43},"HP": {"low" : 25, "high": 45}}
print(prices["IBM"]["low"])

# Reassigning -1 
prices["IBM"]["low"] = prices["IBM"]["low"]+1
print(prices["IBM"]["low"])

# Reassigning -2
prices["IBM"]["low"] = 28
print(prices["IBM"]["low"])

# adding to a dictionary
prices["GOOGLE"] = {"low" : 28, "high": 48}
print(prices)

# Note:-
# We cannot make a mutable objects (List) as a key
# We can make a immutable objects (str, int, tuple) as a key

# Occurance of Characters 
# Approach -1
sentence = "hello world hello world welcome to python"

words = sentence.split()
word_count_pair = {}
for word in words:
    word_count_pair[word] = words.count(word)

print(word_count_pair)

# Approach -2
sentence2 = "hello world hello world welcome to python"
words2 = sentence2.split()
word_count = {}
for word2 in words2:
    if word2 in word_count:
        word_count[word2] = word_count[word2]+1
    else:
        word_count[word2]=1

print(word_count)
