from viscosity import *

cwd = os.getcwd()

deck = Deck(cwd + "/" + "viscosity.yaml")

polymer = Polymer(deck)

model = Model(deck, polymer)

features = GraphFeatures(deck)

graph = Graph(deck, polymer, model, features)
