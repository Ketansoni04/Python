each object type has reference count 
the garbage collection does not occur immidiatly it waits for some time for any another reference so can take the same object
a = 5
a = a + 2
first python bring the references 5 + 2
compute and store in a new object 7
and give reference of this memory now a -> 7
garbage collect the unreferend memory object after some time