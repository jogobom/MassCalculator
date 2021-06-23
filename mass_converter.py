class MassConverter:
    ProtonMassAmu = 1.007276467
    C13MinusC12MassAmu = 1.0033548378

    def NeutralMonoisotopicMassToObservedMz(self, neutralMass, charge, isotope):
        if(charge < 0):
            return (neutralMass + self.C13MinusC12MassAmu * isotope) / abs(charge) - self.ProtonMassAmu
        elif(charge > 0):
            return (neutralMass + self.C13MinusC12MassAmu * isotope) / charge + self.ProtonMassAmu
        else:
            return (neutralMass + self.C13MinusC12MassAmu * isotope)
