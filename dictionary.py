print("\t\tWelcome to Dictionary")
print("Abandon")
print("Crust")
print("Clock")
print("Table")
print("\n")
print("Note: Type the word as mentioned above!")
d1={"Abandon":"cease to support or look after (someone).",
"Crust":"the tough outer part of a loaf of bread.",
"Clock":"a mechanical or electrical device for measuring time, indicating hours, minutes, and sometimes seconds by hands on a round dial or by displayed figures.",
"Table":"a piece of furniture with a flat top and one or more legs, providing a level surface for eating, writing, or working at."}
print("Enter the word you want to search the meaning of : ")
n1=input()
b=n1.capitalize()
# print("\n")
print("The meaning of",n1," is : ",d1[b])

print("\n\t\tThank you for using our Dictionary")
