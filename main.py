import pictures

print("CLI museum challenge\n")

while True:
    print("Informe um dos valores abaixo para observar os quadros respectivos:\n r - retangulo\n l - losango\n e - elipse\n b - sobrepostos\n x - sair")
    input_var = input("Desejo observar: ")

    match input_var:
        case "r":
            pictures.retangulo() # Prenchido com #. Possui largura de 40 colunas e altura de 20 linhas, centralizado na tela.
        case "l":
            pictures.losango() # Preenchido com ~. Possui diagonal horizontal de 40 colunas e diagonal vertical de 20 linhas, centralizado na tela.
        case "e":        
            pictures.elipse() # Apenas contorno com caracteres *. Possui raio horizontal de 10 colunas e raio vertical de 5 linhas, centralizado na tela.
        case "b":        
            pictures.sobrepostos() # Sobrepõe as três figuras acima na mesma tela, seguindo a ordem retângulo, losango e elipse. Caracteres de figuras posteriores substituem o que estiver na tela, mas espaços vazios não devem apagar o que já foi desenhado.
        case "x":        
            print("Agradecemos pelo visita ao museu CLI! Até a próxima!")
            break
        case _:        
            print("Caractere Inválido!")