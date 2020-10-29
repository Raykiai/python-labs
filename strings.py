# #Manipulating Strings
# fruit= 'banana'
# letter= fruit[1]
# print(letter)

# # 
# # 

# x=3
# w=[x-1]
# print(w)

# # 
# # 
# # lenght of string
# fruit= 'apple'
# x = len(fruit)
# print(x)


# # looping through strings
# fruit='banana'
# # iteration variable
# index=0 
# # while loop
# while index < len(fruit):
#  letter = fruit[index]
#  print(index, letter)
#  index= index+1

# # 
# # 
# # 
# # for loop
# # NB: iteration variable is taken care of by the for loop
# fruit ='grapefruit'
# for letter in fruit:
#     print(letter)


# # counts number of times loops encounters a 
# word = 'banana'
# count = 0
# for letter in word :
#     if letter == 'a' :
#         count= count + 2
# print(count)



# # Slicing Strings
# s = 'Monty Python'
# # excludes the second index number included: from- not including 
# print(s[0:4])
# print(s[6:7])
# print(s[6:20])
# # 
# # 
# s = 'Monty Python'
# print(s[2:])
# print(s[:8])
# print(s[:])

# # 
# # "in" is a logical expression that returns either true or false & is used in an if statement
# fruit='banana'
# if 'n' in fruit:
#  print('Found it !')
# else: print('Doesnt exist')

# # 
# # 
# # 
# word = input("fruit name ")
# if word == 'banana': 
#  print('All bananas are ripe!')

#  if word < 'banana':
#      print('Your word' + word + 'Comes after banana')
#  elif word > 'banana':
#         print('Your word' + word + 'Comes after banana')
#  else:
#        print('All right, they are  bananas')

# 
# # 
# # 
# # Prints all words as lower case
# greet = 'Hello Bob'
# zap = greet.lower()
# print(greet)
# print(zap)
# # lower() is a method
# # Short form of printing words in lower case
# print('Hi There' .lower())
# 
# # 
# # 
# # find() gets position of sub-string within string
# fruit = 'banana'
# pos = fruit.find('na')
# print (pos)
# aa= fruit.find('m') 
# print(aa)

# # 
# # 
# # 
# # Stripping Whitespace
# greet = ' Hello Bob '
# # lstrip removes whitespace from the left while rstrip removes whitespace from the right
# # strip removes from both sides
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# # 
# # 
# # 
# # Prefixes
# # display word/letter that starts or ends in string
# line= 'Please have a nice day'
# print(line.startswith('Please'))
# print(line.startswith('p'))
# print(line.startswith('P'))
# print(line.endswith('day'))
# 
# 
# 
# Parsing and extracting


