# Return

def get_grade(marks, subject='unknown'):
    # print('subject=',subject)
    if marks >= 80:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'
        
grade=get_grade(75, 'maths')
print(grade)

#FIXME,TODO,XXX are used to mark the code
a=[1,2,3,4,5,6,7,8,9,10] # list
b=[]
for i in a:
        b.append(i)
b.append(11)

print(a)
print(b)

file=open('README.md')
print(type(file))
print(file.readline())

