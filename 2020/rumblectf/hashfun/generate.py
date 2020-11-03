
FLAG = [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
def hashfun(msg):
    digest = []
    for i in range(len(msg) - 4):
        digest.append(ord(msg[i]) ^ ord(msg[i + 4]))
    return digest

# def dehashfun(msg):
    
        
#     return solution
# print(dehashfun(FLAG))
# print(hashfun(FLAG))

def solve(msg):

    solution = 'CSR{'
    for i in range(len(msg)):

        

        for j in range(100):
            if ord(solution[i]) ^ j == msg[i]:
                solution += chr(j)
                print(solution)
        
    return solution + '}'

print(solve(FLAG))

# [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]
# [CSR{I}]