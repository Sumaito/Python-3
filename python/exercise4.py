#code that speaks the primitive type of the word and that says all the things in which it is linked or not
a = input ('Type something: ')
print('The primitive type of this value is: ', type(a))
b=('Only has uppercase letters: {}\nOnly has letters and numbers: {}\nOnly alphabetic: {}\nOnly digits: {}\nOnly has numbers: {}\nIt is a valid identifier: {} \nIt only has lowercase letters: {}\nIt is printable: {}\nIt only has spaces: {}\nEveryword has uppercase and lower case letters: {}'.format(a.isupper(),a.isalnum(),a.isalpha(),a.isdigit(),a.isnumeric(),a.isidentifier(),a.islower(),a.isprintable(),a.isspace(),a.istitle()))
print (b)
