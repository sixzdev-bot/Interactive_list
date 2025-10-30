#Programa com 3 funções base: inserir, apagar e listar para dar fim ao programa

#Função para automatizar a mensagem principal do programa
def mensagem():
    print("\nSelecione uma opção")
    escolha = input('[i]nserir'" "'[a]pagar'" "'[l]istar: ').lower()
    return escolha

#Função para sempre checar se o input digitado pelo usuário é válido   
def checar_se_valido():
    opcao = mensagem() 
    opcoes_validas  = ["i", "a", "l"]
    while opcao not in opcoes_validas :
        print("\nInválido")
        opcao  = mensagem()
    return opcao

#lista vazia
lista = []

#Enquanto a condição for verdadeira, nosso programa rodará infinitamente
while True:
    acao = checar_se_valido() 
    inserir = acao == "i" 
    apagar = acao == "a"
    listar = acao == "l"  

    #Caso o usuário selecione '[i]nserir'
    if inserir:
        item = input("\nInsira um item na lista: ")
        lista.append(item) 
        print(f"{item} adicionado com sucesso.")

    #Checa se o usuário adicionou mais que item na lista para tratar de forma diferente
    mais_que_um_item = False    

    #Caso o usuário selecione '[a]pagar'
    if apagar:          
        #Caso a lista não possua itens
        if len(lista) < 1:
            print("\nNão tem oque apagar")
        #Caso a lista só possua um item    
        elif len(lista) == 1:
            um_item = lista[0]
            print(f"\nSua lista tem apenas: {um_item}")
            print(f"{um_item} apagado com sucesso.")
            lista.pop()
        else:
            mais_que_um_item = True

    #Esse if só acontece se o else de cima for verdadeiro, ou seja, se houver mais que um item na lista e o usuário selecionar
    #'[a]pagar'
    if mais_que_um_item == True:    

        print("\nNa sua lista tem: ")    
        #Lista todos os itens que o usuário tem na lista
        for indice, nome in enumerate(lista):
            print(indice+1, nome)

        #Checagem se é um inteiro
        try:
            selecao_apagar = int(input("\nQual indíce você quer apagar: "))  
        except ValueError:
            print("\n Oque você digitou não é um número")
            continue

        #Caso o número digitado seja maior que o número de itens na lista    
        if selecao_apagar > len(lista):
            print("Indice maior que o disponivel")
        #Caso o número digitado seja menor que o número de itens na lista        
        elif selecao_apagar < 1:
            print("Indíce menor que o disponivel")
        else:
            lista_apagada = lista.copy()
            lista.pop(selecao_apagar-1)
            print(f"{lista_apagada[selecao_apagar-1]} foi apagado[a]" )   

    #Checa se o usuário pode listar
    listar_valido = listar and len(lista) >= 1  #listar só é válido se o usuário apertar 'l' e tiver mais que um item na lista

    #Caso o usuário selecione [l]istar
    if listar:
        #Caso listar não seja válido
        if not listar_valido:
            print("\nNão tem oque listar")
            continue 
        #Print da lista formatada com índice e nome 
        else:    
            print("\nSua lista ficou assim: \n")
            for indice_final, nome_final in enumerate(lista): 
                print(f"Item {indice_final+1}:  {nome_final}")
            break 

     
            



      


               


                

   

