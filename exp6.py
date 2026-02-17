# students in exams
cet = {"Noor", "Bob"}
jee = {"Hanif", "Bob"}
neet = {"Katif", "Eve"}
print("All students:", cet|jee|neet) #Union
print("Students in all exam:", cet & jee & neet) # intersection
print("Cet but not in jee:", cet - jee) #Difference
