


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

'''

>>> %Run pe1_summary_test_1_Item_2_35_tuple_index_default_dictionary.py
      element 	 index
	 1 	 [0, 3, 12, 15]
	 2 	 [1, 4, 13, 16]
	 3 	 [2, 5, 14, 17]
	 a 	 [6, 9]
	 b 	 [7, 10]
	 c 	 [8, 11]
>>> 

'''
