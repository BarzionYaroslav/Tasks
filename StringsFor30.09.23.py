print("CODE NUMBER 1")
string=input("Write a Sentence ")
print("Number of Words Is: "+str(len(string.split())))

print("CODE NUMBER 2")
string=input("Write a String ")
let=input("Write a Symbol to Swap ")
print("Changed String Is: "+string.replace(let,"😎"))

import collections
print("CODE NUMBER 3")
string=input("Write a String ")
print(collections.Counter(string))

print("CODE NUMBER 4")
f=open("voyna-i-mir-tom-1.txt")
w=open("Answer_for_strings.txt","w")
string=f.read()
ctring=string.split()
num={}
for i in ctring:
    num[i]=ctring.count(i)
w.write(str(num))
print("Find the Answer in 'Answer_for_strings.txt'")
w.close()
f.close()