#-----------------------
# ROCKET CONFIGURATIOON
#-----------------------

RocketMass=80000   #weight of rocket in kg
FullMass=30000     #fuel weight at the time of launching in kg
BurnRate=200       #fuel burning per second
Thrust=500000      #upward thrust 

# ENVIRONMENT VARIABLES

gravity=9.8
dt=1
TotalTime=120

#STARTING CONDITIONS

Altitude=0
Velocity=0
CurrentTime=0
print("ROCKET LAUNCH TIMELINE")
print("Time(s),Altitude(m),Speed(m/s),Fule Left(kg)")
print("-"*50)

#---------------------
# THE SIMULATION LOOP
#---------------------

while (CurrentTime<=TotalTime):
    if(FullMass>0):
        CurrentThrust=Thrust
        FullMass=FullMass-(BurnRate*dt)      #burn fule
    elif(FullMass<0):
        FullMass=0                           #prevent negative fuel
    else:
        CurrentThrust=0                      #out of fuel,engine cuts off
TotalMass=FullMass+RocketMass
UpwardForce=CurrentThrust
DownwardForce=TotalMass*gravity
NetForce=UpwardForce-DownwardForce
Acceleration=NetForce/TotalMass
Velocity=Velocity+(Acceleration*dt)
Altitude=Altitude+(Velocity*dt)
if(Altitude<0):
    Altitude=0
    Velocity=0
    if(CurrentTime%10==0):
        print(f"{CurrentTime:6f}|{Altitude:11.1f}|{Velocity:10f}|{FullMass:12f}")


