'''
dictionary{}
-------------
keys(),values(),items()
key value pair
duplicate keys are not allowed
ordered
'''

#mark={}
#print(type(mark))

phone_numbers={
"akshay":987,
"sarath":123,
"akhil":456
}

print(phone_numbers)
print(phone_numbers['akshay'])
phone_numbers ["akshay"]=888
print(phone_numbers)


#funtions
#--------
'''
get(key_name)
-------------
to get key value'''

print(phone_numbers.get("sarath"))

'''
update({key_value})
-------------------
to change key value'''

phone_numbers.update({"sarath":999})
print(phone_numbers)

# to add new item or key
#-----------------------
phone_numbers["den"]=555
print(phone_numbers)

phone_numbers.update({"ben":755})
print(phone_numbers)

#del,clear()
#---
del phone_numbers['sarath']
print(phone_numbers)

phone_numbers.clear()
print(phone_numbers)

#del phone_numbers
print(phone_numbers)

#pop(),popitem()
#---------------


roll_numbers={
1:"anand",
2:"benison",
3: "hafeed"
}
roll_numbers.pop(2)
print(roll_numbers)
roll_numbers.popitem()
print(roll_numbers)
roll_numbers.clear()
print(roll_numbers)

#keys()
#------
print(roll_numbers.keys())

#values()
#------
print(roll_numbers.values())

#items()
#-------
print(roll_numbers.items())
#------------------------------------------

roll_numbers={
1:"anand",
2:"benison",
3: "hafeed"
}

for i in roll_numbers:
    print(i) #key
print(roll_numbers[i]) #value

for i in roll_numbers.keys():
    print(i)
for i in roll_numbers.values():
    print(i)
for i in roll_numbers.items():
    print(i)
for i,j in roll_numbers.items():
    print(i,j)

#------------------------------------------
#merging
#------

#zip()
# to make an object and convert that object to any data type
#-----------------------------------------------------------
'''
subject=[]
marks=[]
for i in range(5):
    sub=input("enter your subject name:")
    mark=int(input("enter your mark:"))
    marks.append(mark)
print(subjects)
print(marks)


subjects=["physics", "maths", "biology", "chemistry"]
marks=[35,45,50,33,15]
#zip()
mark_sheet=dict(zip(subjects,marks))
print(mark_sheet)
'''
#-----------------------------------------------------------------------
'''
A+ 91-100
A 81-90
B+ 71-80
B 61-70
C 51-60
D 41-50
F BELOW 40

'''
#{'anand': 'A+', 'akhil': 'A', 'benison': 'B+', 'cep':B', 'hafeed': 'C', 'jithin': 'D', 'nithin': 'F'}

students_marks={
"anand":92,
"akhil":84,
"benison": 74,
"cenoy":64,
"hafeed": 55,
"jithin":42,
"nithin":28
}

subjects=["anand", "akhil", "benison", "cep",'hafeed','jithin','nithin']
marks=['A+','A','B+','B','C','D','F']
#zip()
mark_sheet=dict(zip(subjects,marks))
print(mark_sheet)












