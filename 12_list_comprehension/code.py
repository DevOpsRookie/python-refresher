numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(numbers) # [1,3,5]
print(doubled) # [2,6,10]

# -- Dealing with strings --
# Useing for .. if loop .. but next one down pulls it into one line.

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))

# Output from above
#['Sam', 'Samantha', 'Saurabh']
#['Sam', 'Samantha', 'Saurabh']
#False
#friends:  140550452359232  starts_s:  140550454883264
