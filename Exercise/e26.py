a='''
principle
<C_ADRESS>

<DATE>

Subject: Request for On-Duty Application for Two Days

Respected Sir,

I am <NAME>, a student of <CLASS> semester. 
I have been selected to participate in the State Level Athletic Competitions that is 
to be held on the 15th and 16th of this month at the M A Chidambaram Stadium, Chepauk.
I require an attested on-duty application to be able to represent the school and 
participate in the competitions. I request you to kindly provide me with a bonafide 
certificate and an on-duty application so that I would not lose my attendance.

Thanking you

Yours sincerely,

<NAME>
Semester <CLASS>
usn :<USN>
'''
print(a)
name=str(input("Enter the name:"))
sem=str(input("Enter the student SEMESTER:"))
usn=str(input("Enter the student usn:"))
date=str(input("Enter the date:"))
adress2=str(input("Enter the college adress:"))


a=a.replace("<NAME>",name)
a=a.replace("<CLASS>",sem)
a=a.replace("<USN>",usn)
a=a.replace("<C_ADRESS>",adress2)
a=a.replace("<DATE>",date)

print(a)
