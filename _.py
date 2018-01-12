def matplot_test01():
    """
    Created on Sun Jan  7 13:21:40 2018
    @author: nitt0
    """
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

def matplot_test02():
    """
    Created on Sun Jan  7 13:21:40 2018
    @author: nitt0
    """
    import numpy as np
    import matplotlib.pyplot as plt

    def value(x_value):
        return x_value**2

    x_range = np.arange(1, 20, 0.5)

    plt.figure(1)
    plt.plot(x_range, value(x_range), 'r--')
    #plt.plot(x_range, value(x_range), 'r--')
    plt.show()


matplot_test01()
