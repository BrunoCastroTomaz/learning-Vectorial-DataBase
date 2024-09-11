import numpy as np
import faiss

#Exemplo de criação de vetores aleatórios
num_vetores = 10 #número de vetores
dimensao = 32 #dimensão dos vetores

#Criação de vetores aleatórios
vetores = np.random.random((num_vetores, dimensao)).astype('float32')

#mostra os vetores criados
print(vetores)

#armazenar vetores em FAISS
index = faiss.IndexFlatL2(dimensao) #cria um index que usa a distância euclidiana para medir similaridade entre vetores
index.add(vetores) #adiciona os vetores ao index

#CONSULTA DE SIMILARIDADE

#criando um novo vetor de consulta 
consulta = np.random.random((1,dimensao)).astype('float32')

#busca pelos k vetores mais próximos
k = 5 #numeros de vetores mais próximos a encontrar
distancias, indices = index.search(consulta, k)

print(f"Indices dos vetores mais próximos: {indices}")
print(f"Distancias dos vetores mais proximos: {distancias}")

