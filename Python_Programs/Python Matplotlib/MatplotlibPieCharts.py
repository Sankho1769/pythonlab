import matplotlib.pyplot as plt
values=list(map(float,input('Enter values: ').split())); labels=input('Enter labels separated by spaces: ').split(); plt.pie(values,labels=labels); plt.show()
