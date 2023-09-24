# Exercícios de Grafos 1

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
| Matrícula  |                              Aluno                               |
| :--------: | :--------------------------------------------------------------: |
| 19/0089601 | [João Lucas Pinto Vasconcelos](https://www.github.com/HacKairos) |

## Sobre 
Exercícios de Grafos, Resolvidos e explicados. Todos os exercícios foram retirados do online judge [Leet Code](https://leetcode.com/) e foi um total de três exercícios.

A linguagem utilizada na resolução dos 3 exercícios foi [Python](https://www.python.org/).

Não segui a risca o repositório [template](https://github.com/projeto-de-algoritmos/RepositorioTemplate) pois acreditei que alguns tópicos acabariam ficando obsoletos dentro do que realizei, como, por exemplo: Screenshots, Instalação, Uso e Outros.


## Exercícios

### [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/description/)

Você recebeu uma lista de passagens aéreas onde tickets[i] = [fromi, toi] representam os aeroportos de partida e chegada de um voo. Reconstrua o itinerário em ordem e retorne-o.

Todos os bilhetes pertencem a um homem que parte de “JFK”, portanto, o itinerário deve começar com “JFK”. Se houver vários itinerários válidos, você deve retornar o itinerário com a menor ordem lexical quando lido como uma única string.

- Por exemplo, o itinerário [“JFK”, “LGA”] tem uma ordem lexical menor do que [“JFK”, “LGB”]. 

Você pode assumir que todos os bilhetes formam pelo menos um itinerário válido. Você deve usar todos os bilhetes uma vez e apenas uma vez.

### [Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)

Existem n cidades. Algumas delas estão conectadas, enquanto outras não. Se a cidade a está conectada diretamente com a cidade b, e a cidade b está conectada diretamente com a cidade c, então a cidade a está conectada indiretamente com a cidade c.

Uma província é um grupo de cidades direta ou indiretamente conectadas e nenhuma outra cidade fora do grupo.

Você recebeu uma matriz n x n isConnected onde isConnected[i][j] = 1 se a cidade i e a cidade j estão diretamente conectadas, e isConnected[i][j] = 0 caso contrário.

Retorne o número total de províncias.

### [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-targeT/description/)

Dado um grafo acíclico direcionado (DAG) de n nós rotulados de 0 a n - 1, encontre todos os caminhos possíveis do nó 0 ao nó n - 1 e retorne-os em qualquer ordem.

O grafo é dado da seguinte forma: graph[i] é uma lista de todos os nós que você pode visitar a partir do nó i (ou seja, há uma aresta direcionada do nó i para o nó graph[i][j]).

## Soluções
### [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/description/)

#### Explicação

Um dicionário chamado “objetivos” é criado usando collections.defaultdict(list). Este dicionário será usado para mapear cada aeroporto de partida para uma lista de aeroportos de chegada.

Em seguida, percorremos todos os bilhetes, passados como entrada para a função, e os ordenamos inversamente (daqui à necessidade de reverse=True). Para cada bilhete, adicionamos o aeroporto de chegada à lista correspondente no dicionário objetivos.

Inicializamos uma lista vazia chamada rota para armazenar a rota final.

Definimos uma função chamada visita que toma um aeroporto como argumento e a utiliza para explorar os aeroportos adjacentes. O loop while na função percorre os aeroportos adjacentes, chamando recursivamente a função visita para cada um deles. Após visitar todos os aeroportos adjacentes, o aeroporto atual é adicionado à lista rota.

Iniciamos a busca chamando a função visita com o aeroporto 'JFK' como ponto de partida.

Finalmente, retornamos a rota, mas a revertendo usando rota[::-1] para obter a ordem correta dos aeroportos no itinerário de viagem.

#### [Solução](./Solucoes/reconstruct-itinerary.py)

```
class Solution:
        def findItinerary(self, tickets):
            # Cria um dicionário que mapeia cada aeroporto de partida para uma lista de aeroportos de chegada.
            objetivos = collections.defaultdict(list)
            
            # Preenche o dicionário com as informações dos bilhetes, ordenados inversamente.
            for a, b in sorted(tickets, reverse=True):
                objetivos[a].append(b)
            
            # Inicializa uma lista vazia para armazenar a rota.
            rota = []
            
            # Define uma função chamada visita para explorar os aeroportos.
            def visita(aeroporto):
                while objetivos[aeroporto]:
                    # visitae recursivamente o próximo aeroporto da lista.
                    visita(objetivos[aeroporto].pop())
                # Após visitaar todos os aeroportos adjacentes, adicione o aeroporto atual à rota.
                rota.append(aeroporto)
            
            # Inicia a busca a partir do aeroporto 'JFK'.
            visita('JFK')
            
            # A rota está inicialmente em ordem reversa, então a reverta antes de retornar.
            return rota[::-1]
```

### [Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)

#### Explicação

Primeiramente função dfs é definida para realizar a busca em profundidade a partir de um nó (cidade) específico i. Esta função tem o objetivo de encontrar todas as cidades conectadas ao nó i e marcar todas essas cidades como visitadas.

A função dfs(i) começa verificando se o nó i já foi visitado antes. Se sim, retorna 0, indicando que esse nó já foi incluído em uma província anteriormente. Se não, marca o nó i como visitado, adicionando-o ao conjunto visited.

Em seguida, a função dfs itera sobre todas as cidades possíveis (j) a partir do nó i. Se houver uma conexão entre i e j (ou seja, isConnected[i][j] é igual a 1), a função chama recursivamente dfs(j) para explorar a cidade j. Isso garante que todas as cidades conectadas a partir do nó i sejam visitadas e marcadas.

A função dfs retorna 1 no final, indicando que um novo grupo (província) foi encontrado a partir do nó i.

Fora da função dfs, é criado um conjunto vazio chamado visited para rastrear os nós visitados e um contador provinces para contar o número total de províncias.

Em seguida, um loop for é usado para iterar sobre todos os nós (cidades) no grafo, representados pelo comprimento de isConnected. Para cada nó, a função dfs(i) é chamada, onde i é o índice do nó atual. O valor retornado por dfs(i) é adicionado ao contador provinces.

No final do loop, o método findCircleNum retorna o valor de provinces, que representa o número total de províncias no grafo.

#### [Solução](./Solucoes/number-of-provinces.py)

```
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
```

### [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-targeT/description/)

#### Explicação

O código começa inicializando uma lista vazia result para armazenar os caminhos encontrados e uma fila dq para realizar a busca em largura (BFS). A fila é inicializada com um único caminho que começa no nó 0 e define o alvo como o último nó do grafo.

Entra em um loop enquanto houver caminhos na fila. Em cada iteração, ele remove o próximo caminho da fila e verifica se ele termina no nó alvo. Se sim, o caminho é adicionado à lista de resultados.

Se o caminho atual não terminar no nó alvo, o código percorre todos os nós adjacentes ao último nó do caminho atual e adiciona um novo caminho à fila para cada nó adjacente. Cada novo caminho é uma extensão do caminho atual com o nó adjacente adicionado ao final.

Após explorar todos os caminhos possíveis, o código retorna a lista de todos os caminhos que levam do nó 0 ao nó alvo.

#### [Solução](./Solucoes/all-paths-from-source-to-target.py)

```
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
```