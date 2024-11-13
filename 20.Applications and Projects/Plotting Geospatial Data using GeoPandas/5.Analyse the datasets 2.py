fig, ax = plt.subplots(1, figsize =(16, 8))
world.plot(ax = ax, color ='black')
world.plot(ax = ax, column ='pop_est', cmap ='Reds')
