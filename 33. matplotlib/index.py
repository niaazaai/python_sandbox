import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
points = [2, 5, 11, 17, 100]

fig, ax = plt.subplots()
ax.plot(squares , points , 2)
plt.show()
