#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CONSIGNE
# Pour réussir cet exercice, il faut que le pre-commit fasse un test unitaire sur les fonctions ex2a et ex2b
# Le test unitaire, en cas d'échec, doit empêcher le commit de fonctionner
# En cas de mauvais argument envoyé, à toi de trouver la meilleure stratégie (tu peux modifier les fonctions si besoin)

# ex2a
def ex2a(nb1, nb2):
        return (nb2 - nb1) / nb2 # doit renvoyer le résultat de cette opération

# ex2b
# Renvoie la somme des nombre envoyés en paramétre
# Exemple ex2b("1 2 3 4") -> 10
def ex2b(arg):
        return sum([int(a) for a in arg.split(' ')])