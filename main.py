
import scipy as signal
import numpy as np
import matplotlib.pyplot as plt
import pprint

def convvolve(a, b):
    b_inv = np.flip(b.copy)

def prosto_():
    a=np.array([0., 0., 0., 3., 3., 4., 4., 4.,2., 2., 0., 0., 5., 5., 6., 7., 7., 5., 4., 3.,2., 2., 0., 0.,], dtype=float)    
    b=np.array([0., 2., -2., 2., -2., 1., -1., -1.,0., 1., 1., 0.], dtype=float)
    z=signal.convolve(a, b, mode='full')
    plt.plot(a)
    plt.plot(b)
    plt.plot(z)
    plt.legend(['a', 'b', 'z'])
    plt.show()

def the_task_1():
# задача 1
    a=np.ones(3)    
    m=np.zeros(21) 
    m[8:11]=a
    z=signal.convolve(m, m, mode='full')
    plt.plot(m)
    plt.plot(z)
    plt.legend(['m',  'z'])
    plt.show()

def the_task_2():
    # задача 2
    a=np.random.randint(-1, 15, 40)
    b=np.random.randint(0, 7, 20)

    z=np.correlate( a , b, mode='full' ) 

    pprint.pprint("a = {}".format(a))
    pprint.pprint("b = {}".format(b))
    pprint.pprint("z = {}".format(z))
    plt.plot(a)
    plt.plot(b)
    plt.plot(z)
    plt.legend(['a', 'b', 'z'])
    plt.show()

def the_task_3():
    # задача 3
    a=np.ones(3)    
    m=np.zeros(21) 
    m[8:11]=a
    z=signal.convolve(m, m, mode='full')
    plt.plot(m)
    plt.plot(z)
    plt.legend(['m',  'z'])
    plt.show()


if __name__ == "__main__":
#    prosto_()
#   the_task_1()
#   the_task_2()
   the_task_3()


    
