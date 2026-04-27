amount=int(input("Please enter amount for withdraw (multiple of 10): "))

n1=amount//100
n2=(amount%100)//50
n3=((amount%100)%50)//10

print("100 dirham notes are: ", n1)
print("50 dirham notes are: ", n2)
print("10 dirham notes are: ", n3)