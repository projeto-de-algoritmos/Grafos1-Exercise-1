class Solution:
    def allPathsSourceTarget(self, graph):
        # Inicializa a lista de resultados e a fila de busca
        result = []
        dq = deque([(0, [0])])

        # Define o alvo como o último nó do grafo
        target = len(graph) - 1

        # Enquanto houver nós na fila de busca
        while dq:
            # Remove o próximo nó da fila
            cur, route = dq.popleft()

            # Se o nó atual é o alvo, adiciona a rota ao resultado
            if cur == target:
                result.append(route)
            else:
                # Para cada nó adjacente ao nó atual, adiciona o nó e a rota atualizada à fila
                for node in graph[cur]:
                    dq.append((node, route + [node]))

        # Retorna a lista de todas as rotas possíveis do nó 0 ao nó alvo
        return result
