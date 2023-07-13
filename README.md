# Predominance-diagrams-for-the-Ni-S-O

**The problem description**
To write a program which displays predominance diagrams for the Ni-S-O system for varying temperatures.
A predominance diagram basically predicts the number of phases which can form at a particular temperature, it gives the stability of phase for a given partial pressure of SO2 and O2.
Here, the input of the program would be the Temperature according to which a graph of log 〖pO_2〗_v/s log p〖SO〗_2 where p_x  represents partial pressure of x at the particular temperature.These partial pressures are calculated using the temperature dependent equations for change in Gibbs free energy and equilibrium constant.

![image](https://github.com/aaryac33/Predominance-diagrams-for-the-Ni-S-O/assets/102223660/6565728e-4506-4056-aaca-a9c1240a2fa2)
	 
The diagram above depicts the predominance area diagram for Ni - S - O system at constant (specific) temperature.

**Methodology adopted**
We consider the equilibrium state values which means that in the Ni-S-O system, 
> we have to consider all possible reactions which can take place
> we need to know the gibbs free energy values from which we can calculate the equilibrium constant K
> From K, we find out the variation of pSO2 and pO2 while temperature T is constant.
Here, we consider the activity of the condensed phase (c) to be equal to 1.

**Typical results**
According to the diagram above, 
>B, C and D are invariant points 
which means that at these points degrees of freedom F=0 and all the phases will coexist at a particular value of pSO2 and pO2..therefore P=3 and since F=3-P, F=3-3=0.
>Along lines CD or DH, P=2 therefore F=3-2=1
Which means that NiS or NiO can be present at different values of pSO2 for a given value of pO2 (or) different values of pO2 for a given value of pSO2.
> Now, if P=1, F=3- 1=2 
Which means that the phase NiO, NiS and NiSO4 can exist for various combinations of pSO2 and pO2 
Eg: you can change the values of pSO2 and pO2 & get the phase NiO or NiSO4 or NiS

Delta G ( gibbs free energy) values are obtained from the website https://www.drjez.com/uco/ChemTools/Standard%20Thermodynamic%20Values.pdf


For the line CD, NiS and NiO are in equilibrium
NiS(c) + 3/2 O2(g) = NiO(c) + SO2(g) 

delG1=delG_Ni0 + delG_SO2- delG_NiS
K1= exp(-delG1/(R*T))

K1= pSO2/(pO2)^3/2
log(pSO2) = log K1 + 3/2 log(pO2)
Hence this line CD has a slope of 3/2 

	For the line BC, Ni3S2 and NiO are in equilibrium
Ni3S2(c) + 7/2 O2(g) = 3NiO(c) + 2SO2(g)

delG2=3delG_Ni0 +2delG_SO2- delG_Ni3S2
K2= exp(-delG2/(R*T))

K2= (pSO2)^2/(pO2)^7/2
log(pSO2) = 1/2 log K2 + 7/4 log(pO2)
Hence this line BC has a slope of 7/4

For the line AB, Ni and NiO are in equilibrium
Ni(c) + ½ O2(g) = NiO(c)

delG3=delG_Ni0 - delG_Ni
K3= exp(-delG3/(R*T))

K3= 1/(pO2)^½
logK3 = -1/2log(pO2)
Here we see that it’s independent of pSO2, hence a vertical line in the Ni S O system.

For the line GD, NiS and NiSO4 are in equilibrium
NiS(c) + 2O2(g) = NiSO4(c)

delG4=delG_NiSO4 - delG_NiS
K4= exp(-delG4/(R*T))

K4= 1/(pO2)^2
log K4= -2log(pO2)
Here also we see that it’s independent of pSO2, hence a vertical line in the Ni S O system.

For the line DH, NiSO4 and NiO are in equilibrium
2NiO(c) + 2SO2(g) = NiSO4(c) + O2(g)

delG5=delG_NiSO4- 2delG_NiO-2delG_SO2
K5= exp(-delG5/(R*T))

K5= pO2/(pSO2)^2
log (pSO2)= -½ logK5 + ½ log(pO2)
Hence this line DH has a slope of 1/2

For the line FC, NiS and Ni3S2 are in equilibrium
3NiS(c) + O2(g) = Ni3S2(c) + SO2(g)

delG6=delG_Ni3S2 + delG_SO2 - 3delG_NiS
K6= exp(-delG6/(R*T))

K6= pSO2/pO2
log pSO2 = log K6 + log pO2
Hence this line FC has a slope of 1


For the line EB, Ni3S2 and Ni are in equilibrium
Ni3S2(c) + 2O2(g) = 3Ni(c) + 2SO2(g)

delG7=3delG_Ni +2delG_SO2- delG_Ni3S2
K7= exp(-delG7/(R*T))

K7= (pSO2)^2/(pO2)^2
log(pSO2)= log(pO2) + ½ logK7
Hence this line EB also has a slope of 1
