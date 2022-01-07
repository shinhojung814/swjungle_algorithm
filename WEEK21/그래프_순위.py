from collections import defaultdict

def solution(n, results):
    answer = 0
    graph_winner = defaultdict(set)
    graph_loser = defaultdict(set)
    
    for winner, loser in results:
        graph_winner[loser].add(winner)
        graph_loser[winner].add(loser)
    
    for i in range(1, n + 1):
        for winner in graph_winner[i]:
            graph_loser[winner].update(graph_loser[i])
        for loser in graph_loser[i]:
            graph_winner[loser].update(graph_winner[i])
    
    for j in range(1, n + 1):
        if len(graph_winner[j]) + len(graph_loser[j]) == n - 1:
            answer += 1
    
    return answer