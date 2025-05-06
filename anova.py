import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

print("1.probabiliy")
print("2.normal distribution")
print("3.binomial distribution")
print("4.poission distribution")
print("5.exit")
user_choice=int(input("enter your choice:"))
match user_choice:
    case 1:
        n=int(input("enter the total no of outcomes:"))
        e=int(input("enter the no of desired outcomes:"))
        if e>n:
            print("invalid input")
        else:
            print("the probability of the event is:",e/n)
    case 2:
        data=stats.norm(scale=1,loc=0).rvs(1000)
        dx=sns.displot(data,bins=50,kde=True,color='red')
        dx.set(xlabel='Normal Distribution',ylabel='frequency')
        plt.show()
    case 3:
        n,p=1000,0.003
        data=np.random.binomial(n,p,100)
        dx=sns.displot(data,bins=20,kde=False,color='red')
        dx.set(xlabel="binomial distribution",ylabel="frequency")
        plt.show()
    case 4:
        poisson_data=np.random.poisson(lam=5,size=1000)
        dx=sns.displot(poisson_data,kde=True,color='red')
        dx.set(xlabel='poisson dist',ylabel='frequency')
        plt.show()
    case 5:
        print("exit")