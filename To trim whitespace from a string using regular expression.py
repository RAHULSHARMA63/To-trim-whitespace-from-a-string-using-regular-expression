import re
my_string  = " Rahul Sharma "
output = re.sub(r'^\s+|\s+$', '', my_string)
print(output)