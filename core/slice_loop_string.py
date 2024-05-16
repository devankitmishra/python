# string1 = "Greetings, Earthlings"
# print(string1[0])   # Prints “G”
# print(string1[1:7]) # Prints “ting”
# print(string1[11:]) # Prints “Earthlings”
# print(string1[:5])  # Prints “Greet”


# ------------------------joining strings ------------------------------
# greetings = ["Hello", "world"]
# print(" ".join(greetings))  # Prints "Hello world"
# name = "Alice"

# print("Hello, " + name + "!")  # Prints "Hello, Alice!"


# ------------------------combine slicing and joining strings-------------------------
# def format_phone(phonenum):
#     area_code = "(" + phonenum[:3] + ")"
#     exchange = phonenum[3:6]
#     line = phonenum[-4:]
#     return area_code + " " + exchange + "-" + line

# print(format_phone("2025551212"))


# def greet_friends(friends):
#     for friend in friends:
#         print("Hi " + friend)

# greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli']) #it will greet all friends



# def greet_friends(friends):
#     for friend in friends:
#         print("Hi " + friend)

# greet_friends("Barry") # it will greet all alphabates in Barry



# nested for in loops
# for x in range(2):
#     print("This is the outer loop iteration number " + str(x))
#     for y in range(3+1):
#         print("Inner loop iteration number " + str(y))
#     print("Exit inner loop")


# for x in range(7):
#     if x % 2 == 0:
#         print(x)

# # The loop should print 0, 2, 4, 6

# # As a list comprehension:
# even_numbers = [x for x in range(7) if x % 2 == 0]  # way ot write a list of numbers
# print(even_numbers)


# print("*" * 8)

# input = "Four score and seven years ago"
# print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])
