# Definindo as variáveis de teste (você pode alterar os valores para testar)
bateria_atual = 10  # Exemplo: número inteiro de 0 a 100
bola_em_jogo = True  # Exemplo: True ou False

# Processando as condições de forma ordenada (If / Elif / Else)
if bateria_atual < 15 and bola_em_jogo == True:
    print("ALERTA MÁXIMO. Bateria baixa! Substitua a bola na próxima paralisação.")
elif bateria_atual < 15 and bola_em_jogo == False:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")
else:
    print("Sistema Trionda operando normalmente. Bateria ok.")
