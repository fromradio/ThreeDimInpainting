#! /usr/bin/env python
# parameterization optimization for sparse fitting

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt 
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(var):
	if var.shape[1] != 2:
		raise ValueError("The input should be 2d")
	return np.sin(var[:,0])*np.cos(var[:,1])

n = 1000
x = (np.random.rand(n,2)-0.5)*2*np.pi
mainfig = plt.figure()


def main():
	# for debug
	tri = Delaunay(x)
	ax = mainfig.add_subplot(111,projection='3d')
	ax.plot_trisurf(x[:,0],x[:,1],f(x),cmap = cm.jet)
	print f(x)
	mainfig.show()
	plt.show()
if __name__=='__main__':
	main()