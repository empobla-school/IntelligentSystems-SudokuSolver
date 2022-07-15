def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


if __name__ == '__main__':
    digits   = '123456789'
    rows     = 'ABCDEFGHI'
    cols     = digits

    # Array with all posible squares
    squares  = cross(rows, cols)

    # Array with all possible units (rows, columns, squares)
    unitlist = ([cross(rows, c) for c in cols] +
                [cross(r, cols) for r in rows] +
                [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
    
    # Map units to individual squares
    units = dict((s, [u for u in unitlist if s in u]) 
                for s in squares)
    
    # Peers are all units on which a square appears
    peers = dict((s, set(sum(units[s],[]))-set([s]))
                for s in squares)

    print(peers)