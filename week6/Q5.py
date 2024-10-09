print("Enter Name, RollNo., Marks of Students")
f = open('Marks.data','w+')
while(1):
    name = input("Enter name: ")
    rollNo = input("Enter RollNo.: ")
    marks = input("Enter Marks : ")

    f.write(name + "  " +rollNo + "  " +marks+"\n" )

    q = input("Quit? Enter Y/N : ")
    if(q=='Y' or q=='y'):
        break
#print(f.tell())
#f.seek(0)
#print(f.tell())
lines = f.readlines()
print(lines)
