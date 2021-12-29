def solution(number, k):
    answer = ''
    stack = []
    count = 0
    
    for num in number:
        if count == k:
            stack.append(num)
            continue
        
        if len(stack) == 0:
            stack.append(num)
        else:
            if stack[len(stack) - 1] >= num:
                stack.append(num)
            else:
                while stack[len(stack) - 1] < num:
                    count += 1
                    stack.pop()
                    
                    if count == k:
                        break
                    if len(stack) == 0:
                        break
                stack.append(num)
    
    if count != k:
        answer = ''.join(stack[:len(number) - k])
        return answer
    
    answer = ''.join(stack)
    return answer

