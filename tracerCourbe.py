import numpy as np
import matplotlib.pyplot as plt

def bonusGolem(tempsSansGolem):#en seconde
    return tempsSansGolem*1.5

def fonctionGolem(temps:int):
    if temps<3:
        return 0
    if temps>15:
        re= -temps/2.5+10
        if re <1:
            return 1
        return re
    return temps/6+1
y=[]
temps = np.linspace(0, 20, 100)
for x in temps:
    y.append(fonctionGolem(x))

fig, ax = plt.subplots()
ax.plot(temps, y)
plt.show()