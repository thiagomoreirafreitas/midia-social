#!/usr/bin/python
# -*- coding: UTF-8 -*-
import networkx as nx
import io

#Função que calcula overlap de cada aresta do grafo
def overlap(H, edge):
    node_i = edge[0]
    node_j = edge[1]
    degree_i = H.degree(node_i)
    degree_j = H.degree(node_j)
    neigh_i = set(H.neighbors(node_i))
    neigh_j = set(H.neighbors(node_j))
    neigh_ij = neigh_i & neigh_j
    num_cn = len(neigh_ij)
    if degree_i > 1 or degree_j > 1:
        return float(num_cn) / (degree_i + degree_j - num_cn - 2)
    else :
        return 2
    
#Função que calcula o grau de cada nó do grafo   
def grau(diretorio,G):
    i=0
    
    grau = nx.degree(G)#Obtém o grau de cada nó do grafo
    
    #Salva o conteudo em arquivo
    for g in grau:
        arq = open(diretorio,'a')
        aux=grau.values()[i]
        arq.write(str(aux))
        arq.write('\n')
        i=i+1
        arq.close()
        
    #Imprime na tela o resultado    
    print '\n\nGrau dos nós'
    print grau
    
def cluster(diretorio,G):
    j=0
    
    clust = nx.clustering(G)#Obtém o coeficiente de clusterização de cada nó do grafo
    
    #Salva o conteudo em arquivo
    for c in clust:
        arq2 = open(diretorio,'a') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
        aux2=clust.values()[j]
        arq2.write(str(aux2))
        arq2.write('\n')
        j=j+1
        arq2.close()
        
    #Imprime na tela o resultado     
    print '\n\nCoeficiente de Clusterização'
    print clust
    
#Função que chama a função de calcular overlap de cada aresta, calculando o overlap de cada aresta do grafo    
def ovlap(diretorio,G):
    
    print '\n\nOverlap'
    
    #Salva o conteudo em arquivo e imprime o overlap de cada aresta na tela
    for e in G.edges():
        arq3 = open(diretorio,'a')
        aux=overlap(G,e)
        
        if aux <> 2:
            print aux
            arq3.write(str(aux))
            arq3.write('\n')
        arq3.close()
        
    

        
G = nx.read_edgelist('grafo/Wiki-Vote.txt') #Carregando o arquivo que contém o grafo

diretorio1 = 'Arquivos/grau.txt'#Diretório para salvar arquivo contendo o grau de cada nó do grafo
diretorio2 = 'Arquivos/culst.txt'#Diretório para salvar arquivo contendo o coeficiente de clusterização de cada nó do grafo
diretorio3 = 'Arquivos/over.txt'#Diretório para salvar arquivo contendo o overlap de cada nó do grafo

#Chamada das Funções
grau(diretorio1, G)
cluster(diretorio2, G)
ovlap(diretorio3, G)
print "Coeficiente de clusterização global = ", nx.transitivity(G)






