#a has the string type with the text (int) but it is not set as int.
a = 'int'
print(f"Value a type: ",type(a));

#b has the int type
b = 7
print(f"Value b type: ",type(b));

#c has the boolean statements
c = False
print(f"Value c type: ",type(c));

#d has the string type with the text (18.5) but it is not set as float.
d = "18.5"
print(f"Value d type: ",type(d));


#The float(d) converts the string to float type
x = b+float(d);
print(f"Value x type: ",type(x));

#This prints the value of x which already b + float(d) from above
print(f"{x}");