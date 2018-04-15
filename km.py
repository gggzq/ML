import numpy as np
import matplotlib.pyplot as plt

class Kmeans:
    def __init__(self,k,mu,data):
    # mu for center points,row for sample
    # data  row for sample
        self.k=k
        self.data=data
        if mu.shape[0]==k:
            self.mu=mu
        else:
            print('中心点数不够，将取前k个数据点作为中心点')
            self.mu=self.data[:k,:]

    def k_cluster(self):
        result={}
        n=self.data.shape[0]
        distance=np.zeros((1,self.k))
        for i in range(self.k):
            result[str(i)]=[]
        for i in range(n):
            distance=np.sum((self.mu-self.data[i,:])**2,1)
            result[str(np.argmin(distance))].append(self.data[i,:])
        return result

    def change_centers(self):
        result=self.k_cluster()
        centers=np.zeros((self.k,self.data.shape[1]))
        for i in range(self.k):
            centers[i,:]=np.mean(np.array(result[str(i)]),0)
        return centers

    def kms(self):
        flag=1
        while flag:
            centers=self.change_centers()
            if centers.all()!=self.mu.all():
                self.mu=centers
            else:
                flag=0
        result=self.k_cluster()
        print('聚类中心：')
        print(self.mu)
        print('各类点：')
        for i in range(self.k):
            print(str(i))
            print(result[str(i)])
    def show(self):
        # call it when your data is two-dimensional
        result=self.k_cluster()
        assert(self.data.shape[1]==2)
        for i in range(self.k):
            r=np.array(result[str(i)])
            plt.scatter(r[:,0],r[:,1])
        plt.show()

if __name__=='__main__':
    np.random.seed(0)
    data=np.random.standard_normal([50,2])
    kk=Kmeans(2,np.array([[-1,0],[1,0]]),data)
    kk.kms()
    kk.show()



















