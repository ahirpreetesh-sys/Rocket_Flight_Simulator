import math

MassR=int(input("Enter rocket mass (kg) "))
MassF=int(input("Enter fuel mass (kg) "))
Thrust=int(input("Enter thrust (N) "))
BurnT=int(input("Enter burn time (s) "))
DragCo=0.5
g=9.8
rho=1.2
CrossA=0.2
LaunchA=int(input("Enter launch angle (degrees) "))

                                                                                                    #simulation setting

dt=0.1
MaxT=100
Fuel_b_r=MassF/BurnT
AngleRad=math.radians(LaunchA)

                                                                                                    #initial constants

x=0
y=0
ax=0  
ay=0  
Time=0
CurrentF=MassF
PitchA=AngleRad
steps=0

print(f"{'Time(s)':<10}{'Altitude(m)':<15}{'Downrange(m)':<15}{'Speed(m/s)':<12}")
print("-"*60)
print(f"{Time:<10.2f}{y:<15.3f}{x:<15.3f}{0:<12.3f}")

                                                                                                    #simulation loop

while(Time<=MaxT):
                                                                                                    #calculation
    VMg=math.sqrt(ax**2+ay**2)
    if(VMg>0.1):
        PitchA=math.atan2(ay,ax)
    else:
        PitchA=AngleRad
                                                                                                    #condition for fuel
    if ((Time<BurnT) and (CurrentF>0)):
        current_th=Thrust
        CurrentF -=Fuel_b_r*dt
        CurrentF=max(CurrentF,0)
    else:
        current_th=0
    TotalM=CurrentF+MassR
    FDrag=0.5*rho*(VMg**2)*DragCo*CrossA                                                            #force

                                                                                                    #vector component

    thrust_x =current_th*math.cos(PitchA)
    thrust_y =current_th*math.sin(PitchA)
    dragX =FDrag*math.cos(PitchA)
    dragY =FDrag*math.sin(PitchA)

                                                                                                    #net acceleration

    bx=(thrust_x-dragX)/TotalM
    by=(thrust_y-dragY-(TotalM*g))/TotalM

                                                                                                    #new velocity

    ay+=by*dt
    ax+=bx*dt

                                                                                                    #new position

    x+=ax*dt
    y+=ay*dt

    Time+=dt
    steps+=1

    if(steps%int(2/dt)==0):
        print(f"{Time:<10.1f}{y:<15.2f}{x:<15.2f}{VMg:<12.2f}")

    if((y<0) and (Time>dt)):
        print("*"*50)
        print(f"Crash! rocket hit the ground at {Time:.1f} seconds")
        break
