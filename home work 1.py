# Qs - 1
first = 7
second = 44.3
print(first + second) # result = 7+44.3=51.3
print(first * second) # result = 7*44.3=310.09999999999997
print(second / first) # result = 44.3/7=6.328571428571428

print("-----------------")

# Qs - 2
    # result: a=9!, b=8!, c=9+6=15!
# lets check if this is correct
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(a, b, c)

print("-----------------")

# Qs - 3
# no difference both are strings. strings can be in "" or ''. the importance is to keep all the code the same...


# Qs - 4
    # the issue here is that you can't print in the same line/concatenating a str! with int!
    # this is why one method is to do casting
    # so i can cast the integer as string
my_number = 5 + 5
print("result is: "+str(my_number))

print("-----------------")

# Qs - 5
    # the output should be 7
    # because the castig here changes the float into integer
    # means for 2.36 (float) to 2 (integer)
    # lets check it:
x = 5
y = 2.36
print(type(y))
print(x + int(y))

print("-----------------")

# Qs - 6
#fixing the code:
a = 8
b = "123"
print(a + int(b))
# or
print(str(a) + b)
# casting again...