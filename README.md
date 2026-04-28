# Museu CLI

Este projeto é uma aplicação de terminal em Python que desenha figuras geométricas em uma grade de texto. O usuário pode escolher entre retângulo, losango, elipse ou uma imagem composta que sobrepõe as três figuras.

## Estrutura do Projeto

- `main.py` - Loop principal da aplicação, exibe o menu e chama as funções de desenho.
- `pictures.py` - Contém as funções que geram/desenham as figuras no terminal:
  - `retangulo()`
  - `losango()`
  - `elipse()`
  - `sobrepostos()`
- `utils.py` - Funções utilitárias de suporte ao desenho:
  - `bresenham()` - algoritmo de linha de Bresenham para gerar pontos de segmento.
  - `bresenham_elipse()` - algoritmo para gerar pontos de elipse.
  - `paint_losango()` - calcula as coordenadas das bordas do losango usando o algoritmo de Bresenham.

## Requisitos

- Python 3.10 ou superior.

## Como Executar

1. Abra um terminal na pasta do projeto.
2. Execute:

```bash
python main.py
```

3. Escolha uma opção no menu:

- `r` - desenha o retângulo.
- `l` - desenha o losango.
- `e` - desenha a elipse.
- `b` - desenha as três figuras sobrepostas.
- `x` - sai do programa.

