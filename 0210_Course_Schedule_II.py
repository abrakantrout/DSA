"""
Problem: Course Schedule II
LeetCode: 210
Difficulty: Medium

Topic:
- Graphs
- BFS
- Topological Sort
- Kahn's Algorithm
- Cycle Detection

Approach:
- Build a directed graph where prerequisite -> course.
- Calculate the indegree of every course.
- Start BFS with all courses having indegree 0.
- Process courses in topological order and reduce the indegree
  of their dependent courses.
- Add a course to the result when its indegree becomes 0.
- If all courses are processed, return the topological ordering.
- If some courses remain, a cycle exists, so return [].

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        indegree = [0] * numCourses

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != numCourses:
            return []

        return result