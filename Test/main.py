import time
import random
from openpyxl import Workbook
from Experiment_A.Sort_Algorithm import *
from Experiment_B.pack import *

functionList = [recursiveMergeSort, recursiveQuickSort, nonRecursiveMergeSort, nonRecursiveQuickSort]
n1 = [1000, 3000, 5000, 7000, 9000, 12000, 15000, 20000, 25000]
n2 = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 2000]

packWeight = 3000


def Test4A():
    print("实验A开始测试")
    print("时间单位：μs")
    res = []
    for eachN in n1:
        """生成随机数据"""
        randomData_1 = generateRandomData(eachN)
        """随机测试"""
        func_time = []
        # print("-----------------------")
        for eachFunc in functionList:
            # print(eachFunc.__name__)
            time1 = recordTime(eachFunc, randomData_1)
            func_time.append(round(time1*10**-3,2))
        res.append(func_time)

    print(res)
    return res


def Test4B():
    print("实验B开始测试")
    print("时间单位：ms")
    res = []
    for eachN in n2:
        """生成随机数据"""
        rVL = generateRandomData(eachN,randrange=800)
        rWL = generateRandomData(eachN,randrange=800)

        """随机测试"""
        time1 = recordTime(pack, rVL,rWL,packWeight,eachN-1)
        res.append(round(time1*10**-6,2))
    print(res)
    return res


def recordTime(function, *args):
    start = time.perf_counter_ns()
    function(*args)
    end = time.perf_counter_ns()
    return end-start


def generateRandomData(extent, randrange=100000):
    return [random.randrange(0, randrange) for x in range(extent)]


def getAVGTest4A(times=50):
    temp = np.mat(np.zeros((len(n1),len(functionList))))
    for i in range(times):
        print("-----------------------------------")
        print("the No.{} time".format(i + 1))
        t = np.mat(Test4A())
        temp+=t
    res = temp/times
    return res.T.tolist()


def getAVGTest4B(times=50):
    temp = np.mat(np.zeros((1,len(n2))))
    for i in range(times):
        print("-----------------------------------")
        print("the No.{} time".format(i+1))
        t = np.mat([Test4B()])
        temp += t
    res = temp / times
    return res.tolist()[0]


if __name__ == "__main__":
    times = 50
    res_A = getAVGTest4A(times)
    res_B = getAVGTest4B(times)

    wb = Workbook()
    ws = wb.active

    ws.append(["数据规模"]+n1)
    for i in range(len(res_A)):
        ws.append([functionList[i].__name__]+res_A[i])
    ws.append([])
    ws.append(["数据规模"]+n2)
    ws.append(["01pack"]+res_B)

    wb.save('result.xlsx')
    print("文件已写入")



