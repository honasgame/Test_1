def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
#i have used zip here because when i was scrolling from the help(dict) function  i found zip which would do the iteraion i wanted to do for this function but i was confused one how to do the iteration  so i used zip but if you think that i shouldn't had used this function please forgive me and give me another chance  

sum_1 = ["Virat","Rohit","Hardik"]
sum_2 = ["Kohli","Sharma","Pandya"]
sum_3 = ["Batsman","Batsman","Batsman"]
print(nested_dictionary(sum_1,sum_2,sum_3))