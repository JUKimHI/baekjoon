import math

def solution(signals):
    cycles = []
    for signal in signals:
        cycles.append(sum(signal))
    
    lcm = 1
    for num in cycles:
        lcm = lcm * num
    
    for t in range(1, lcm+1):
        all_yellow = True
        
        for g, y, r in signals:
            cycle = g + y + r
            pos = (t-1) % cycle + 1
            
            if not (g+1 <= pos <= g + y):
                all_yellow = False
                break
            
        if all_yellow:
            return t
    return -1