#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
from math import *


class Graph:
    
    def __init__(self, deck, polymer, model, features):
        
        self.deck = deck
        self.polymer = polymer
        self.model = model
        self.viscosity_as_a_function_of_temperature_and_shear_stress(deck, polymer, model, features)
    
        

    def viscosity_as_a_function_of_temperature_and_shear_stress(self, deck, polymer, model, features):
        # Prediction of the melt viscosity as a function of the temperature and the shear stress.
        # Draw the graph of the log(melt viscosity) as a function of the shear stress to the power of 1/2 for differents temperatures
        
        T = [463, 483, 503, 533, 553]
        T = numpy.array(T)
        color = ['ro', 'bo', 'go', 'yo', 'ko']
        legend = ['463K', '483K', '503K', '533K', '553K']
        
        shear_stress_power = numpy.linspace(250, 1000, features.discretisation)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        
        for k in range(len(T)):
            log_melt_viscosity = []
            for i in range(features.discretisation):
                melt_viscosity = model.viscosity(polymer.constantB, polymer.energy, polymer.gas_constant, T[k], polymer.constantb, shear_stress_power[i])
                log_melt_viscosity.append(log10(melt_viscosity))
            log_melt_viscosity = numpy.array(log_melt_viscosity)
            axes.plot(shear_stress_power, log_melt_viscosity, color[k], label = legend[k])
            
        axes.grid()
        axes.set_xlabel("Shear stress to the power of 1/2", fontsize=16)
        axes.set_ylabel("log ( Melt viscosity )", fontsize=16)
        axes.set_title(" %s " % (polymer.name), fontsize=16, y=1.)
        axes.legend()
        plt.savefig("./graphics/viscosity_as_a_function_of_temperature_and_shear_stress.pdf", format="pdf")


    def bird_viscosity_as_a_function_of_temperature_and_strain_rate(self, deck, polymer, model, features):
        # Prediction of the melt viscosity as a function of the temperature and the strain rate.
        # Draw the graph of the melt viscosity as a function of the strain rate for differents temperatures
        
        T = [463, 483, 503, 533, 553]
        T = numpy.array(T)
        color = ['ro', 'bo', 'go', 'yo', 'ko']
        legend = ['463K', '483K', '503K', '533K', '553K']
        
        strain_rate = numpy.linspace(500, 4000, features.discretisation)
        
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1)
        
        for k in range(len(T)):
            melt_viscosity = []
            for i in range(features.discretisation):
                shift = model.arrhenius_shift(T[k], polymer.activation_energy, polymer.ref_temperature, polymer.gas_constant)
                melt_viscosity.append(model.viscosity_bird(polymer.constant_k1, polymer.constant_k2, polymer.constant_k3, shift, strain_rate[i]))
            melt_viscosity = numpy.array(melt_viscosity)
            axes.plot(strain_rate, melt_viscosity, color[k], label = legend[k])
            
        axes.grid()
        axes.set_xlabel("Strain rate in /s", fontsize=16)
        axes.set_ylabel("Melt viscosity", fontsize=16)
        axes.set_title(" %s " % (polymer.name_bird), fontsize=16, y=1.)
        axes.legend()
        plt.savefig("./graphics/viscosity_with_bird_model.pdf", format="pdf")
