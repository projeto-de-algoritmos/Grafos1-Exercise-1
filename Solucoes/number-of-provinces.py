class Solution:
    def findCircleNum(self, isConnected):
        # Função de busca em profundidade (DFS)
        def dfs(i):
            # Se o nó já foi visitado, retorne 0
            if i in visited:
                return 0
            # Marque o nó como visitado
            visited.add(i)
            # Para cada nó conectado ao nó atual, faça uma nova busca
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    dfs(j)
            # Retorne 1 para indicar que um novo grupo foi encontrado
            return 1
        
        # Conjunto para armazenar os nós visitados
        visited = set()
        # Contador para o número de províncias (grupos de cidades conectadas)
        provinces = 0
        
        # Para cada nó no grafo, faça uma busca em profundidade
        for i in range(len(isConnected)):
            provinces += dfs(i)
        
        # Retorne o número total de províncias
        return provinces
