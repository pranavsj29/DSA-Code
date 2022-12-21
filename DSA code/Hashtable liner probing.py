List=[]
print("enter no of elements to be insert")
number_of_element=int(input())
for i in range(number_of_element):
    c=int(input())
    List.append(c)
HashTable=[0]*len(List)
print(HashTable)
for i in range(len(List)):
    index=List[i]%len(HashTable)
    if HashTable[index]==0:
        HashTable[index]=List[i]
    else:
        for j in range(index+1,len(List)):
            if HashTable[j]==0:
                HashTable[j]=List[i]
                break
        else:
            for k in range (index):
                if HashTable[k]==0:
                    HashTable[k]=List[i]
                    break
print(HashTable)
print("enter value to be found")
a=int(input())
b=a%len(HashTable)
if HashTable[b]==a:
    print("value is found at index",b+1)
else:
    for j in range(b+1,len(List)):
        if HashTable[j]==a:
            print("element is found at index",j+1)
            break
    else:
        for k in range(b):
            if HashTable[k]==a:
                print("element found in index",k+1)
                break
                
            

            