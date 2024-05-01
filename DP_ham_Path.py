def Hamiltonian_path(adj, N):
    dp = [[False for i in range(1 << N)] for j in range(N)]
    parent = [[-1 for i in range(1 << N)] for j in range(N)]

    # Set all dp[i][(1 << i)] to true and initialize parent
    for i in range(N):
        dp[i][1 << i] = True
        parent[i][1 << i] = i

    # Iterate over each subset of nodes
    for i in range(1 << N):
        for j in range(N):
            # If the jth node is included in the current subset
            if (i & (1 << j)) != 0:
                # Find K, neighbour of j also present in the current subset
                for k in range(N):
                    if (i & (1 << k)) != 0 and adj[k][j] == 1 and j != k and dp[k][i ^ (1 << j)]:
                        # Update dp[j][i] to true
                        dp[j][i] = True
                        parent[j][i] = k
                        break

    # Check for any endpoint with a full subset path
    for i in range(N):
        if dp[i][(1 << N) - 1]:
            # Path exists, reconstruct the path
            path = []
            current = i
            subset = (1 << N) - 1
            while subset:
                path.append(current)
                temp = subset
                subset ^= (1 << current)
                current = parent[current][temp]
            path.reverse()  # reverse to get the path from start to end
            print("YES")
            print("Path:", path)
            return True

    # If no path found
    print("NO")
    return False

# Example usage
adj = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]

N = len(adj)
Hamiltonian_path(adj, N)
