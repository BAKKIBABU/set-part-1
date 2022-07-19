#  what is set set is represented by curlee braket{} but curlee braketcontains values but empty curly braket means dictionary
# if set all clear  the elements ofter then we get answer sett offf
# if all the clear elements in the dictionary ansswer get curlee braket {}
# set is immutable -> add$remove also
# sett is un orderlist


# and set is unorderable_list_difference
# a={}
# print(a,type(a))    # 'dict'
# a={4,5}
# print(a,type(a))     # class set
# b={1,1.2,'hello',('hi',2)}
# print(b,type(b))      #    class set
# a={1,3,5}
# print(a)
# a={10,20,30}
# print(a[1])     # 'set' object is not subscriptable
# b={2,3,5}
# print(b,type(b))   # class 'set'
# k=frozenset(b)
# a={1,2,3}
# b='hello',1,2,3
# a.add(b)         #1,2,3,'hello',1,2,3
# b.add(a)      # AtrributeError:'tuple' object has no attribute 'add'
# print(a)
# b={1,5,7}
# b.clear()
# print(b)    #set() set off
# what is intersectionn meaning 
# return the intersection off two sets as a new setall elements are in both sets 
# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
# print(a.intersection(b))    #  {3}
# print(a.intersection(c))      #  set offff set()
# print(a.intersection(d))      # {1}
# print(b.intersection(d))        #{4}
# a={1,2,3,'hello'}   # dublicate or multiple number is set that time one time only counted in both sett
# b={4,3,5,'hey'}
# print(a.union(b))    #{1,2,3,4,5,'hey','hello'}
# print(b.union(a))       # {1,2,3,4,5,'hey','hello'}
# a={1,2,3}
# b=['hello',1,2,3]
# a.add(b)
# print(a)   # {1,2,3,('hello',1,2,3)}
# a.add(b)
# print(a)          #typeError:unhashable type:list
# a={1,2,3}
# b={4,3,5}
# c={4,3,7}
# a.update(b)     # {1,2,3,4,5}
# a.update(c)        #{1,2,3,4,7}
# print(a)
# a={5,10,15,20,25,30}
# b={10,21,5}
# print(a.difference(b))    # {25,20,30,15}
# print(b.difference(a))   #21
# print(a-b)                 # {25,20,30,15}
# print(b-a)                   #{21}
# c={55,56,57,73,45,23}
# c.discard(44)
# print(c)   #same sett
# c.discard(73)
# print(c)        #{55,23,56,45,57}
# d={26,7,11,4,23}
# d.pop()
# print(d)     #{23,7,26,11}
# a={1,2,3,4}
# b={5,6,7}
# c={4,5,6}
# print('are a and b disjoint?',a.isdisjoint(b))    #true
# print('are a and c disjoint?',a.isdisjoint(c))      #false 
# print('are b and c disjoint?',b.isdisjoint(c))        #false