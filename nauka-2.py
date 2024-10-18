# print ('Yeelo')
import numpy as np
height = 1.79
weight = 69
BMI = weight / height**2
print('BMI wynosi: ', round(BMI,2))
fam_weight = [54.6,63.2,89.3,78.1,49.9]
print(fam_weight)
np_fam_weight = np.array(fam_weight)
print('np_fam w kg:', np_fam_weight)
lb_factor = 0.45
np_lb_fam_weight = np.round(np_fam_weight / lb_factor ,2)
print('np_fam w lb: ', np_lb_fam_weight)