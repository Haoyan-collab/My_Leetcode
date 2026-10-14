from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        q = deque()
        for classes in prerequisites:
            c, pre = classes
            graph[pre].append(c)
            indegree[c] += 1

        finished = 0

        for i,degree in enumerate(indegree):
            if degree == 0:
                q.append(i)
                finished += 1
                print(i)
        
        while q:
            pre = q.popleft()
            for i in graph[pre]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    finished += 1
                    print("append:",i)

        return finished == numCourses