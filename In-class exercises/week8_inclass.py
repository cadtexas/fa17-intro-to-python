'''
def match_words(words):

    count = 0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
    return count

def main():
    words=['abc','xyz','aba','1221']
    print(words)
    print(match_words(words))

main()


# Write a function to do the following:
# Take in word
# Make two separate lists for the consonants and vowels in word
# Report the number of consonants and vowels
# Report the "largest" letter (e.g. z > a)
def wordReport(word):
    vowel='aeiou'
    listc=[]
    listv=[]
    for let in word:
        if(let in vowel):
            listv.append(let)
        else:
            listc.append(let)
    largest=max(max(listv),max(listc))
    numc=len(listc)
    numv=len(listv)
    print(listc)
    print(listv)
    print("There are ",numc," consonants and ",numv," vowels in ",word,".")
    print("The largest letter is ",largest,".")

def main():
    wordList=['elephant','giraffe','anteater','snake']
    for word in wordList:
        print(word)
        wordReport(word)
        print("\n")
main()

'''
# Homework
# Write a function that takes in 2 pre-sorted lists and
# uses pop and append to transfer all elements of list2
# to list1. After the function,
# list1 should be sorted and contain all elements from both lists.
# list2 should be empty.
def mergeSorta(list1,list2):
    

# Write a function that takes in a list and pops any word
# whose first letter matches its position in the list.
# This function should account for movement in the list after pops.
# e.g. if we had the list ['apple','milk','bagel','dressing'], 
# since 'apple' is in the 1st position and 'a' is the 1st letter, 
# we pop 'apple'. Now the list is ['milk','bagel','dressing']. 
# 'milk' does not start with an 'a' so we move on. Then we pop 'bagel',
# leaving us with ['milk','dressing'].
def abridger(list1):
    abc='abcdefghijklmnopqrstuvwxyz'
    cont=True
    while cont:
        # complete this loop

def main():
    list1=['apple','milk','bagel','dressing']
    print("Before abridger:")
    print(list1)
    abridger(list1)
    print("After abridger:")
    print(list1)
    list2=['grapes','lettuce','juice']
    print("Before mergeSorta, list2:")
    print(list2)
    mergeSorta(list1,list2)
    print("After mergeSorta,\nlist1:")
    print(list1)
    print("list2:")
    print(list2)

main()
