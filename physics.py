import math

def calculateDrag(Speed,DragCo,CrossA,rho=1.2):
    return (0.5*rho*(Speed**2)*DragCo*CrossA)

def computeAccelerations(Thrust,PitchA,DragF,TotalMass,g=9.8):
    ThrustX=Thrust*math.cos(PitchA)
    ThrustY=Thrust*math.sin(PitchA)
    
    DragX=DragF*math.cos(PitchA)
    DragY=DragF*math.sin(PitchA)
    
    bx=(ThrustX-DragX)/TotalMass
    by=(ThrustY-DragY-(TotalMass*g))/TotalMass
    
    return (bx,by)
