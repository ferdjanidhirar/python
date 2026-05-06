class SystemeExpert:

    def __init__(self):
        self.faits = []
        self.regles = []
        self.historique = []

    def ajouteRegle(self, conditions, consequence):
        self.regles.append([conditions, consequence])

    def satisfait(self, regle):
        return all(c in self.faits for c in regle[0])

    def chainageAvantSimple(self, faitsInitiaux):

        self.faits = faitsInitiaux.copy()
        cycle = 1
        changement = True

        while changement:
            changement = False

            for i, regle in enumerate(self.regles):

                if self.satisfait(regle) and regle[1] not in self.faits:

                    self.faits.append(regle[1])
                    self.historique.append((cycle, i + 1, regle[1]))
                    changement = True

            cycle += 1

    def trace(self):
        for cycle, r, fait in self.historique:
            print(f"Cycle {cycle} -> R{r} => {fait}")


# ================= EXEMPLE =================

se = SystemeExpert()

se.ajouteRegle(["A", "B"], "C")
se.ajouteRegle(["C"], "D")
se.ajouteRegle(["D"], "E")

se.chainageAvantSimple(["A", "B"])

print("Faits finaux :", se.faits)
print("\nTrace :")
se.trace()
