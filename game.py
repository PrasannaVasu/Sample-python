import random
import datetime
import time


print "Hello user. . .\nWelcome :)"

name=raw_input("\nPeople cal u as :")
r=random.randrange(1,5)
if r==1:
   print "\n\nSweet name ;) . . .\n"
elif r==2:
   print "\n\nLovely  name. . .\n "
elif r==3:
   print "\n\n---Nice name---\n"
elif r==4:
   print "\n\n+++Wonderful name+++\n"
else:
   print "\n\nVery kind of you\n"

dob=raw_input( "\nGive me your birth date(yyyy-mm-dd):")
year, month, day = map(int, dob.split('-'))
dob = datetime.date(year, month, day)
print "\n\nLet's find your age. . .\n"
age=datetime.datetime.now().year-year
print name,". . .Your age is ",age

bg=raw_input("\n\nBlood_group:")
blood = {'A+' :  'Donate blood to A+,AB+.Receive blood from A+,A-,O+,O-'  ,  'O+' :  'Donate Blood To O+, A+, B+,AB+.Receive blood from O+,O-' , 'B+' : 'Donate Blood To B+,AB+.Receive blood from B+,B-,O+,O-.' , 'AB+' : 'Donate Blood To AB+.Receive blood from everyone.' , 'A-' : 'Donate Blood To A+,A-,AB+,AB-.Receive blood from A-,O-.' , 'O-' : 'Donate Blood To everyone.Receive blood from O-.' , 'B-' : 'Donate Blood To B+,B-,AB+,AB-.Receive blood from B-,O-.' , 'B+' : 'Donate Blood To AB-,AB+.Receive blood from AB-,A-,B-,O-.'}
print blood[bg]

aim=raw_input("\n\nWhat's ur aim:")
c1=["Decide.Commit.Succeed" , "Dream of success" , "Work hard to achieve it" , "Nobody cares,Work harder"]
print random.choice(c1)

incident=raw_input("\nFantasy incident you like to happen. . .")
about=raw_input("\nWaiting for this moment??")


print "\n\n\nDETAILS OF ",name,"\nDate of Birth : ",dob,"\nAge : ",age,"\nBlood group : ",bg, "\nblood[bg]\nAim : ",aim,"\nFantasy incident : ",incident,"\nWaiting moment : ",about


print "\n\nFinally. . .Dare to be completed. . .",time.sleep(10)
comments =["Sing the alphabet without moving your mouth." , "Bark like a dog.","Say a dirty fantasy you would never actually do in real life." , "Mention the most annoying experience in some shopping." , "Have you fallen in love with a friend of your partner? Has anyone noticed?" , " Imitate one of your friends or one of your teachers at school." , "Go to the wall and talk to it like it is your boyfriend." , " Pretend you are Tarzan for two minutes."]
print random.choice(comments)


