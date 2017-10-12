# write a program that takes in letter grades
# and converts to find an average numerical grade

# counter-controlled
'''
# initialize variables (count, total)
count = 0
total = 0
numGrades = eval(input("How many grades would you like to enter? "))
print()

while count < numGrades:
    # use this line in your loop to take in a letter grade
    strGrade = input("Enter grade #" + str(count+1) + " ")
    # use if, elif, else to convert to number grade
    if(strGrade == "A"):
        total += 95
    elif(strGrade == "B"):
        total += 85
    elif(strGrade == "C"):
        total += 75
    elif(strGrade == "D"):
        total += 65
    else:
        total += 55
    
    # increment count
    count += 1

# after the loop, perform calculations
average = total / count
print("Average Grade: ",average)
'''

# sentinel-controlled
'''
# initialize variables (count, total)
count = 0
total = 0
strGrade = "A"
print()

while strGrade != "Z":
    # use this line in your loop to take in a letter grade
    strGrade = input("Enter grade #" + str(count+1) + " (enter Z if done) ")
    # use if, elif, else to convert to number grade
    if(strGrade == "A"):
        total += 95
    elif(strGrade == "B"):
        total += 85
    elif(strGrade == "C"):
        total += 75
    elif(strGrade == "D"):
        total += 65
    elif(strGrade == "F"):
        total += 55
    else: # if we get a Z we don't want count or total to change this time
        count -= 1
    
    # increment count
    count += 1

# after the loop, perform calculations
average = total / count
print("Average Grade: ",average)
'''

# user-controlled

# initialize variables (count, total)
count = 0
total = 0
cont = 'y'
print()

while cont == 'y':
    # use this line in your loop to take in a letter grade
    strGrade = input("Enter grade #" + str(count+1) + " ")
    # use if, elif, else to convert to number grade
    if(strGrade == "A"):
        total += 95
    elif(strGrade == "B"):
        total += 85
    elif(strGrade == "C"):
        total += 75
    elif(strGrade == "D"):
        total += 65
    else:
        total += 55

    cont = input("Continue? y/n ")
    
    # increment count
    count += 1

# after the loop, perform calculations
average = total / count
print("Average Grade: ",average)


