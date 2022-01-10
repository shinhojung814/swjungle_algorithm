from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    
    for key, value in tickets:
        routes[key].append(value)
    
    for route in routes:
        routes[route].sort()
    
    stack = ["ICN"]
    path = []
    
    while stack:
        tmp = stack[-1]
        
        if not routes[tmp]:
            path.append(stack.pop())
        else:
            stack.append(routes[tmp].pop(0))
    
    answer = path[::-1]
    
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))