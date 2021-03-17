number = int(input('Insert number'))

i = number-1

while i>1:
    if number%i == 0:
        print(i)
    i = i-1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []
for i in a:
    for j in b:
        if i == j:
            if i in result:
                None
            else:
                result.append(i)
print(result)

s = str(input('Enter a string\n'))

if s == s[::-1]:
    print('Is a palindrome')
else:
    print('not a palindrome')

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = [i for i in a if i % 2 == 0]
print(even_list)

