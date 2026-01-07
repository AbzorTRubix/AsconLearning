def parse(X: str, r: int) -> list[str]:
    l = len(X)//r
    blocks = []
    for i in range(l):
        blocks.append(X[(i*r):((i+1)*r)])
    if len(X) % r != 0:
        blocks.append(X[(l*r):])
    return blocks

def pad(X: str, r: int) -> str:
    j = (-1*len(X) - 1) % r
    X_prime = "".join([X,"1",("0"*j)])
    return X_prime
