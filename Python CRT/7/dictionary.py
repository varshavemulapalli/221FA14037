'''
Dict={101:'Python',102:'Java',103:'SQL',104:'Javascript'}
print(Dict)
print(type(Dict))
print(Dict[101])
'''
'''
stu={101:'Rahul',102:'Raj',103:'Sonam'}
fees={'rahul':2000,'raj':3000,'sonam':8000}
print(stu[101])
print(stu[102])
print(stu[103])
print(fees['rahul'])
print(fees['raj'])
print(fees['sonam'])
'''
'''
Eventcode={101:'Hackathon',102:'Coding',103:'Progject'}
print(Eventcode)
#modification
Eventcode[102]='Coding challenge'
print(Eventcode)
'''

JobRole={101:'Full Stack Developer',102:'Data Engineer',103:'Data Analyst'}
print(JobRole)
JobRole[105]='Cloud Engineer'
print(JobRole)
#more job roles pop
JobRole.pop(101)
print(JobRole) 
print(JobRole.keys())
print(JobRole.values())
print(JobRole.items())

'''
delete
person = {'city': 'guntur', 'age': '32', 'job': 'developer'}
#delete
del person['city']
print(person) #output:{'name':'john','age':'32','job':'developer'}
job=person.pop('job')
print(job)
print(person)
print(len(person))
print(person.items())
'''