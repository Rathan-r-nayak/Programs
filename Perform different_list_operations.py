if __name__ == '__main__':
    n = int(input())
    li_in=[]
    li=[]
    for i in range(n):
        inp=input()
        li_in=inp.split()
        if(li_in[0]=="insert"):
            li.insert(int(li_in[1]),int(li_in[2]))
            
        elif(li_in[0]=="print"):
            print(li)
            
        elif(li_in[0]=="remove"):
            li.remove(int(li_in[1]))
        
        elif(li_in[0]=="append"):
            li.append(int(li_in[1]))
            
        elif(li_in[0]=="sort"):
            li.sort()
        
        elif(li_in[0]=="pop"):
            li.pop()
        
        elif(li_in[0]=="reverse"):
            li.reverse()
        
        li_in=[]



# Consider a list (list = []). You can perform the following commands:

#     insert i e: Insert integer 

# at position
# .
# print: Print the list.
# remove e: Delete the first occurrence of integer
# .
# append e: Insert integer

#     at the end of the list.
#     sort: Sort the list.
#     pop: Pop the last element from the list.
#     reverse: Reverse the list.

# Initialize your list and read in the value of
# followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list. 