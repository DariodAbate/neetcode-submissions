import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = defaultdict(int)
        for task in tasks:
            freqs[task] += 1

        avails = [] # stores [freq, task]
        for task in freqs:
            heapq.heappush_max(avails, [freqs[task] , task])

        cooldowns = deque() # stores [avail_cycle, task]

        cycles = 0
        while avails or cooldowns:
            cycles += 1
            # check for tasks that are available now
            while cooldowns and cooldowns[0][0] <= cycles:
                avail_cycle, task = cooldowns.popleft()
                heapq.heappush_max(avails, [freqs[task], task])

            # pick most frequent task first
            if avails:
                task_freq, task = heapq.heappop_max(avails)
                freqs[task] -= 1
                if freqs[task] > 0:
                    cooldowns.append([cycles + n + 1, task])
            elif cooldowns: # avoid unnecessary cycles
                cycles = cooldowns[0][0] - 1

            
        return cycles



