import matplotlib.pyplot as plt
import numpy as np

V0 = 3000 # м/c
B0 = 10 # Тл
mu0 = np.pi * 4 * (10**(-7)) # константа mu0
Fi = 1 # Тл*м^2
q = 9600 # кг/м^3
h = 10 # м
d = 0.001 # м
D = 0.1 # м
m = 960 # кг
dt = 0.0000005
n = 500

time = [dt * (i + 1) for i in range(n)]
ds = [ 2 * V0 * h * dt]
B = [ B0 * Fi / (Fi - ds[0]) ]
I = [ B[0] * (h / mu0) ]
a = [ B[0] * I[0] * (h / m) ]
V = [ V0 - (dt * a[0]) ]
xds = [ 2 * V0 * dt] 
a1 = [-a[0]]

for i in range(1, n):
    ds.append(2 * V[i - 1] * h * dt + ds[i - 1])
    B.append(B0 * Fi / (Fi - ds[i]))
    I.append(B[i] * (h / mu0))
    a.append(B[i] * I[i] * (h / m))
    a1.append(-a[i])
    V.append(V[i - 1] - a[i]*dt)
    xds.append( 2 * V[i - 1] * dt)


cont = [ (q  - ds[i]) / 10 for i in range(n)]

fig, axs = plt.subplots(2, 2, figsize=(20,10))
axs[0,0].plot(time, V, color="g")
axs[0,0].set_ylabel('Скорость')
axs[0,0].set_xlabel('time')

axs[1,0].plot(time, cont, color="g")
axs[1,0].set_ylabel('расстояние от пластин')
axs[1,0].set_xlabel('time')

axs[0,1].plot(time, B, color="g")
axs[0,1].set_ylabel('Магнитное поле')
axs[0,1].set_xlabel('time')

axs[1,1].plot(time, a1, color="g")
axs[1,1].set_ylabel('Ускорение')
axs[1,1].set_xlabel('time')

fig.suptitle('Графики', fontsize=16)
plt.show()