tree = [3, 5, 6, 9, 1, 2, 0, -1]

def minimax(depth, node, maximizing):

    if depth == 3:
        return tree[node]

    if maximizing:
        best = -999

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, False)
            best = max(best, value)

        return best

    else:
        best = 999

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, True)
            best = min(best, value)

        return best


# Main Program
result = minimax(0, 0, True)

print("Optimal Value:", result)

 