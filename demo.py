class Solution:
    def findCircleNum(self, isConnected):

        n = len(isConnected)

        visited = set()
        provinces = 0

        def dfs(node):

            # Mark current city as visited
            visited.add(node)

            # Check every possible neighbor
            for neighbor in range(n):

                # If there is a connection
                # and the city hasn't been visited
                if isConnected[node][neighbor] == 1 and neighbor not in visited:

                    # Explore that city
                    dfs(neighbor)


        # Check every city
        for city in range(n):

            # If we haven't visited this city,
            # we found a new province
            if city not in visited:

                provinces += 1

                # Explore the entire province
                dfs(city)

        return provinces


isConnected = [[1,1,0],[1,1,0],[0,0,1]]