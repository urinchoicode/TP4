# Ex 1 Arbres d'expression

import math

class Noeud:

    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter(self, enfant):
        if not isinstance(enfant, Noeud):
            raise TypeError("enfant n'est pas un noeud !")
        self.enfants.append(enfant)

    def affichage_polonais(self):
        poland_list = [str(self.valeur)]
        for enfant in self.enfants:
            poland_list.append(enfant.affichage_polonais())
        return " ".join(poland_list)

    def evaluer(self, variables = dict):
        # 1. 상수(숫자)인 경우
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        # 2. 연산자인 경우
        if self.valeur in ["+", "-", "*", "/", "exp", "log", "sin", "cos"]:
            vals = [e.evaluer(variables) for e in self.enfants]
            
            # 단항 연산자
            if self.valeur == "exp":
                return math.exp(vals[0])
            elif self.valeur == "sin":
                return math.sin(vals[0])
            elif self.valeur == "cos":
                return math.cos(vals[0])
            elif self.valeur == "log":
                return math.log(vals[0])

            # 이항 연산자
            elif self.valeur == "+":
                return vals[0] + vals[1]
            elif self.valeur == "-":
                return vals[0] - vals[1]
            elif self.valeur == "*":
                return vals[0] * vals[1]
            elif self.valeur == "/":
                return vals[0] / vals[1]

        # 3. 변수인 경우
        if isinstance(self.valeur, str):
            if self.valeur in variables:
                return float(variables[self.valeur])
            else:
                raise ValueError(f"Variable non définie: '{self.valeur}'")

        raise ValueError(f"Valeur de noeud inconnue: {self.valeur}")
