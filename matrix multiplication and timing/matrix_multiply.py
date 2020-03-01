matrix = [[2,5], [1,2]]



def transpose(matrix):
    length = len(matrix)
    answer = [[] for i in range(length)]
    for r in range(length):
        for c in range(length):
            answer[r].append(0)
    for r in range(length):
        for c in range(length):
            answer[r][c] = matrix[c][r]
            
    return answer

def square(matrix):
    trmatrix = transpose(matrix)
    length = len(matrix[0])
    answer = [[] for i in range(length)]
    for r in range(length):
        for c in range(length):
            answer[r].append(0)
    print(answer)

    sum = 0
    for i in range(length):
        for j in range(length):
            sum += matrix[i][j]*trmatrix[i][j]
            
            print(sum)
            answer[i][j] = sum
        sum = 0
    return answer

print(square(matrix))
        

    
