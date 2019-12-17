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
        return order

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
        return order

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
        return order

    def roundRobin(self, quantom):
        processes = deepcopy(self.processes)
        processes = sorted(processes, key=lambda i: (i['startTime']))
        currTime = 0
        idle = True
        order = []
        while len(processes) != 0:
            for process in processes:
                if process['startTime'] <= currTime:
                    order.append(process['pid'])
                    currTime += min(quantom, process['burstTime'])
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
        return order
