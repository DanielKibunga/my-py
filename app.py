
students_count = 100

## this is an integer ## class "int"



rating = 4.99 

## this is a float as in decimal number in python ## class "float"



name = "Daniel" 

 ## this is a string 
 # ## class 'str'


is_student = True 

## this is a boolean true or false
#  ## MUST  ALWAYS START WITH CAPITAL LETTERS 
#  ## clas 'bool'

course = "    python programming"
###print(len(course))

## this is a function 
# ## we use parenthesis as in like we are calling this function()
# ##this particular one shows the total number of characters of the argument or variable in this case 20(space is also counted)
##print is like console.log

###print(course [-19])

##to get to a specific character in the string we use the square brackets notation
## it always strats count from 0 like always so n-1
## when using negative values you it starts from the back -1 being the last character
##using a similar syntax we can slice a string


######print(course [0:3])


## we have extracted only the first three characters
## this returns the first three characters 0,1,2 not 3 'pyt'
## if we do only the starting index [0:] it will show the whole thing "Python Programming" also happens if we dont give it any index [:]
## if we only include the ending index [:3] it will show from the start to where the index ends "Pyt"

first = "Daniel"
last = "Kimani"
full = f"{len(first)} {last}"
##print(f"{"Good morning"} {full}")

## using f"" you must use curly braces{} to add a variable## also use space between multiple variables ## use "" when adding a string like print(f"{"Good morning"} {full}") variables dont need the quotes .....you can also add functions like len 
# full = f"{len(first)} {last}"]
# 
#  print(f"{"Good morning"} {full}")  
# this is returned - Good morning 6 Kimani


##print(course.title())
## we have accessed the course variable and changed it using the dot notation ....so the function is course.upper()...changes the letters to upperscase and lower case if you use .lower().. the methods that we call here return a new string and the original string is not affected
##print(course.strip()) removes any unnecessary spaces
print(course.find("pyt")) ## returns the index of what ur lookin for
print(course.replace("p", "j"))

print("pro" in course)  ### this will show you whether the letters sre there are not true or false


###numbers or integers

print (10 + 3) 
print (10 - 3)
print (10 * 3)
print (10 / 3)    ###division
print (10 // 3)  ## will give you rounded up to nearest number
print (10 % 3)  ## 10 divided by 3  = 9 remainder 1
print (10 ** 3) ## this is like 10 cubed as in 10^3