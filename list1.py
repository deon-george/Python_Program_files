'''students = {"hermonie":"griffindor",
            "harry": "griffindor",
              "ron":"griffindor",
            "draco":"sylsetherinn",
            }

print(students["hermonie"])
print(students["ron"])
print(students["draco"])
print(students["harry
for student in  students :
   print(student ,students[student], sep=", ")'''



students =[
    {"nme":"hermoninee","house": "gryyindor" ,"patronous": "otter" },
    {"nme":"harry","house":"gryffindor", "patronous":"stag"},
    {"nme":"ron","house":"gryffidor","patronous":"stag"},
    {"nme":"darco","house":"syllethein","patronous":None}
    
]
for student in students:
    print(student["nme"],student["house"],student["patronous"],sep=" ")