import numpy as np
from scipy import stats
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency

data=([207,282,241],[234,242,232])
stat,p,dof,excepted=chi2_contingency(data)
alpha=0.05
print("pvalue is"+str(p))
if p<=alpha:
    print("dependent reject H0")
else:
    print("independent accept H0")