import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def h(x):
	if x>0:
		return np.exp(-1/(x*x))
	else:
		return 0

def g(x):
	return (h(2-x)/(h(2-x) + h(x-1)))

def b(x):
	if x>0:
		return g(x)
	else:
		return g(-x)

@np.vectorize
def sinc(x,y):
	if x == 0 and y == 0:
		return 0
	else:
		return np.sin(np.sqrt(x*x + y*y))/np.sqrt(x*x + y*y)

def fn_plot1d(fn, x_min ,x_max ,filename):
	x = np.linspace(x_min,x_max,num=500)
	plt.plot(x,list(map(fn,x)))
	plt.xlabel("x")
	plt.ylabel("b(x)")
	plt.grid(True)
	plt.title("b(x) vs x plot")
	plt.savefig(filename)
	plt.close()

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
	xx = np.linspace(x_min,x_max,num=500)
	yy = np.linspace(y_min,y_max,num=500)
	x,y = np.meshgrid(xx,yy)
	z = fn(x,y)
	ax = Axes3D(plt.gcf())
	ax.plot_surface(x,y,z)
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	plt.title("z = sincc(x,y) plot")
	plt.savefig(filename)
	plt.close()

def nth_derivative_plotter(fn,n,xmin,xmax,filename):
	xx = np.linspace(xmin,xmax,num=500)
	y = [derivative(fn,x,n=n,dx=0.0001) for x in xx]
	plt.plot(xx,y)
	plt.grid(True)
	plt.xlabel("x")
	plt.ylabel("$b^%i$(x)" %n)
	plt.title("%ith derivative plot of b(x)" %n)
	plt.savefig(filename)
	plt.close()


fn_plot1d(b,-2,2,"fn1plot.png")
fn_plot2d(sinc,-1.5*np.pi,1.5*np.pi,-1.5*np.pi,1.5*np.pi,"fn2plot.png")
nth_derivative_plotter(b,1,-2,2,"bd_1.png")
nth_derivative_plotter(b,2,-2,2,"bd_2.png")



