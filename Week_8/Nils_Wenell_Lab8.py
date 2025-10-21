"""
Your Name
Lab 8
Adv Functions 
"""




#Problem 1
#replace this line with your calc_toll function from part 1.




def calc_toll(hour,am=True,weekend=False):
    toll = 0.0
    if weekend == False:
        if am == True:
            if hour<7:
                toll=1.15
            elif hour<10:
                toll=2.95
            else:
                toll=1.9
        else:
            if hour<3:
                toll=1.9
            elif hour<8:
                toll=3.95
            else:
                toll=1.1
    else:        
        if am == True:
            if hour<7:
                toll=1.05
            else:
                toll=2.15
        else:
            if hour<8:
                toll=2.15
            
            else:
                toll=1.1
    return toll


def calc_weekly_toll(begin_work, end_work, in_office_days, weekend_emp):
	#hint: remember each employee needs to travel to and from work.
	#your code here
    weekdaytoll = ((calc_toll(begin_work-1))+(calc_toll(end_work+1,False)))*in_office_days
    weekendtoll=0
    if weekend_emp == True:
        weekendtoll = ((calc_toll(begin_work-1,True,True))+(calc_toll(end_work+1,False,True)))*2
    return weekendtoll+weekdaytoll


'''
These are the test cases
Do not modify any of the below code.
Look at the console to see if you answers are correct.
Use comments if you want to check cases one by one.
'''


def test_solution(fctn_value, actual_value):
	return abs(fctn_value - actual_value) < 0.0000000001

#Frank works from 8am to 5pm Monday through Friday.
weekly_toll = calc_weekly_toll(8,5,5,False)
if(test_solution(weekly_toll, 34.50)): 
	print(f"Frank's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Frank's weekly toll should be $34.50, but you got ${weekly_toll:.2f}")


#Annus works from 8am to 1pm Monday through Friday.
weekly_toll = calc_weekly_toll(8,1,5,False)
if(test_solution(weekly_toll, 24.25)): 
	print(f"Annus' weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Annus' weekly toll should be $24.25, but you got ${weekly_toll:.2f}")


#Vivian works from 8am to 5pm Monday, Wednesday, Friday.
weekly_toll = calc_weekly_toll(8,1,2,False)
if(test_solution(weekly_toll, 9.70)): 
	print(f"Vivian's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Vivian's weekly toll should be $9.70, but you got ${weekly_toll:.2f}")


#Rami works every weekend from 6am to 6pm Monday, Wednesday, Friday.
weekly_toll = calc_weekly_toll(6,6,2,True)
if(test_solution(weekly_toll, 6.40)): 
	print(f"Rami's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Rami's weekly toll should be $6.40, but you got ${weekly_toll:.2f}")


#Sue works 6am to 6pm Monday, Wednesday, Friday.
if(test_solution(calc_weekly_toll(6,6,3,False), 15.30)): 
	print(f"Sue's weekly toll of ${calc_weekly_toll(6,6,3,False):.2f} is correct")
else:
	print(f"Sue's weekly toll should be $15.30, but you got ${calc_weekly_toll(6,6,3,False):.2f}")


#Zijia works from 8am to 5pm Monday through Friday.
weekly_toll = calc_weekly_toll()
if(test_solution(weekly_toll, 34.50)): 
	print(f"Zijia's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Zijia's weekly toll should be $34.50, but you got ${weekly_toll:.2f}")


#Yamato works everyday but saturday and sunday, ending at 3, starting at 8.
weekly_toll = calc_weekly_toll(weekend_emp=False, end_work=3)
if(test_solution(weekly_toll, 34.50)): 
	print(f"Zijia's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Zijia's weekly toll should be $34.50, but you got ${weekly_toll:.2f}")


#As the CEO, Mayu picks his own hours.  He leaves everyday at 2, 
#but shows up at noon.  He also never works Monday, Friday, Saturday or Sunday.
weekly_toll = calc_weekly_toll(end_work=2,begin_work=12,in_office_days=3)
if(test_solution(weekly_toll, 17.55)): 
	print(f"Mayu's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Mayu's weekly toll should be $17.55, but you got ${weekly_toll:.2f}")


#Clarabell works completely remotely.  She does not have any days in the office.
weekly_toll = calc_weekly_toll(in_office_days=0)
if(test_solution(weekly_toll, 0)): 
	print(f"Clarabell's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Clarabell's weekly toll should be $0, but you got ${weekly_toll:.2f}")

#Adriana must work 13 hour days starting at 7am, but most only work Monday, Tuesday, Wednesday
weekly_toll = calc_weekly_toll(in_office_days=3, begin_work=7, end_work=8)
if(test_solution(weekly_toll, 7.65)): 
	print(f"Adriana's weekly toll of ${weekly_toll:.2f} is correct")
else:
	print(f"Adriana's weekly toll should be $7.65, but you got ${weekly_toll:.2f}")

