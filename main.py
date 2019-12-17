from schedulingPolicies import SchedulingPolicies

numberOfProcesses = int(input())
processes = []
for i in range(numberOfProcesses):
    parts = input().split()
    processes.append({'pid': i, 'startTime': int(parts[0]), 'burstTime': int(parts[1]), 'priority': int(parts[2])})


schedulingPolicies = SchedulingPolicies(processes)
print('------\nFCFS:')
schedulingPolicies.firstComeFirstServe()
print('------')
print('SJF:')
schedulingPolicies.shortestJobFirst()
print('------')
print('Priority:')
schedulingPolicies.priority()
print('------')
print('Round Robin:')
schedulingPolicies.roundRobin(3)
print('------')



# 4
# 2 5 1
# 2 2 4
# 0 2 2
# 1 4 3

# 4
# 2 5 1
# 2 2 4
# 0 2 2
# 1 20 3

