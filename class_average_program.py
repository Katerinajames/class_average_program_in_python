
total=0

gradecounter=0
gradelist=[]
n=int(input("Enter the number of the grades you wish to append to your list \n"))


for i in range (1,n+1):
	grade=int(input("Please enter a grade\n"))
	gradelist.append(grade)   

print("------------------------------")
print("PRINTING GRADES ON THE SCREEN")

for grades in gradelist:
	  print(grades)
	  total=total+grades
    
print("------------------------------")
print("PRINTING THE GRADE AVERAGE ")
average=total/n

print ("The grade average is %.2f"%(average))
