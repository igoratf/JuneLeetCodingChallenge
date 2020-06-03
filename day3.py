def twoCitySchedCost(costs):
    cost = 0
    n = len(costs)
    p_costs = {

    }
    a_left = n // 2
    b_left = n // 2

    for i in range(n):
        p_costs[i] = max(costs[i][0], costs[i][1]) - min(costs[i][0], costs[i][1])
    
    sorted_p = sorted(p_costs.items(), key=lambda value: value[1], reverse=True)
    
    for j in range(n):
        current = costs[sorted_p[j][0]]
        a,b = current
        if min(a,b) == a:
            if a_left > 0:
                cost += a
                a_left -= 1
            else:
                cost += b
                b_left -= 1
        elif min(a,b) == b:
            if b_left > 0:
                cost += b
                b_left -= 1
            else:
                cost += a
                a_left -= 1
    return cost

# twoCitySchedCost([[10,20], [30,200], [400,50], [30,20]])
twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])