#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reference : 
Mark G. Dodin Ph.D. (1986) 
Mathematical Models of Polymer Melt Viscosity in Shearing Flow.
Polystyrene and Polypropylene Melts—2
International Journal of Polymeric Materials and Polymeric Biomaterials
1:3, 185-203,
DOI: 10.1080/00914038608078660
"""

from math import exp


class Model:

    # Initializer Attributes
    def __init__(self, deck, polymer):
        self.deck = deck
        self.polymer = polymer


    # Model number 1
    # from [dodin_mathematical_1986] see biblio.bib
    def viscosity(self, B, E, R, T, b, shear_stress_power):
        """ 
        Prediction of the viscosity of melt polymer
        Valid for all polymers
        
        :Input:  
        - *B, b* : constant of the material
        - *E* : activation energy of viscous-elastic flow under condition of shear stress = constant
        - *shear_stress_power* : shear stresse to the power of 1/2
        - *R* : gas constant in J/(mol.K)
        - *T* : temperature of experiment (K)
        
        :Returns:
        Melt viscosity in shearing flow

        """
        return B*exp(E/(R*T)-b*shear_stress_power)


    # Model number 1
    # osswald_polymer_2006
    def arrhenius_shift(self, temperature, activation_energy, ref_temperature, R):
        """ 
        Prediction of the Arrhenius shift
        Valid for semi-crystalline polymers
        
        :Input:  
        - *temperature* : temperature (K)
        - *activation_energy* : activation energy (J/mol)
        - *ref_temperature* : reference temperature (K)
        - *R* : gas constant (J/(mol.K))
        
        :Returns:
        Arrhenius shift (no unit)
        """
        return exp((activation_energy / R * (1. / temperature - 1. / ref_temperature)))
        
    # The Bird-Carreau-Yasuda Model
    # osswald_polymer_2006
    def viscosity_bird(self, k1, k2, k3, arrhenius_shift, strain_rate):
        """ 
        Prediction of the melt viscosity
            
        :Input:  
        - *k1, k2, k3* : Constants for Carreau-Arrhenius model (semi-crystalline polymer)
        k1 in Pa.s, k2 in s and k3 no unit
        - *arrhenius_shift* : Arrhenius shift (no unit)
        - *strain_rate* : strain rate (/s)
            
        :Returns:
        Melt viscosity (Pa.s)
        """
        return k1 * arrhenius_shift / ((1 + k2 * strain_rate * arrhenius_shift)**k3)

