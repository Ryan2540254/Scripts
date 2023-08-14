# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:04:39 2023

@author: ADMIN
"""

import numpy as np

a= np.array([[2,1,3],[4,2,1],[2,3,2]])
print(a)

det = round((np.linalg.det(a)),2)
In  = np.linalg.inv(a)
print(det)
print(In)