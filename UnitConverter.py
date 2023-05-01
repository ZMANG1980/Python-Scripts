#convert any unit to any unit... kind of

# the 3 apostropes are string formatting
menu='''
in the cm (ic)
cm to in  (ci)
Kg to g (kgg)
g to kg (gkg)
    which conversion?
'''
import random
from Conversion import*

user=input(menu)
#loop untill the user says quit whileuser says quite
while(user!="quite"):

#run that specific conversion
    if user=="ic":
        in2cm()
#run the in to cm function
    elif user=="ci":
    #run the cm to in function
        cm2in()
#ask the user which conversion?
    elif user=="kgg":
        kg2g()
    elif user=="gkg":
        g2kg()



user=input(menu)

