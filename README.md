# Polymer properties

## Viscosity

### Compute the viscosity as a function of the temperature and the shear stress  

<img src="https://latex.codecogs.com/gif.latex?\eta&space;=&space;B&space;exp(\frac{E_{\tau&space;}}{RT}-b\tau&space;^{s})" title="\eta = B exp(\frac{E_{\tau }}{RT}-b\tau ^{s})" />


&nbsp;


<img src="https://latex.codecogs.com/gif.latex?\eta" title="\eta" /> : Melt viscosity (Pa.s)

<img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /> : Shear stress

<img src="https://latex.codecogs.com/gif.latex?E_{\tau&space;}" title="E_{\tau }" /> : activation energy of viscous-elastic flow under condition of <img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /> = constant

R : gas constant in J/(mol.K)

T : temperature of experiment in K

B, b, s : Constants of the material (in this case : s=1/2)



### How this code works ?

**Classes**
- Deck : get the value in viscosity.yaml
- Polymer : stock the values of deck concerning the polymer in variables that will be reuse
- Model : contain the equation to predict the viscosity
- Graph : calculate the data with the model, draw the graphic and save it in the folder Graphics


**What the user have to do ?**
- Adapt the values in the file viscosity.yaml :

```yaml
Polymers:
  Name: 'PP Shell'
  Constant B: 1.5
  Constant b: 0.0043
  Activation Energy: 45522

Constants:
  Gas Constant: 8.314

Discretisation: 20
```

The Discretisation number is the number of points on the graphics.

- Install all required python packages listed in requirements.txt: 

```linux
pip install -r requirements.txt
```

- The only file which need to be run is the main_viscosity.py. This script brings together all classes.

```linux
python main_viscosity.py
```

## Surface tension
