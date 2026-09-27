class Rocket:
    def __init__(self,MassR,MassF,Thrust,BurnT):
        self.MassR=MassR
        self.MassF=MassF
        self.MaxThrust=Thrust
        self.BurnT=BurnT
        self.CurrentF=MassF
        self.Fuel_b_r=MassF/BurnT

    @property
    def TotalMass(self):
        return (self.CurrentF+self.MassR)

    def GetThrust(self,Time):
        if((Time<self.BurnT) and (self.CurrentF>0)):
            return (self.MaxThrust)
        return 0

    def update_fuel(self, dt):
        if (self.CurrentF>0):
            self.CurrentF-=(self.Fuel_b_r*dt)
            self.CurrentF=max(self.CurrentF,0)
