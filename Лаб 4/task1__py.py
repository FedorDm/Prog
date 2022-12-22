stud = []
stud1 = ["Sam", "man", "hor"]
stud.append(stud1)
stud2 = ["Tom", "man", "otl"]
stud.append(stud2)
stud3 = ["Yana", "woman", "tri"]
stud.append(stud3)
stud4 = ["Dasha", "woman", "hor"]
stud.append(stud4)
for k in range(3):
    if stud[k][1] == "man" and (stud[k][2] == "otl" or stud[k][2] == "hor"):
        print(stud[k][0], "Molodec!!!")