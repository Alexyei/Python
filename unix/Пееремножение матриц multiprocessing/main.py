from multiprocessing import Pool
import os
import pickle

def save_matrix(filename, matrix):
    with open(filename, 'wb') as fp:
        pickle.dump(matrix, fp)

def load_matrix(filename):
    with open(filename, 'rb') as fp:
        return pickle.load(fp)

def main():
    # количество потоков процессора
    # print(os.cpu_count())
    # матрица A
    # A = [[1, 0], [2, 1], [-1, 1]]
    # # матрица B
    # B = [[1, 2, 0], [0, -1, 1]]

    # матрица A
    A = [[3, -1, 2], [4, 2, 0], [-5, 6, 1]]
    # # матрица B
    B = [[8, 1], [7,2],[2,-3]]

    save_matrix('matrixA', A)
    save_matrix('matrixB', B)
    # A = load_matrix('matrixA')
    # B = load_matrix('matrixB')

    p = Pool(processes=len(A)*len(B[0]))

    C = []
    for i in range(len(A)):
        C.append(p.starmap(getMulElement, [(A,B, i, j) for j in range(len(B[0]))]))
    print(C)
    save_matrix('matrixC', C)

    p.close()
    p.join()

def getMulElement(A,B,i:int, j:int):
    res = 0
    for k in range(len(B)):
        res += A[i][k]*B[k][j]
    return res

if __name__ == '__main__':
    main()


