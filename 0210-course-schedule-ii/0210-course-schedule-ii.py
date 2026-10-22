from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        path = []
        for sec,fst in prerequisites:
            indegree[sec] += 1
            graph[fst].append(sec)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            path.append(cur)
            for sec in graph[cur]:
                indegree[sec] -= 1
                if indegree[sec] == 0:
                    q.append(sec)
        return path if len(path) == numCourses else []