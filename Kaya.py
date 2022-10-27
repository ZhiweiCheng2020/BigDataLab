class kaya_identity:
    def __init__(self, pop_size: float, gdp: float, energy_intensity: float, carbon_intensity: float) -> None:
        self.pop_size = pop_size
        self.gdp = gdp
        self.energy_intensity = energy_intensity
        self.carbon_intensity = carbon_intensity
    
    def check_input(self, variable, def_string):
        if not (isinstance((variable), (float, int))):
            raise ValueError("Please input a number for "+ def_string + "!")
        if variable <= 0:
            raise ValueError("Please input a positive number for "+ def_string + "!")
        
    def cal_kaya_identity(self) -> float:
        """
        pop_size: Population size (in millions)
        gdp: GDP per capita (in 1000$/person)
        energy_intensity: Energy intensity (in Gigajoule/$1000GDP)
        carbon_intensity: Carbon intensity (in tonnes CO2/Gigajoule)
        
        return: carbon_intensity, 
        """
        kaya_identity.check_input(self, self.pop_size, "Population size")
        kaya_identity.check_input(self, self.gdp, "GDP per capita")
        kaya_identity.check_input(self, self.energy_intensity, "Energy intensity")
        kaya_identity.check_input(self, self.carbon_intensity, "Carbon intensity")
            
        
        kaya_iden = self.pop_size * self.gdp * self.energy_intensity * self.carbon_intensity
        print(kaya_iden)
        return kaya_iden
    
if __name__ == "__main__":
    kaya_identity(1,2,1,1).cal_kaya_identity()