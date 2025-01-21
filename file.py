st="hey thetere how are you "
f=open("my.txt", "w")
f.write(st)
f.close()

f=open("file.txt")
data=f.read()
print(data)
f.close()
