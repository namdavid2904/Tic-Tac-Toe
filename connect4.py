def make_empty_board(nrows, ncols):
    s = []
    for i in range(nrows):
        s.append('.'*ncols)
    return s

def print_board(l):
    for i in range(len(l)):
        if i != len(l) - 1:
            for j in range(len(l[i])):
                if j != len(l[i]) - 1:
                    if l[i][j] == 'O':
                        print(' O', end=' |')
                    elif l[i][j] == 'X':
                        print(' X', end=' |')
                    else: 
                        print(' ', end='  |')
                else:
                    if l[i][j] == 'O':
                        print(' O', end='\n')
                    elif l[i][j] == 'X':
                        print(' X', end='\n')
                    else: 
                        print('  ', end='\n')
            for j in range(len(l[i])):
                if j != len(l[i]) - 1:
                    print('---+', end='')
                else:
                    print('---', end='\n')
        else:
            for j in range(len(l[i])):
                if j != len(l[i]) - 1:
                    if l[i][j] == 'O':
                        print(' O', end=' |')
                    elif l[i][j] == 'X':
                        print(' X', end=' |')
                    else: 
                        print(' ', end='  |')
                else:
                    if l[i][j] == 'O':
                        print(' O', end='\n')
                    elif l[i][j] == 'X':
                        print(' X', end='\n')
                    else: 
                        print('  ', end='\n')

def verify_board(l):
    count_O = sum(i.count('O') for i in l)
    count_X = sum(i.count('X') for i in l) 
    if abs(count_O - count_X) > 1:
        return False
    for i in range(len(l) - 1):
      for j in range(len(l[i])):
        if ((l[i][j] != '.') and (l[i+1][j] == '.')):
          return False
    return True

def verify_move(l, id):
    if id < 0 or id > len(l[0]) - 1:
        return False
    else:
        for i in l:
            if i[id] == '.':
                return True
    return False
        
def update_board(l, id, d):
    s = [i for i in range(len(l)) if l[i][id] == '.']
    l[max(s)] = list(l[max(s)])
    l[max(s)][id] = d
    l[max(s)] = ''.join(l[max(s)])
    return l

def has_won(l, id):
    k = next((i for i, row in enumerate(l) if row[id] != '.'), None)
    if k is None:
        return False

    d = l[k][id]
    if k <= len(l) - 4 and all(l[k + i][id] == d for i in range(1, 4)):
        return True
    
    count = 1
    for i in [-1, 1]:
        count -= 1
        for j in range(id, -1 if i < 0 else len(l[0]), i):
            if l[k][j] == d:
                count += 1
                if count == 4:
                    return True
            else:
                break

    count = 1
    for i, j in [(1, -1), (-1, 1)]:
        count -= 1
        a, b = k, id
        while 0 <= a < len(l) and 0 <= b < len(l[0]):
            if l[a][b] == d:
                count += 1
                if count == 4:
                    return True
            else:
                break
            a += i
            b += j
    
    count = 1        
    for i, j in [(-1, -1), (1, 1)]:
        count -= 1
        a, b = k, id
        while 0 <= a < len(l) and 0 <= b < len(l[0]):
            if l[a][b] == d:
                count += 1
                if count == 4:
                    return True
            else:
                break
            a += i
            b += j

    return False
