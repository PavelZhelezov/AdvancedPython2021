shifr={}
shifr[-1]=' '
j=0
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in alphabet:
   shifr[j]=i
   j+=1
st=str(input())
deshifr=''
bufer=''
flag=0
n=0
for i in st:
    if bufer=='End':
        break
    if i==' ':
        flag=1
    if flag==0:
        bufer+=i
    if flag==1:
        flag=0
        deshifr=deshifr+shifr[int(bufer)]
        bufer='' 
print(deshifr)
