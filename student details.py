'''WAPP to read the following subjects’ marks and compute the average marks of a student
	Maths,English, computer, and science '''

student_name=input("enter student name")

maths=int(input ("Enter the marks of Maths: "))
science=int(input("enter science marks:"))
english=int(input("enter eng marks:"))
computer=int(input("enter comp marks:"))

avg =(maths+science+english+computer)/4;
print("student name :",student_name)
print(avg)




