Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> from sklearn.linear_model import LinearRegression
>>> import pandas as pd
>>> from sklearn.model_selector import train_test_split
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from sklearn.model_selector import train_test_split
ModuleNotFoundError: No module named 'sklearn.model_selector'
>>> 
KeyboardInterrupt
>>> from sklearn.model_selection import train_test_split
>>> np.loadtxt(r'C:\Users\anaedu paschal\Desktop\as.txt', delimiter = ',')
array([[2.10400e+03, 3.00000e+00, 3.99900e+05],
       [1.60000e+03, 3.00000e+00, 3.29900e+05],
       [2.40000e+03, 3.00000e+00, 3.69000e+05],
       [1.41600e+03, 2.00000e+00, 2.32000e+05],
       [3.00000e+03, 4.00000e+00, 5.39900e+05],
       [1.98500e+03, 4.00000e+00, 2.99900e+05],
       [1.53400e+03, 3.00000e+00, 3.14900e+05],
       [1.42700e+03, 3.00000e+00, 1.98999e+05],
       [1.38000e+03, 3.00000e+00, 2.12000e+05],
       [1.49400e+03, 3.00000e+00, 2.42500e+05],
       [1.94000e+03, 4.00000e+00, 2.39999e+05],
       [2.00000e+03, 3.00000e+00, 3.47000e+05],
       [1.89000e+03, 3.00000e+00, 3.29999e+05],
       [4.47800e+03, 5.00000e+00, 6.99900e+05],
       [1.26800e+03, 3.00000e+00, 2.59900e+05],
       [2.30000e+03, 4.00000e+00, 4.49900e+05],
       [1.32000e+03, 2.00000e+00, 2.99900e+05],
       [1.23600e+03, 3.00000e+00, 1.99900e+05],
       [2.60900e+03, 4.00000e+00, 4.99998e+05],
       [3.03100e+03, 4.00000e+00, 5.99000e+05],
       [1.76700e+03, 3.00000e+00, 2.52900e+05],
       [1.88800e+03, 2.00000e+00, 2.55000e+05],
       [1.60400e+03, 3.00000e+00, 2.42900e+05],
       [1.96200e+03, 4.00000e+00, 2.59900e+05],
       [3.89000e+03, 3.00000e+00, 5.73900e+05],
       [1.10000e+03, 3.00000e+00, 2.49900e+05],
       [1.45800e+03, 3.00000e+00, 4.64500e+05],
       [2.52600e+03, 3.00000e+00, 4.69000e+05],
       [2.20000e+03, 3.00000e+00, 4.75000e+05],
       [2.63700e+03, 3.00000e+00, 2.99900e+05],
       [1.83900e+03, 2.00000e+00, 3.49900e+05],
       [1.00000e+03, 1.00000e+00, 1.69900e+05],
       [2.04000e+03, 4.00000e+00, 3.14900e+05],
       [3.13700e+03, 3.00000e+00, 5.79900e+05],
       [1.81100e+03, 4.00000e+00, 2.85900e+05],
       [1.43700e+03, 3.00000e+00, 2.49900e+05],
       [1.23900e+03, 3.00000e+00, 2.29900e+05],
       [2.13200e+03, 4.00000e+00, 3.45000e+05],
       [4.21500e+03, 4.00000e+00, 5.49000e+05],
       [2.16200e+03, 4.00000e+00, 2.87000e+05],
       [1.66400e+03, 2.00000e+00, 3.68500e+05],
       [2.23800e+03, 3.00000e+00, 3.29900e+05],
       [2.56700e+03, 4.00000e+00, 3.14000e+05],
       [1.20000e+03, 3.00000e+00, 2.99000e+05],
       [8.52000e+02, 2.00000e+00, 1.79900e+05],
       [1.85200e+03, 4.00000e+00, 2.99900e+05],
       [1.20300e+03, 3.00000e+00, 2.39500e+05]])
>>> data = np.loadtxt(r'C:\Users\anaedu paschal\Desktop\as.txt', delimiter = ',')
>>> np.c_[data[:,0]]
array([[2104.],
       [1600.],
       [2400.],
       [1416.],
       [3000.],
       [1985.],
       [1534.],
       [1427.],
       [1380.],
       [1494.],
       [1940.],
       [2000.],
       [1890.],
       [4478.],
       [1268.],
       [2300.],
       [1320.],
       [1236.],
       [2609.],
       [3031.],
       [1767.],
       [1888.],
       [1604.],
       [1962.],
       [3890.],
       [1100.],
       [1458.],
       [2526.],
       [2200.],
       [2637.],
       [1839.],
       [1000.],
       [2040.],
       [3137.],
       [1811.],
       [1437.],
       [1239.],
       [2132.],
       [4215.],
       [2162.],
       [1664.],
       [2238.],
       [2567.],
       [1200.],
       [ 852.],
       [1852.],
       [1203.]])
