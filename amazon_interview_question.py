# HW 5
# 4** Amazon interview question:
# Create a function that will take a string as an input
# and print the 1st unique letter of a string.
# "google" => l
# How would you test it? How would you handle edge cases?

def unique(string: str):

    string = string.lower()

    d = {}
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1



    for k, v in d.items():
        if v == 1:
            return k
    return ''


print(unique('google'))
print(unique('amazon'))


