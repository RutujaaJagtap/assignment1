print("Enter the First Number:")
number1=int(input())
print("Enter the Second Number:")
number2=int(input())
print("1.Addtion")
print("2.Subtraction")
print("3.Multipliaction")
print("4.Division")
print("Enter the choice:")
choice=int(input())
if(choice==1):
  print(number1+number2)
elif(choice==2):
  print(number1-number2)
elif(choice==3):
  print(number1*number2)
elif(choice==4):
  if(number1>=number2):
    print(number1/number2)
  else:
    print("Number1 must be greater than Number2")
else:
  print("Inavlid choice")