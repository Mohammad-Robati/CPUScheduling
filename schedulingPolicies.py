from math import inf


class SchedulingPolicies:

    def __init__(self, processes):
        self.processes = processes

    def fcfs(self):
        processes = self.processes
        order = []
        while len(processes) != 0:
            minStartTime = inf
            firstProcess = None
            for process in processes:
                if process['startTime'] < minStartTime:
                    minStartTime = process['startTime']
                    firstProcess = process
            order.append(firstProcess['pid'])
            processes.remove(firstProcess)
        return order

