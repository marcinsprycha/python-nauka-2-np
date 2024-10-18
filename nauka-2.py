# print ('Yeelo')
import numpy as np
np_random_5000_height = np.round(np.random.normal(1.75,0.20,5000),2)
np_random_5000_weight = np.round(np.random.normal(70, 15, 5000),2)
np_stack = np.column_stack((np_random_5000_height,np_random_5000_weight))
print(np_random_5000_height)
print(np_random_5000_weight)
print(np_stack)

fam1_weight = [54.6,63.2,89.3,78.1,49.9]
fam1_height = [1.67,1.56,1.81,1.85,0.31]
fam2_weight = [79.5,102.4,98.3,78.1]
fam2_height = [1.56,1.61,1.70,1.69]

# fam1fam2_weight = fam1_weight + fam2_weight
# fam1fam2_height = fam1_height + fam2_height
# fam1fam2_weightheight = [fam1fam2_weight,fam1fam2_height]
# print(fam1fam2_weightheight)
print('fam1_weight: ',fam1_weight)
print('fam1_height: ' ,fam1_height)
print('fam2_weight: ',fam2_weight)
print('fam2_height: ' ,fam2_height)
# print('fam1fam2_weight: ',fam1fam2_weight)
# print('fam1fam2_height: ' ,fam1fam2_height)
np_fam1_weight = np.array(fam1_weight)
np_fam1_height = np.array(fam1_height)
np_fam1_bmi = np_fam1_weight / np_fam1_height ** 2
np_fam1_weight_height = np.array([np_fam1_height,np_fam1_weight])
print('np_fam1_weight_height: ', np_fam1_weight_height)
print('np_fam1_weight_height shape: ',np_fam1_weight_height.shape)
print('np_fam1_bmi: ', np_fam1_bmi)
print('np_fam1_bmi > 23: ', np_fam1_bmi[np_fam1_bmi > 23])
print('np_fam_weight w kg:', np_fam1_weight)
print('np_fam_height w m: ', np_fam1_height)
lb_factor = 0.4536
foot_factor = 0.3048
np_lb_fam1_weight = np.round(np_fam1_weight / lb_factor ,2)
np_foot_fam1_height = np.round(np_fam1_height/foot_factor ,2)
print('np_fam_weight w funtach: ', np_lb_fam1_weight)
print('np_fam_height w stopach: ', np_foot_fam1_height)
# print((fam1fam2_weightheight))