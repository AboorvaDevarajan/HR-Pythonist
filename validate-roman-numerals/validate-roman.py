import re
exp = re.compile("^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
s = input()
if exp.match(s):
    print('True')
else:
    print('False')
