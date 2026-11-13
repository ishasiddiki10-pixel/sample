G = {
    'E': ['TA'],
    'A': ['+TA', '#'],
    'T': ['FB'],
    'B': ['*FB', '#'],
    'F': ['(E)', 'i']
}
first, follow = {k : set() for k in G}, {k : set() for k in G}
def fs(s):
    r = set()
    for c in s:
        f = first[c] if c in G else {c}
        r.update(f - {"#"})
        if '#' not in f:
            return r
    return r | {'#'}
    
ch = True
while ch:
    ch = False
    for nt, prod in G.items():
        for p in prod:
            old = len(first[nt])
            first[nt].update(fs(p))
            if(len(first[nt])) != old:
                ch = True
        
ch = True
while ch:
    ch = False
    for nt, prod in G.items():
        for p in prod:
            for i, c in enumerate(p):
                if c in G:
                    old = len(follow[c])
                    b = p[i + 1 : ]
                    f = fs(b) if b else {'#'}
                    follow[c].update(f - {'#'})
                    if not b or '#' in f:
                        follow[c].update(follow[nt])
                    if(len(follow[c])) != old:
                        ch = True
print("FIRST : ", first)
print("FOLLOW : ", follow)
