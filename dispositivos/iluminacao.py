from time import sleep

def atuar(acao, objeto):
    print("Verificando se é um comando para iluminação...")
    sleep(1)
    
    sucesso = False
    if acao in ["ligar", "desligar", "acender", "apagar"] and objeto in ["iluminação"]:
        sucesso = True

    return sucesso
