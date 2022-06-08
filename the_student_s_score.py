
# https://edube.org/learn/pe-1/tuples-and-dictionaries-27

# 4.6.1.9 Korke i rječnici

# 4.6.1.9 Tuples and dictionaries

school_class = {}

while True:
    name = input("Enter the student's name: ")


    if name == "":
        break
    score = ()
    ocjena = 0
    while ocjena >= 0 or ocjena <=10:
        ocjena = int(input("Enter the student's score (0-10): or 11 for exit \n"))
        if ocjena == 11:
            break
        if ocjena not in range(0 , 11):
            ocjena = int(input("Enter the student's score (0-10): or 11 for exit \n"))
            if ocjena not in range(0 , 11):
                break
        
        score +=(ocjena , )
    
    if name in school_class:
        school_class[name] += (score , )
    else:
        school_class[name] = (score , )
        
print(school_class)        
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        for i in range(len(score)):
            print("len score" , len(score))
            print("i" , i )
            adding += score[i]
            print("adding" , adding)
            counter +=1
    print("adding" , adding , "couner" , counter)
    print(name, ":" , adding / counter)
    
