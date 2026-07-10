var1 = input("enter the first variable:")
var2 = input("enter the second variable:")

temp = var1
var1 = var2
var2 = temp

print("first variable after swap:",var1)
print("second variable after swap:",var2)