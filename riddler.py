import numpy as np
import matplotlib.pyplot as plt

dN = int(20)
nSamps = int(1e5)

#One dice
sampTosses = [np.random.randint(low=1,high=dN+1) for i in range(nSamps)]
plt.hist(sampTosses,100);
print(np.mean(sampTosses))

#Disadvantage
sampTosses = [min(np.random.randint(low=1,high=dN+1),np.random.randint(low=1,high=dN+1)) for i in range(nSamps)]
plt.hist(sampTosses,100);
print(np.mean(sampTosses))

#Advantage
sampTosses = [max(np.random.randint(low=1,high=dN+1),np.random.randint(low=1,high=dN+1)) for i in range(nSamps)]
plt.hist(sampTosses,100);
print(np.mean(sampTosses))

#Advantage of disadvantage
sampTosses = [max(min(np.random.randint(low=1,high=dN+1),np.random.randint(low=1,high=dN+1)),min(np.random.randint(low=1,high=dN+1),np.random.randint(low=1,high=dN+1))) for i in range(nSamps)]
plt.hist(sampTosses,100);
print(np.mean(sampTosses))


#Disadvantage of advantage
sampTosses = [min(max(np.random.randint(low=1,high=dN+1),np.random.randint(low=1,high=dN+1)),max(np.random.randint(low=1,high=dN+1),np.random.randint(low=1,high=dN+1))) for i in range(nSamps)]
plt.hist(sampTosses,100);
print(np.mean(sampTosses))

#Disadvantage
EV = 0
prob = dN*2-1
for i in range(1,dN+1):
  EV = EV+i*prob/(dN*dN)
  prob = prob-2
print(EV)

#Advantage
EV = 0
prob = 1
for i in range(1,dN+1):
  EV = EV+i*prob/(dN*dN)
  prob = prob+2
print(EV)

maxProb = [0]*dN
for i in range(0,dN):
  maxProb[i] = (2*(i+1)-1)*(2*(i+1)-1)+sum([2*(2*(i+1)-1)*(2*j-1) for j in range(i+2,dN+1)])

minProb=maxProb.copy()
minProb.reverse()

minEV = 0
maxEV = 0
for i in range(1,dN+1):
  minEV = minEV+i*minProb[i-1]/(dN**4)
  maxEV = maxEV+i*maxProb[i-1]/(dN**4)
print(minEV,maxEV)

plt.figure(1)
plt.axis([0, dN+1, 0, 2/dN]);
plt.plot(range(1,dN+1),[mp/(dN**4) for mp in maxProb],'-o');
plt.plot(range(1,dN+1),[mp/(dN**4) for mp in minProb],'-o');
plt.plot(range(1,dN+1),[1/dN]*dN,'-o');
plt.xticks(np.arange(0, dN+1, 1));
plt.legend(('D of A','A of D', 'Single'));

cumProbSingle = list(np.cumsum([1/dN]*dN))
cumProbSingle.reverse()
cumProbDoA = list(np.cumsum([mp/(dN**4) for mp in maxProb][::-1]))
cumProbDoA.reverse()
cumProbAoD = list(np.cumsum([mp/(dN**4) for mp in minProb][::-1]))
cumProbAoD.reverse()

plt.figure(2)
plt.axis([0, dN+1, 0, 1.01]);
plt.plot(range(1,dN+1),cumProbDoA,'-o');
plt.plot(range(1,dN+1),cumProbAoD,'-o');
plt.plot(range(1,dN+1),cumProbSingle,'-o');
plt.xticks(np.arange(0, dN+1, 1));
plt.legend(('D of A','A of D', 'Single'));
