course = {"name":None,"duration":"1 month","tutor":"Sridhar","month":"Sep","mode":"online"}
fields = ["name","duration","tutor","month","mode"]

# for field in fields:
#     if field in course.keys():
#         if course[field] is not None:
#             print(course[field])
#         else:
#             print(f"{field} is none")
#             course.update({field:"Value not found"})
#     else:
#         print("course details not found")


list_courses = list(course.items())

index = 0

while(index<len(list_courses)):
    key, value = list_courses[index]
    if key in fields:
        print(f"{key} : {value}")
    index +=1