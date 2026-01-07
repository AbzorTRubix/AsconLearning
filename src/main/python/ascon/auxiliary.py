'''
Filename: auxiliary.py
Author: Nolan Attreed
Creation Date: 1/6/2025
Last Edit: 1/7/2025
Description: Contains definitions of the auxiliary functions defined in
SP.800-232 Section 2.1
'''
def parse(X: str, r: int) -> list[str]:
    '''
    Ascon Parse Auxiliary Function
    
    :param X: Binary string
    :type X: str
    :param r: Positive integer
    :type r: int
    :return: Parses blocks as defined in SP.800-232 Section 2.1
    :rtype: list[str]
    '''
    l = len(X)//r
    blocks = []
    for i in range(l):
        blocks.append(X[(i*r):((i+1)*r)])
    if len(X) % r != 0:
        blocks.append(X[(l*r):])
    return blocks

def pad(X: str, r: int) -> str:
    '''
    Ascon Pad Auxiliary Function
    
    :param X: Binary string
    :type X: str
    :param r: Positive Integer
    :type r: int
    :return: Padded block as defined in SP.800-232 Section 2.1
    :rtype: str
    '''
    j = (-1*len(X) - 1) % r
    X_prime = "".join([X,"1",("0"*j)])
    return X_prime
