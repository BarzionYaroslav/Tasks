import requests #---------TASK NUMBERO UNO----------
print("Our trip is startin' on task number 1. Be ready. That is a long trip")
link = requests.get("https://habr.com/ru/articles/top/weekly/")
con=link.content
str=con.decode("utf-8")
fi=str.find("<h2")
while fi>-1:
    ei=str.find("</h2",fi)
    substr=str[fi:ei]
    fii=substr.find('<a href="/ru')
    while fii>-1:
        eii=substr.find('data-test-id=',fii)
        subsubstr=substr[fii:eii]
        num=subsubstr[-9:-3]
        zelda=requests.get("https://habr.com"+subsubstr[9:-3])
        f=open(num+".html","w",encoding="utf-8")
        f.write(zelda.text)
        f.close()
        fii=-1
    fi=str.find("<h2",ei)
print("We are going to task number 2! Hold your hats tight!")
#---------TASK NUMBERO DOS----------
link=requests.get("https://jsonplaceholder.typicode.com/posts/")
json=link.json()
f=open("titles.txt","a",encoding="utf-8")
f.truncate(0)
for i in range(len(json)):
    f.write(json[i]["title"]+"\n")
f.close()
print("Okay, Our trip to task 2 is done")