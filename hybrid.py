import matplotlib.pyplot  as plt
import numpy as np
import time as tm


class sorter:
    def insertion(self, arr: list[int])->list[int]:
        # print("Insertion sort start on array:")
        # print(arr)
        for i in range(1,len(arr)):
            j = i-1
            temp = arr[i]
            while j >= 0 and temp < arr[j]:  
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
        # print("after insertion sort the array is:")
        # print(arr)
        return arr
    
    def merge(self, arr1: list[int], arr2: list[int])->list[int]:
        temp = []
        p1, p2 = 0, 0
        while(p1<len(arr1) and p2<len(arr2)):
            if arr1[p1]<arr2[p2]:
                temp.append(arr1[p1])
                p1+=1
            else:
                temp.append(arr2[p2])
                p2+=1

        if p1<len(arr1):
            for i in range(p1, len(arr1)):
                temp.append(arr1[p1])
                p1+=1

        if p2<len(arr2):
            for i in range(p2, len(arr2)):
                temp.append(arr2[p2])
                p2+=1
        # print("after merging: ")
        # print(temp)
        return temp

    def hybridsort(self, arr: list[int], k: int) -> list[int]:
        
        n = len(arr)
        if n<k:
            return self.insertion(arr)
        else: 
            return self.merge(self.hybridsort(arr[0:(n//2)], k), self.hybridsort(arr[n//2:n], k))
    

class test:
    def test(self):
        fig, axs = plt.subplots(4,4)
        plt.xlabel('K Value')
        plt.ylabel('Average Time (s)')
        times = []
        ks = []
        for n in range(100, 1601, 100):
            # print("SIZE N IS SET TO n = " + str(n))
            y = []
            x = []
            for  k in range(5,100, 1):
                sumTimes = 0
                testSize = 30 # this controls how many times you do this to get the mean time value
                for i in range(testSize):
                    t = np.random.randint(0,100,n).tolist()
                    startTime = tm.perf_counter()
                    sorted = sorter().hybridsort(t,k)
                    endTime = tm.perf_counter()
                    time = endTime-startTime
                    sumTimes+=time
                meanTime = sumTimes/testSize
                y.append(meanTime)
                x.append(k)
                
            times.append(y)
            ks.append(x)

        axs[0, 0].scatter(ks[0], times[0])
        axs[0, 0].set_title('run time vs k of size 100')
        axs[0, 1].scatter(ks[1], times[1])
        axs[0, 1].set_title('run time vs k of size 200')
        axs[0, 2].scatter(ks[2], times[2])
        axs[0, 2].set_title('run time vs k of size 300')
        axs[0, 3].scatter(ks[3], times[3])
        axs[0, 3].set_title('run time vs k of size 400')
        axs[1, 0].scatter(ks[4], times[4])
        axs[1, 0].set_title('run time vs k of size 500')
        axs[1, 1].scatter(ks[5], times[5])
        axs[1, 1].set_title('run time vs k of size 600')
        axs[1, 2].scatter(ks[6], times[6])
        axs[1, 2].set_title('run time vs k of size 700')
        axs[1, 3].scatter(ks[7], times[7])
        axs[1, 3].set_title('run time vs k of size 800')

        axs[2, 0].scatter(ks[8], times[8])
        axs[2, 0].set_title('run time vs k of size 900')
        axs[2, 1].scatter(ks[9], times[9])
        axs[2, 1].set_title('run time vs k of size 1000')
        axs[2, 2].scatter(ks[10], times[10])
        axs[2, 2].set_title('run time vs k of size 1100')
        axs[2, 3].scatter(ks[11], times[11])
        axs[2, 3].set_title('run time vs k of size 1200')
        axs[3, 0].scatter(ks[12], times[12])
        axs[3, 0].set_title('run time vs k of size 1300')
        axs[3, 1].scatter(ks[13], times[13])
        axs[3, 1].set_title('run time vs k of size 1400')
        axs[3, 2].scatter(ks[14], times[14])
        axs[3, 2].set_title('run time vs k of size 1500')
        axs[3, 3].scatter(ks[15], times[15])
        axs[3, 3].set_title('run time vs k of size 1600')

        plt.show()



    def compare(self, arr1, arr2):
        if(len(arr1)!= len(arr2)):
            print("The array lengths do not match. ")
            return False
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                print("These arrays are not equivalent.")
                return False
        print("These arrays are equivalent. ")
        return True


if __name__ == "__main__":
    test().test()