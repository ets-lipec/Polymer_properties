#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polymer:

    # Initializer Attributes
    def __init__(self, deck):
        self.name = deck.doc['Polymers']['Name']
        self.constantB = float(deck.doc['Polymers']['Constant B'])
        self.constantb = float(deck.doc['Polymers']['Constant b'])
        self.energy = float(deck.doc['Polymers']['Activation Energy'])
        self.name_bird = deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Name']
        self.constant_k1 = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Constant k1'])
        self.constant_k2 = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Constant k2'])
        self.constant_k3 = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Constant k3'])
        self.activation_energy = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Activation Energy'])
        self.ref_temperature = float(deck.doc['Polymers']['Constants for Carreau-Arrhenius model']['Reference Temperature'])
        self.gas_constant = float(deck.doc['Constants']['Gas Constant'])

    
