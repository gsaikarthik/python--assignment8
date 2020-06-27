def check_equality(str1, str2):
    str = str1[8: :]
    print('String is ',str)
    if str == str2:
        print('Strings are equal')
    else:
        print('Strings are not equal')

str1 = "This is Python"
str2 = "Python"
check_equality(str1, str2)
