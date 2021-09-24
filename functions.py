'''
Funcões que retornam a soma maxima e as posições para o retorno
'''

def max_sum(b=dict()):
    A=b.copy()
    max_so_far = 0
    max_ending_here = 0
    min_value=A['lista'][0]

    for i in A['lista']:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
    if A['lista'][0] < 0 and A['lista'][1] < 0 and A['lista'][2] < 0 and A['lista'][3] < 0 and A['lista'][4] < 0:
        for i in A['lista']:
            if i > min_value:
                min_value=i
        return min_value

    else:
        return max_so_far

def position(b):
    A=b.copy()
    max_ending_here = 0
    min_value=A['lista'][0]
    positions=[]
    count=0
    
    for i in A['lista']:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        if max_ending_here != 0:
            positions.append(count)
        count+=1
    count=0
    if A['lista'][0] < 0 and A['lista'][1] < 0 and A['lista'][2] < 0 and A['lista'][3] < 0 and A['lista'][4] < 0:
        for i in A['lista']:
            if i > min_value:
                min_value=i
                positions.append(count)
            count+=1
        return positions

    else:
        return positions