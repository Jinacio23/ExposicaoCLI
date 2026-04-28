# Utils
def bresenham(x0, y0, x1, y1):
    pontos = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        pontos.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return pontos

def bresenham_elipse(xc, yc, rx, ry):
    x = 0
    y = ry
    pontos = []

    # Quadrados dos raios para acelerar o cálculo
    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    def adicionar_4_pontos(xc, yc, x, y):
        return [(xc + x, yc + y), (xc - x, yc + y), 
                (xc + x, yc - y), (xc - x, yc - y)]

    # Região 1 (Inclinação < 1)
    p = round(ry2 - (rx2 * ry) + (0.25 * rx2))
    px = 0
    py = two_rx2 * y

    while px < py:
        pontos.extend(adicionar_4_pontos(xc, yc, x, y))
        x += 1
        px += two_ry2
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= two_rx2
            p += ry2 + px - py

    # Região 2 (Inclinação > 1)
    p = round(ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2)
    while y >= 0:
        pontos.extend(adicionar_4_pontos(xc, yc, x, y))
        y -= 1
        py -= two_rx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += two_ry2
            p += rx2 - py + px
            
    return pontos

def paint_losango(altura, largura):
    centro = [19,39]
    meia_altura = abs(altura // 2)
    meia_largura = abs(largura // 2)
    vetores = []
    all_cords_board = []
    ref = 1

    for x in range(4):
        arr = []
        if x == 0:
            x0 = abs(centro[0] - meia_altura)
            y0 = centro[1]
            arr.append([x0, y0])
        elif x == 1:
            x0 = centro[0]
            y0 = abs(centro[1] + meia_largura)
            arr.append([x0, y0])
        elif x == 2:
            x0 = abs(centro[0] + meia_altura)
            y0 = centro[1]
            arr.append([x0, y0])
        elif x == 3:
            x0 = centro[0]
            y0 = abs(centro[1] - meia_largura)
            arr.append([x0, y0])
            
        vetores.append(arr)

    for i, vetor in enumerate(vetores):
        if i == 3:
            ref = -3
        else:
            ref = 1

        next_vetor = vetores[i + ref]
        line = bresenham(vetor[0][0],vetor[0][1],next_vetor[0][0],next_vetor[0][1])
        all_cords_board.extend(line)

    return all_cords_board

import pictures