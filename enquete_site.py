# Simulação de enquete simples (Sim ou Não)

sim = 0
nao = 0

print("=== ENQUETE ===")
print("Você vai pro arraia da poica?")
print("Digite 'sim' ou 'nao'")
print("Digite 'sair' para encerrar a votação.\n")

while True:
    voto = input("Seu voto: ").strip().lower()
    
    if voto == "sim":
        sim += 1
        print("Voto registrado como SIM!\n")
    elif voto == "nao":
        nao += 1
        print("Voto registrado como NÃO!\n")
    elif voto == "sair":
        break
    else:
        print("Opção inválida! Digite apenas 'sim', 'nao' ou 'sair'.\n")

total = sim + nao

print("\n=== RESULTADO FINAL ===")
print(f"Total de votos: {total}")
print(f"Sim: {sim}")
print(f"Não: {nao}")

if total > 0:
    print(f"Percentual SIM: {(sim/total)*100:.1f}%")
    print(f"Percentual NÃO: {(nao/total)*100:.1f}%")
else:

    print("Nenhum voto foi registrado.")
