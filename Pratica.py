import numpy as np #importa numpy, mas podemos chamar digitando apenas np

#cria matriz adiagonal de acordo com o vetor, com os elementos dele
def matrizDiagonal(vetor):
    return (np.diag(vetor))


def matrizDiagonalRaiz(vetor):
    saida=[]
    aux=[]
    for m in range(len(vetor)):
        for n in range(len(vetor)):
            if(m==n):
                aux.append(vetor[m])
            else:
                aux.append(0)
        saida.append(aux)
        aux=[]
    return(saida)

def printMatriz(matriz):
    print("[", end="")
    for m in range(len(matriz)):
        if(m!=0):
            print(" [", end="")
        else:
            print("[", end="")
        if(type(matriz[m])!=int or type(matriz[m])==float):
            for n in range(len(matriz[m])):
                print(matriz[m][n], end="")
        else:
            print(matriz[m], end ="]")
        if(m!=len(matriz)-1):
            print("")
    print("]")


def matrizLinha(vetor):   
    return np.array([vetor])

def matrizLinhaRaiz(vetor):
    saida=[]
    for m in range(len(vetor)):
        if(type(vetor[m])==int or type(vetor[m])==float):
            saida.append(vetor[m])
        else:
            for n in range(len(vetor[m])):
                saida.append(vetor[m][n])
    return saida

def matrizColuna(vetor):   
    return np.array([vetor])

def matrizColunaRaiz(vetor):
    aux=[]
    saida=[]
    for m in range(len(vetor)):
        if(type(vetor[m])==int or type(vetor[m])==float):
            aux=[vetor[m]]
            saida.append(aux)
        else:
            for n in range(len(vetor[m])):
                aux=vetor[m]
                saida.append(aux)
    return saida

def transposicaoMatriz(matriz):
    return np.transpose(matriz)

def transposicaoMatrizRaiz(matriz):
    saida = []
    aux=[]
    if(len(matriz)==1): # matriz linha, possui somente 1 linha
        for m in range (len(matriz)):
            if (type(matriz[m])==list):
                for n in range(len(matriz[m])):
                    aux=[matriz[m][n]]
                    saida.append(aux)
            else:
                aux=[matriz[m]]
                saida.append(aux)    
    else:   #caso possua mais de uma linha, é matriz coluna
        for m in range (len(matriz)):
            if (type(matriz[m])==list):
                for n in range(len(matriz[m])):
                    aux=[matriz[m][n]]
                    saida.append(matriz[m][n])
            else:
                aux=[matriz[m]]
                saida.append(matriz[m])
    return saida

#imprime matriz nula de ordem N M, ordem é vetor 1x2 
def matrizNula(ordem):
    return np.zeros(ordem)

def matrizNulaRaiz(ordem):
    saida=[]
    for m in range(ordem[0]):
        linha=[]
        for n in range(ordem[1]):
            linha.append(0)
        saida.append(linha)
    return saida

def matrizIdentidade(dimensao):
    return np.identity(dimensao)

def matrizIdentidadeRaiz(dimensao):#dimensao é o tamanho MN da matriz, inteiro
    saida=[]
    for m in range(dimensao):
        linha=[]
        for n in range(dimensao):
            if(m==n):
                linha.append(1)
            else:
                linha.append(0)
        saida.append(linha)
    return saida

def transposicaoMatriz(matriz):
    return (np.transpose(matriz))


#Cria uma matriz nula com m e n invertidos, depois preenche
def transposicaoMatrizRaiz(matriz):
    saida=matrizNula([len(matriz[0]),len(matriz)])
    for m in range(len(matriz)):
        for n in range(len(matriz[m])):
            saida[n][m]=matriz[m][n]
    return saida


def validacaoPropriedades(A, B):
    #matrizes são iguais?
    print(A==B)
    #soma transpostas
    print((A+B).T == A.T +B.T)
    #Transposta quadrada
    print((A.T).T==A)
    #Alfa e transposição
    print((56*A).T==56*A.T)
    #ordem multiplicação
    print((A*B).T==B.T*A.T)

def somaEscalar(matriz, escalar):
    aux = np.array(matriz)
    aux +=2
    return (aux)

def somaEscalarRaiz(matriz, escalar):
    for m in range(len(matriz)):
        for n in range(len(matriz[0])):
            matriz[m][n]+=escalar
    return matriz
                        
    
                
    
vetor = [[1,2],[3,4]]
#vetor=[[1],[2],[3],[4]]
matrizDiagonal([1,2,4,5])
matrizDiagonalRaiz([1,2,4,5])
matrizLinha(vetor)
matrizLinhaRaiz(vetor)
matrizColunaRaiz(vetor)
#printMatriz(transposicaoMatriz(vetor))
#print(transposicaoMatrizRaiz(vetor))
#print(matrizNula([2,3]))
#print(matrizNulaRaiz([2,2]))
#printMatriz(matrizIdentidade(10))
#print(transposicaoMatriz(vetor))
#print(transposicaoMatrizRaiz(vetor))

#A = np.array([[1,2],[3,4]])
#B = np.array([[5,6],[7,8]])
#validacaoPropriedades(A,B)

#print(somaEscalar(vetor, 2)
print(somaEscalarRaiz(vetor, 2))
