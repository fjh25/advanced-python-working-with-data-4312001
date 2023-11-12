# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# Counter is a dectionary ; can use a key  


# TODO: How many students in class 1 named James?
print(c1["James"], "students named James in class 1")

# TODO: How many students are in class 1?
print(sum(c1.values()), "students in class 1")

# TODO: Combine the two classes
c1.update(c2)
print(sum(c1.values()), "students in class 1 after updating with class 2")

# TODO: What's the most common name in the two classes?
print(c1.most_common(3))

# TODO: Separate the classes again
c1.subtract(c2)  # c1.subtract(class2) works as well.
print(c1.most_common(1))

# TODO: What's common between the two classes?
#intersection of the two counters.
print(c1 & c2)  # result  ->  Counter({'James': 1, 'Frank': 1}) # not sure signficance of value to key (names)