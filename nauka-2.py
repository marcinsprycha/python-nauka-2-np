# print ('Yeelo')
import numpy as np


fam_weight = [54.6,63.2,89.3,78.1,49.9]
fam_height = [1.67,1.56,1.81,1.85,0.31]
print('fam_weight: ',fam_weight)
print('fam_height: ' ,fam_height)
np_fam_weight = np.array(fam_weight)
np_fam_height = np.array(fam_height)
print('np_fam_weight w kg:', np_fam_weight)
print('np_fam_height w m: ', np_fam_height)
lb_factor = 0.4536
foot_factor = 0.3048
np_lb_fam_weight = np.round(np_fam_weight / lb_factor ,2)
np_foot_fam_height = np.round(np_fam_height/foot_factor ,2)
print('np_fam_weight w funtach: ', np_lb_fam_weight)
print('np_fam_height w stopach: ', np_foot_fam_height)