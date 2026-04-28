import utils

# picture blank - pattern template
# for l in range(linhas):
#         for c in range(colunas):
#             if l == 0 or l == linhas - 1 or c == 0 or c == colunas - 1:
#                 print("*", end="") # borda
#             elif l == 19 and c == 39:
#                 print("*", end="") # meio
#             else:
#                 print(" ", end="") # interior vazio
#         print()

# Variables
linhas = 40 #40
colunas = 80 #80

# Functions
def retangulo(sobreposto=False):
    layers = []
    for l in range(linhas):
        layer = []
        for c in range(colunas):

            if l == 0 or l == linhas - 1 or c == 0 or c == colunas - 1:
                if sobreposto == False:
                    print("*", end="")
                else:
                    layer.append("*")
            elif l >= 9 and l <= 29 and c >= 19 and c <= 59:
                if sobreposto == False:
                    print("#", end="")                
                else:
                    layer.append("#")
            else:
                if sobreposto == False:
                    print(" ", end="")
                else:
                    layer.append(" ")

            if c == colunas - 1:
                layers.append(layer)

        if sobreposto == False:
            print()
    if sobreposto:
        return layers
    else:
        print("Retângulo gerado com sucesso!\n")
    

def losango(sobreposto=False): 
    layers = []

    diagonal_cords = utils.paint_losango(20, 40) 

    for l in range(linhas):
        layer = []
        left = None
        right = None
        for c in range(colunas): 
            if (l, c) in diagonal_cords: 
                if left is None: 
                    left = c 
                right = c 

        for c in range(colunas): 
            limit_cord = False 

            for cord in diagonal_cords: 
                if (l, c) == cord: 
                    limit_cord = True 
                    break 

            if limit_cord:
                if sobreposto == False:
                    print("~", end="")
                else:
                    layer.append("~")
            elif left is not None and right is not None and left < c < right:
                if sobreposto == False:
                    print("~", end="")
                else:
                    layer.append("~") 
            elif l == 0 or l == linhas - 1 or c == 0 or c == colunas - 1: 
                if sobreposto == False:
                    print("*", end="")
                else:
                    layer.append("*")
            else: 
                if sobreposto == False:
                    print(" ", end="")
                else:
                    layer.append(" ")

            if c == colunas - 1:
                layers.append(layer)

        if sobreposto == False:
            print()
    if sobreposto:
        return layers
    else:
        print("Losango gerado com sucesso!\n")

def elipse(sobreposto=False):
    layers = []

    elipse_cords = utils.bresenham_elipse(19, 39, 10, 5)

    for l in range(linhas):
        layer = []
        for c in range(colunas):

            limit_cord = False 

            for cord in elipse_cords: 
                if (l, c) == cord: 
                    limit_cord = True 
                    break 
                
            if limit_cord:
                if sobreposto == False:
                    print("*", end="")
                else:
                    layer.append("*")
            elif l == 0 or l == linhas - 1 or c == 0 or c == colunas - 1:
                if sobreposto == False:
                    print("*", end="")
                else:
                    layer.append("*")
            else:
                if sobreposto == False:
                    print(" ", end="")
                else:
                    layer.append(" ")

            if c == colunas - 1:
                layers.append(layer)

        if sobreposto == False:
            print()
    if sobreposto:
        return layers
    else:
        print("Elipse gerada com sucesso!\n")

def sobrepostos():
    ret_layers = retangulo(True)
    los_layers = losango(True)
    elip_layers = elipse(True)

    merged_layers = []
    merged_layers.append(ret_layers)
    merged_layers.append(los_layers)
    merged_layers.append(elip_layers)

    length_merges = len(merged_layers)

    changed_layers = []
    for i in range(length_merges):

        changes = merged_layers[i]

        for line in range(linhas):
            if changed_layers == [] and len(changes) > 1:
                changed_layers = changes
                continue
            changed_line = []
            for char in range(colunas):
                base_char = changed_layers[line][char]
                changed_char = changes[line][char]

                if base_char == " " and changed_char != " ":
                    changed_line.append(changed_char)
                elif base_char != " " and changed_char == " ":
                    changed_line.append(base_char)
                elif base_char != " " and changed_char != " ":
                    changed_line.append(changed_char)
                else:                   
                    changed_line.append(changed_char)
                
                if char == colunas - 1:
                    changed_layers[line] = changed_line

    for layer in changed_layers:
        line = ""
        for char in layer:
            line += char
        print(line)

    print("Sobreposição executada com sucesso!\n")