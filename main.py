from schedulingPolicies import SchedulingPolicies

numberOfProcesses = int(input())
processes = []
for i in range(numberOfProcesses):
    parts = input().split()
    processes.append({'pid': i, 'startTime': int(parts[0]), 'burstTime': int(parts[1])})

schedulingPolicies = SchedulingPolicies(processes)
print(schedulingPolicies.fcfs())