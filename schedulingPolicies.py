from copy import deepcopy


class SchedulingPolicies:

    def __init__(self, processes):
        self.processes = processes

    def firstComeFirstServe(self):
        processes = deepcopy(self.processes)
        order = []
        processes = sorted(processes, key=lambda i: i['startTime'])
        for process in processes:
            order.append(process['pid'])
        print('Order:', order)
        self.calculateAverage(order)

    def shortestJobFirst(self):
        processes = deepcopy(self.processes)
        processes = sorted(processes, key=lambda i: (i['burstTime'], i['startTime']))
        currTime = 0
        idle = True
        order = []
        while len(processes) != 0:
            for process in processes:
                if process['startTime'] <= currTime:
                    order.append(process['pid'])
                    currTime += process['burstTime']
                    idle = False
                    processes.remove(process)
                    break
            if idle:
                currTime += 1
                idle = True
        print('Order:', order)
        self.calculateAverage(order)

    def priority(self):
        processes = deepcopy(self.processes)
        processes = sorted(processes, key=lambda i: (i['priority'], i['startTime']))
        currTime = 0
        idle = True
        order = []
        while len(processes) != 0:
            for process in processes:
                if process['startTime'] <= currTime:
                    order.append(process['pid'])
                    currTime += process['burstTime']
                    idle = False
                    processes.remove(process)
                    break
            if idle:
                currTime += 1
                idle = True
        print('Order:', order)
        self.calculateAverage(order)

    def roundRobin(self, quantom):
        processes = deepcopy(self.processes)
        processes = sorted(processes, key=lambda i: (i['startTime']))
        currTime = 0
        idle = True
        order = []
        timings = []
        while len(processes) != 0:
            for process in processes:
                if process['startTime'] <= currTime:
                    order.append(process['pid'])
                    currTime += min(quantom, process['burstTime'])
                    timings.append(min(quantom, process['burstTime']))
                    idle = False
                    needed = process['burstTime'] - quantom
                    processes.remove(process)
                    if needed > 0:
                        process['burstTime'] = needed
                        processes.append(process)
                    break
            if idle:
                currTime += 1
                idle = True
        print('Order:', order)
        self.calculateRoundRobinAverage(order, timings)

    def calculateAverage(self, order):
        processes = self.processes
        waitingTimes = [0 for i in range(len(self.processes))]
        turnAroundTimes = [0 for i in range(len(self.processes))]
        for i in range(0, len(order)):
            tmp = 0
            for j in range(0, i):
                tmp += processes[order[j]]['burstTime']
            waitingTimes[order[i]] += max(tmp - processes[order[i]]['startTime'], 0)
            turnAroundTimes[order[i]] = processes[order[i]]['burstTime'] + waitingTimes[order[i]]
        sum = 0
        for waitingTime in waitingTimes:
            sum += waitingTime
        averageWaitingTime = sum / len(waitingTimes)
        print('Waiting Times:', waitingTimes)
        print('Turnaround Times:', turnAroundTimes)
        print('Average Waiting Time:', averageWaitingTime)

    def calculateRoundRobinAverage(self, order, timings):
        processes = deepcopy(self.processes)
        processes = sorted(processes, key=lambda i: (i['pid']))
        waitingTimes = [0 for i in range(len(self.processes))]
        for i in range(0, len(processes)):
            time = 0
            for j in range(0, len(order)):
                if i == order[j]:
                    waitingTimes[i] = time - processes[i]['startTime']
                    break
                else:
                    time += timings[j]
        sum = 0
        for waitingTime in waitingTimes:
            sum += waitingTime
        averageWaitingTime = sum / len(waitingTimes)
        print('Waiting Times:', waitingTimes)
        print('Average Waiting Time:', averageWaitingTime)
