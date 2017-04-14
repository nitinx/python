#  18 Mar 2017 | Determine if input string is a palindrome

str_in = input('Enter a String: ')
str_in = str_in.strip(' ')

#for chr in range(len(str_in)):
#    str_rev[chr] = str_in[(chr + 1) * -1]

str_rev = str_in[::-1]

print('Input String:', str_in)
print('Reversed String:', str_rev)

if str_in.capitalize() == str_rev.capitalize():
    print('Palindrome: Yes')
else:
    print('Palindrome: No')
