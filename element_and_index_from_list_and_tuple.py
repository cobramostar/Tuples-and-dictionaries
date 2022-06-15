# return all Werte and index for list

# Source code author cobrasathdtv@googlemail.com

# Find an index of duplicate elements in list Python Example

# How do you find the index of a duplicate element in a list

def readListElementAndIndex(mylist):

    duplicate_element = []

    for i,element in enumerate(mylist):
        counter = 1
        if element in duplicate_element:
            continue
        #print("")
        d = 0
        while mylist.count(element)>=counter and element not in duplicate_element:
            if counter==1:
                print(f"element {element} have index {mylist.index(element)}" , end = " ")
            else:
                d = mylist.index(element ,d) +1
                print(f"{mylist.index(element,d)}" , end = " ")
            counter +=1
        duplicate_element.append(element)
        print("")
        
        
 
foo = (8 , 1 , 2 , 3 , 1 , 2 , 3 , "a" , "b" , "c" , "a" , "b" , "c" , 1 , 2 , 3 , 1 , 2 , 3 , 21)

readListElementAndIndex(foo)



'''

>>> %Run Find_an_index_of_duplicate_elements_in_list_Python_Example.py

element 8 have index 0 
element 1 have index 1 4 13 16 
element 2 have index 2 5 14 17 
element 3 have index 3 6 15 18 
element a have index 7 10 
element b have index 8 11 
element c have index 9 12 
element 21 have index 19 
>>> 

'''
    

    
