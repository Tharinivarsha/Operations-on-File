#Activity 3
file1=open("codingal.txt","r")
file2=open("updatedcodingalfile.txt","w")

for line in file1.readlines():
    if not(line.startswith("Coding")):
        print(line)
        file2.write(line)

file1.close()
file2.close()