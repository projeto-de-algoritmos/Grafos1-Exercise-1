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