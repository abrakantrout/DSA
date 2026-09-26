"""
Problem: Course Schedule
LeetCode: 207
Difficulty: Medium

Topic:
- Graphs
- BFS
- Topological Sort
- Kahn's Algorithm
- Cycle Detection

Approach:
- Treat each course as a node and each prerequisite relationship
  as a directed edge.
- Build an adjacency list and calculate the indegree of every course.
- Start BFS with all courses having indegree 0.
- When a course is completed, reduce the indegree of its neighbors.
- If a neighbor reaches indegree 0, add it to the queue.
- If all courses can be processed, the graph has no cycle and all
  courses can be completed.
- If some courses remain unprocessed, a cycle exists.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        indegree = [0] * numCourses

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses