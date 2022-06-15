


# return all Werte and index for list

# Source code author cobrasathdtv@googlemail.com

# Find an index of duplicate elements in list Python Example

# How do you find the index of a duplicate element in a list

def readListElementAndIndex(mylist):

    duplicate_element = []

    for i,element in enumerate(foo):
        counter = 1
        if element in duplicate_element:
            continue
        print("")
        d = 0
        while foo.count(element)>=counter and element not in duplicate_element:
            if counter==1:
                print(f"element {element} have index {foo.index(element)}" , end = " ")
            else:
                d = foo.index(element ,d) +1
                print(f"{foo.index(element,d)}" , end = " ")
            counter +=1
        duplicate_element.append(element)
        
        
 
foo = (8, 1 , 2 , 3 , 1 , 2 , 3 , "a" , "b" , "c" , "a" , "b" , "c" , 1 , 2 , 3 , 1 , 2 , 3 , 21)

readTupleElementAndIndex(foo)
