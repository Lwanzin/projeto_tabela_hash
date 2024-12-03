# Tabelas para armazenar eleitores e votos dos candidatos
voter_register = {}
candidate_votes = {}

def vote(voter_id, candidate):
    # Verifica se o eleitor já votou
    if voter_id in voter_register:
        return "Erro: Eleitor já votou."
    
    # Marca o eleitor como tendo votado
    voter_register[voter_id] = True

    # Registra o voto para o candidato
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

    return f"Voto registrado para {candidate}!"

def show_result():
    print("Resultados da eleição:")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {votes} votos")

# Teste
print(vote("123", "Alice"))  # Deve registrar o voto
print(vote("123", "Bob"))    # Deve bloquear o voto
print(vote("456", "Bob"))    # Deve registrar o voto
show_result()
