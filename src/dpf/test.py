#%%
from dysts.flows import Lorenz
import matplotlib.pyplot as plt

model = Lorenz()
sol = model.make_trajectory(1000)
plt.plot(sol[:, 0], sol[:, 1])


#%%
eq = Lorenz()
sol = eq.load_trajectory(subsets="test", noise=False, granularity="fine")
plt.plot(sol[:, 0], sol[:, 1])
