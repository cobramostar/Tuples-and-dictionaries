


# https://edube.org/quiz/pe-1/pe1-summary-test-1

# pe1-summary-test-1

from collections import defaultdict

foo = (1 , 2 , 3 , 1 , 2 , 3 , "a" , "b" , "c" , "a" , "b" , "c" , 1 , 2 , 3 , 1 , 2 , 3)

dictionary_list = defaultdict(list)

for i,element in enumerate(foo):
        dictionary_list[element].append(foo.index(element,i))
print("     " ,"element" ,"\t","index")        
for element, index in dictionary_list.items():
    print("\t" ,element ,"\t",index)
