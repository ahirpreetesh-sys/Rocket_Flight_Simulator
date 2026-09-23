import math
g=9.8
rho=1.2
#Rocket specs
mass_r=600
mass_f=400
thrust=25000
burn_t=20
drag_co=0.5
cross_a=0.2
launch_a=80
#Simulation settings
dt=0.1
max_t=100
fuel_b_r=mass_f/burn_t
angle_rad=math.radians(launch_a)
#INITIAL CONSTANTS
x=0
y=0
ax=0
ay=0
time=0
current_f=mass_f
pitch_a=angle_rad
steps=0
current_th=0

print(f"{'time(s)':<10}{'altitude(m)':<15}{'downrange(m)':<15}{'speed(m/s)':<12}")
print("*"*50)
#THE SIMULATION LOOP
while (time<=max_t):
    v_mg=math.sqrt(ax**2 + ay**2)
    if(v_mg>0.1):
        pitch_a=math.atan2(ay,ax)
    #else:
     #   pi    tch_a=angle_rad
    if(time<=burn_t and current_f>0):
        current_th=thrust
        current_f-=thrust
        current_f-=fuel_b_r*dt
        current_f=max(current_f,0)
    else:
        current_th=0
    total_m=mass_f+mass_r
    f_drag=0.5*rho*(v_mg**2)
    thrust_x=current_th*math.cos(pitch_a)
    thrust_y=current_th*math.sin(pitch_a)

    drag_x=f_drag*math.cos(pitch_a)
    drag_y=f_drag*math.sin(pitch_a)
    
    bx=(thrust_x-drag_x)/total_m
    by=(thrust_y-drag_y-(total_m*g))/total_m
    
    ax += bx*dt
    ay += by*dt
    x += ax*dt
    y += ay*dt
    
    time +=dt
    steps+=1
    
    if(steps%int(2/dt)==0):
        print(f"{time:<10f}{y:<15f}{v_mg:<12f}")
    if(y<0):
        print("*"*50)
        print(f"crash! rocket hit the ground at {time:1f} second")
        break
