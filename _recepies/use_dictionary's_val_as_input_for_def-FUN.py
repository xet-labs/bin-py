aamy = {
	  "Name": "Amy",
	  "Final Assessment": 74,
	  "Second Test": 72,
	  "First Test": 68
}

def show_grades(student,**grades):
    print("Student record for {}: ".format(student))

    for key, value in grades.items():
        print("{} earned a grade of {} in their {}.".format(student, value, key))

    print('\n',grades)


show_grades(aamy["Name"], SeeeecondTest=aamy["Second Test"])
print('\n')


show_grades(aamy["Name"], FiiiirstTest=aamy["First Test"], SeeeecondTest=aamy["Second Test"])








##-------tried to understand by self=>
reg={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    }
def naml(alphabet,**num):
    print('number for alphabet',alphabet,)
    for key,value in num.items():
        print('alphabet=',key,'--number=',value)
##-------tried to understand by self --END--


naml(reg['a'],aa=reg['a'],bbb=reg['b'],ccc='ee')
