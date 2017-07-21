

# import csv
# import string
#
# # Open the CSV File and read it in.
# f = open('countries.csv')
# data = f.read()
#
# # Split the data into an array of countries.
# countries = data.split('\n')
#
# length = len(countries)
# print(countries[1])
# print(countries)
#
# # Start your search algorithm here.



countries=["Taiwan", "China", "Korea", "United States","Greenland", "Iran", "Japan", "Brazil", "Italy", "Angola"]
countries.sort()
length = len(countries)
print (countries)

midpoint = length//2
print(midpoint)
print(countries[midpoint])

country = input("What country would you like to search for?")

def els(countries, midpoint, length):
    if length == 2:
        if country == countries[0]:
            print("huzzah")
        elif country == countries[1]:
            print("huzzah")
        else:
            print("not in list")
    else:
        countries = countries[midpoint:midpoint*2]
        length = len(countries)
        if length == 2:
            if country == countries[0]:
                print("huzzah")
            elif country == countries[1]:
                print("huzzah")
            else:
                print("not in list")
        else:
            length = len(countries)
            midpoint = length//2
            print(countries)
            if country < countries[midpoint-1]:
                midpoint = midpoint//2
            elif country == countries[midpoint-1]:
                print("huzzah")
            else:
                return els

#first half
if country < countries[midpoint]:
    countries = countries[0:midpoint]
    print(countries)
    length = len(countries)
    midpoint = length//2
#If there isn't more

    if length == 1:
        if country == countries[midpoint-1]:
            print("huzzah")
        else:
            print("not in list")
    elif country < countries[midpoint-1]:
        midpoint = midpoint//2
    elif country == countries[midpoint-1]:
        print("huzzah")
    else:
        els(countries, midpoint, length)

        midpoint = midpoint//2
        print(countries[midpoint])
        #checking
        if country < countries[midpoint]:
            midpoint = midpoint//2
        elif country == countries[midpoint]:
            print("huzzah")
        else:
            countries = countries[midpoint:midpoint*2]
            check()

#midpoint
elif country == countries[midpoint]:
    print("huzzah")
#second half
else:
    countries = countries[midpoint + 1:midpoint*2+1]
    length = len(countries)
    midpoint = length//2
    #If there isn't more

    if length == 1:
        if country == countries[midpoint-1]:
            print("huzzah")
        else:
            print("not in list")
    elif country < countries[midpoint-1]:
        midpoint = midpoint//2
    elif country == countries[midpoint-1]:
        print("huzzah")
    else:
        els(countries, midpoint, length)









# def check():
#     midpoint = midpoint//2 -1
#     if country < countries[midpoint]:
#         check()
#     elif country == countries[midpoint]:
#         print("huzzah")
#     else:
#         countries = countries[midpoint:midpoint*2]
#         check()


#
# midpointWord = countries[midpoint]
# if country[0] <= midpointWord[0] :
#     midMidpoint = midpoint//2 -1
#     if the word is between a and mid mid point
#     else the word is between mid mid point and midpoint
#
#
# else #between Korea and Greenland



#     If the letter is greater than a but less than g
#         if the letter is or greater than a but less than d
#             if the letter is or greater than but <= b
#             else d or e
#         else between d and g
#
#
#     Else beteern g and m
#
#
#
# Else between m and z
