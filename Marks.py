print("Enter marks obtained in for subjects")
Maths=int(input("Maths: "))
Arabic=int(input("Arabic: "))
Science=int(input("Science: "))
English=int(input("English: "))

sum=Maths+Arabic+English+Science
print("Marks of 4 subjects are: ", sum)
p=(sum/400)*100
print(end="Percentage= ")
print(p)
