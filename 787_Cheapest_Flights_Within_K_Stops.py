"""
Problem: Cheapest Flights Within K Stops
LeetCode: 787
Difficulty: Medium

Topic:
- Graphs
- Bellman-Ford
- Shortest Path
- Limited Number of Edges

Approach:
- A route with at most k stops can contain at most k + 1 flights.
- Relax every flight exactly k + 1 times.
- Use a copy of the distance array for each iteration so that
  one iteration represents only one additional flight.
- If the destination remains unreachable, return -1.

Time Complexity: O(k * E)
Space Complexity: O(V)
"""

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        distance = [float('inf')] * n
        distance[src] = 0

        max_flights = k + 1

        while max_flights:
            new_dist = distance.copy()

            for s, d, price in flights:
                if distance[s] == float('inf'):
                    continue

                new_cost = distance[s] + price

                if new_cost < new_dist[d]:
                    new_dist[d] = new_cost

            distance = new_dist
            max_flights -= 1

        if distance[dst] == float('inf'):
            return -1

        return distance[dst]