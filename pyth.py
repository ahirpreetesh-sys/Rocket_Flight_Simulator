import math

g = 9.8
rho = 1.2

# Rocket specs
mass_r=int(input("Enter rocket mass (kg) "))
mass_f=int(input("Enter fuel mass (kg) "))
thrust=int(input("Enter thrust (N) "))
burn_t=int(input("Enter burn time (s) "))
drag_co=0.5
cross_a=0.2
launch_a=int(input("Enter launch angle (degrees) "))

# Simulation settings
dt=0.1
max_t=100
fuel_b_r=mass_f/burn_t
angle_rad=math.radians(launch_a)

# INITIAL CONSTANTS
x=0
y=0
vx=0  # Fixed: Defined velocity X
vy=0  # Fixed: Defined velocity Y
time=0
current_f=mass_f
pitch_a=angle_rad
steps=0

print(f"{'time(s)':<10}{'altitude(m)':<15}{'downrange(m)':<15}{'speed(m/s)':<12}")
print("-"*60)
print(f"{time:<10.1f}{y:<15.2f}{x:<15.2f}{0.0:<12.2f}")

# THE SIMULATION LOOP
while(time<=max_t):
    # Calculate speed and pitch from VELOCITY (vx, vy)
    v_mg=math.sqrt(vx**2+vy**2)
    if(v_mg>0.1):
        pitch_a=math.atan2(vy,vx)
    else:
        pitch_a=angle_rad

    # Fuel burn logic
    if (time<burn_t and current_f>0):  # Fixed: Changed <= to < to perfectly match fuel burn time
        current_th =thrust
        current_f -=fuel_b_r*dt
        current_f=max(current_f,0)
    else:
        current_th=0
    total_m =current_f+mass_r

    # Forces
    f_drag =0.5*rho*(v_mg**2)*drag_co*cross_a

    # Vector Components (Drag opposes the direction of velocity)
    thrust_x =current_th*math.cos(pitch_a)
    thrust_y =current_th*math.sin(pitch_a)
    drag_x =f_drag*math.cos(pitch_a)
    drag_y =f_drag*math.sin(pitch_a)

    # Net Accelerations
    ax =(thrust_x - drag_x)/total_m
    ay =(thrust_y - drag_y -(total_m * g))/total_m

    # Update Velocities (Fixed variable names)
    vx +=ax*dt
    vy +=ay*dt

    # Update Positions (Fixed: Use velocity vx/vy instead of acceleration ax/ay)
    x +=vx*dt
    y +=vy*dt

    time +=dt
    steps +=1

    if (steps%int(2/dt)==0):
        print(f"{time:<10.1f}{y:<15.2f}{x:<15.2f}{v_mg:<12.2f}")

    if y<0 and time>dt:
        print("*" *50)
        print(f"Crash! Rocket hit the ground at {time:.1f} seconds")
        break