>>> data_x1 = np.c_[data[:,0]]
>>> data_x2 = np.c[data[:,1]]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    data_x2 = np.c[data[:,1]]
AttributeError: module 'numpy' has no attribute 'c'
>>> data_x2 = np.c_[data[:,1]]
>>> y = np.c_[data[:,2]]
>>> x_data = np.c_[data_x1,data_x2]
>>> plt.scatter(data_x1,y, marker = x)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    plt.scatter(data_x1,y, marker = x)
NameError: name 'x' is not defined
>>> plt.scatter(data_x1,y, marker = 'x')
<matplotlib.collections.PathCollection object at 0x00D959F0>
>>> plt.xlabel('Size')
Text(0.5, 0, 'Size')
>>> plt.ylabel('Price')
Text(0, 0.5, 'Price')
>>> plt.title('Price against Size of Rooms')
Text(0.5, 1.0, 'Price against Size of Rooms')
>>> plt.show()
>>> from mpl_toolkits.mplot3d import axes3d
>>> fig = plt.figure()
>>> ax = axes3d(fig)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ax = axes3d(fig)
TypeError: 'module' object is not callable
>>> x_test, x_train, y_test, y_train = train_test_split(data_x2, y, test_size = 0.2, random_state = 0)
>>> reg = LinearRegression()
>>> reg.fit(x_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
>>> reg.predict(x_test)
array([[369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [369913.21348315],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [310548.34831461],
       [310548.34831461],
       [369913.21348315],
       [369913.21348315],
       [369913.21348315],
       [488642.94382022],
       [429278.07865169],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [369913.21348315],
       [369913.21348315],
       [369913.21348315],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [310548.34831461],
       [429278.07865169],
       [369913.21348315],
       [429278.07865169],
       [369913.21348315],
       [310548.34831461],
       [369913.21348315],
       [310548.34831461]])
>>> y_pred = reg.predict(x_test)
>>> from sklearn.metrics import r2_score
>>> r2_score(y_test,y_pred)
0.028383724810793765
>>> reg.intercept_
array([191818.61797753])
>>> reg.predict(2150)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    reg.predict(2150)
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\base.py", line 213, in predict
    return self._decision_function(X)
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\base.py", line 196, in _decision_function
    X = check_array(X, accept_sparse=['csr', 'csc', 'coo'])
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\utils\validation.py", line 545, in check_array
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got scalar array instead:
array=2150.
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
>>> reg.predict([2450,3000])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    reg.predict([2450,3000])
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\base.py", line 213, in predict
    return self._decision_function(X)
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\base.py", line 196, in _decision_function
    X = check_array(X, accept_sparse=['csr', 'csc', 'coo'])
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\utils\validation.py", line 552, in check_array
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got 1D array instead:
array=[2450 3000].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
>>> reg.predict([2450][3000])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    reg.predict([2450][3000])
IndexError: list index out of range
>>> reg.predict([2450])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    reg.predict([2450])
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\base.py", line 213, in predict
    return self._decision_function(X)
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\base.py", line 196, in _decision_function
    X = check_array(X, accept_sparse=['csr', 'csc', 'coo'])
  File "C:\Users\anaedu paschal\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\utils\validation.py", line 552, in check_array
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got 1D array instead:
array=[2450].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
>>> x_data
array([[2.104e+03, 3.000e+00],
       [1.600e+03, 3.000e+00],
       [2.400e+03, 3.000e+00],
       [1.416e+03, 2.000e+00],
       [3.000e+03, 4.000e+00],
       [1.985e+03, 4.000e+00],
       [1.534e+03, 3.000e+00],
       [1.427e+03, 3.000e+00],
       [1.380e+03, 3.000e+00],
       [1.494e+03, 3.000e+00],
       [1.940e+03, 4.000e+00],
       [2.000e+03, 3.000e+00],
       [1.890e+03, 3.000e+00],
       [4.478e+03, 5.000e+00],
       [1.268e+03, 3.000e+00],
       [2.300e+03, 4.000e+00],
       [1.320e+03, 2.000e+00],
       [1.236e+03, 3.000e+00],
       [2.609e+03, 4.000e+00],
       [3.031e+03, 4.000e+00],
       [1.767e+03, 3.000e+00],
       [1.888e+03, 2.000e+00],
       [1.604e+03, 3.000e+00],
       [1.962e+03, 4.000e+00],
       [3.890e+03, 3.000e+00],
       [1.100e+03, 3.000e+00],
       [1.458e+03, 3.000e+00],
       [2.526e+03, 3.000e+00],
       [2.200e+03, 3.000e+00],
       [2.637e+03, 3.000e+00],
       [1.839e+03, 2.000e+00],
       [1.000e+03, 1.000e+00],
       [2.040e+03, 4.000e+00],
       [3.137e+03, 3.000e+00],
       [1.811e+03, 4.000e+00],
       [1.437e+03, 3.000e+00],
       [1.239e+03, 3.000e+00],
       [2.132e+03, 4.000e+00],
       [4.215e+03, 4.000e+00],
       [2.162e+03, 4.000e+00],
       [1.664e+03, 2.000e+00],
       [2.238e+03, 3.000e+00],
       [2.567e+03, 4.000e+00],
       [1.200e+03, 3.000e+00],
       [8.520e+02, 2.000e+00],
       [1.852e+03, 4.000e+00],
       [1.203e+03, 3.000e+00]])
>>> 
