message = input("Enter a message: ")
distance = int(input("Enter distance value: "))
result = ""
for x in message:
    result += chr(ord(x)+distance)
print(""+result)
