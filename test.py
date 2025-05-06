import numpy as np
from scipy import stats
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
data1=np.array([14,15,15,16,13,8,14,17,16,14,19,20,21,25,15,16,16,13,14,12])
print("1. One sample T test")
print("2. Independent T etest")
print("3. Anova test")
print("4. CHI sq  test")
print("5.exit")
user_choice=int(input("enter your choice:"))
match user_choice:
    case 1:
        populationMean= float(input("enter the population mean"))
        Testresults=stats.ttest_1samp(data1,popmean=populationMean)
        print(Testresults)
        print("____________")
    case 2:
        data2=np.array([157.97,146,140.2,170.15,167.34,176.123,162.35,156.123,169.43,148.123])
        result=stats.ttest_ind(data1,data2)
        print("**independent T-test**")
        print(result)
        print("_____________")
    case 3:
        perf1=[89,89,88,78,79]
        perf2=[93,92,94,89,88]
        perf3=[89,88,89,93,90]
        perf4=[81,78,81,92,82]
        res=f_oneway(perf1,perf2,perf3,perf4)
        print("**ANOVA**")
        print("_____________")
        if(res.pvalue<0.05):
            print("since the pvalue is <0.05 we reject nullhyp.so, there is a difference in performance <= different oils")
        else:
            print("pvalue>0.05,we accept null hyp,therefore there is no difference <=respect to oils")
    case 4:
        data=([207,282,241],[234,242,232])
        stat,p,dof,excepted=chi2_contingency(data)
        alpha=0.05
        print("pvalue is"+str(p))
        if p<=alpha:
            print("dependent reject H0")
        else:
            print("independent accept H0")

