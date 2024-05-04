import os
os.system ('cls')

while True:
    print("--"*5,"CALCULADORA DE CONVERSÃO PARA DECIMAL:", 
          "--"*5)
    print('=='*30)
    print("                ==== MENU DE ESCOLHA ====                ")
    print('=='*30)
    print('''
    [ 1 ] - BINÁRIO
    [ 2 ] - OCTADECIMAL
    [ 3 ] - HEXADECIMAL
    [ 4 ] - CRÉDITOS
    [ 5 ] - FINALIZAR PROGRAMA
          ''')
    
    print('=='*30)
    print("Digite uma opção de conversão (1-5): ")
    opção = input('')
    print("=="*30)

    if opção == "1":
        bin = input("Insira um número binário: ")
        l = len(bin)
        dec = 0
        for i in bin:
            l = l - 1
            dec = dec + int(i)*2**l
        print('=='*30)        
        print(f"{bin}[2] é {dec}[10]")
        print('--'*30) 
        input("Pressione ENTER para voltar ao Menu !!")

    elif opção == "2":
        oct = input("Insira um número em Octadecimal: ")
        l = len(oct)
        dec = 0
        for i in oct:
            l = l - 1
            dec = dec + int(i)*8**l   
        print('=='*30) 
        print(f"{oct}[8] é {dec}[10]")
        print('--'*30) 
        input("Pressione ENTER para voltar ao Menu !!")

    elif opção == "3":
        hexa = input("Insira um número Hexadecimal: ")
        dec = int(hexa, 16)
        print('=='*30) 
        print(f"{hexa}[16] é {dec}[10]")
        print('--'*30) 
        input("ENTER para voltar ao MENU !!")

    elif opção =="4":
        print("[Curso: Análise e Desenvolvimento de Sistemas]")
        print('--'*30)
        print("[DESENVOLVIDO POR:]\n>> Gabriel Lima de Souza |RGM - 39389197|\n>> Gabriel Macedo Bastos |RGM - 37623451|\n>> Gustavo Akira Wendling Miyasaki |RGM - 38738091|\n>> Kayky de Oliveira Leonardo |RGM - 37732846|\n>> Pedro Soares Ribeiro |RGM - 38708787|")
        print('--'*30)
        print("[Disciplinas Envolvidas:]\n<Organização e Arquitetura de Computadores>\n<Programação de Computadores>")
        print('--'*30)
        print("[Versão do aplicativo:]\n> 1.0.1 <")
        print('--'*30)
        input("ENTER para voltar ao MENU !!")
        
    elif opção == "5":
        print("Programa Encerrado -_- !!")
        break
    
    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')
        input('\nPressione Enter para CONTINUAR...')
    
    


        