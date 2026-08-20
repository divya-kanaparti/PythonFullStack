#FILE HANDLING
#step-1 open file
path=r"D:\Divya\Desktop\PythonFullStack\file.txt"
f=open(path,'r')
#step-2 write data to file
#override present data
f.write("Hello world")
l=["line1\n","line2\n","line3\n"]
f.writelines(l)
#to read data
print(f.readLine())
#step-3 cloase file
f.close
print("Written completed")
#Method-2
#here no need to close the file
with open(path,'r') as f:
    print(f.read())