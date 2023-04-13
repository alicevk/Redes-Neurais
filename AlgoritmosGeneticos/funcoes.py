# Imports:

import random

# Funções:

# ------------------------------- SUPORTE:

def distânciaDoisPontos(a, b):
    ''' Esta função computa a distância Euclidiana entre dois pontos em R^2.

    Args:
        a: lista contendo as coordenadas x e y de um ponto.
        b: lista contendo as coordenadas x e y de um ponto.

    Returns:
        Distância entre as coordenadas dos pontos `a` e `b`.
    '''
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def criaCidades(n):
    ''' Esta função cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
        n: número de cidades que serão visitadas pelo caixeiro.

    Return:
        Dicionário contendo o nome das cidades como chaves e a coordenada no plano
        cartesiano das cidades como valores.
    '''
    cidades = {}
    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades

def computaMochila(indivíduo, objetos, ordem_dos_nomes):
    ''' Esta função computa o valor total e peso total de uma mochila.
    
    Args:
        indivíduos: lista binária contendo a informação de quais objetos serão selecionados.
        objetos: Dicionário onde as chaves são os nomes dos objetos e os valores são
    dicionários com a informação do peso e valor.
        ordem_dos_nomes: lista contendo a ordem dos nomes dos objetos.

    Returns:
        valor_total: valor total dos itens da mochila em unidades de dinheiros.
        peso_total: peso total dos itens da mochila em unidades de massa.
        '''
    valor_total = 0
    peso_total = 0
    for pegou_o_item_ou_não, nome_do_item in zip(indivíduo, ordem_dos_nomes):
        if pegou_o_item_ou_não == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            valor_total += valor_do_item
            peso_total += peso_do_item

    return valor_total, peso_total


# ------------------------------- GENE:

def gene_cb():
    ''' Esta função gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor 0 ou 1.
    '''
    valoresPossíveis = [0, 1]
    gene = random.choice(valoresPossíveis)

    return gene


def gene_cnb(x):
    ''' Esta função gera um gene válido para o problema das caixas não-binárias.
    
    Args:
        x: valor máximo para cada gene.

    Return:
        Um valor inteiro aleatório de 0 a x.
    '''
    gene = random.randint(0,x)

    return gene


def gene_letra(letras):
    ''' Esta função sorteia uma letra entre as possíveis.

    Args:
        letras: letras possíveis de serem sorteadas.

    Return:
        Uma letra sorteada entre as possíveis.
    '''
    letra = random.choice(letras)

    return letra


def gene_ligaElemento(elementos):
    ''' Esta função sorteia um elemento entre os possíveis para o problema da liga
    ternária.

    Args:
        elementos: elementos possíveis de serem sorteados.

    Return:
        Um elemento aleatório sorteado entre os possíveis.    
    '''
    elemento = random.choice(elementos)

    return elemento


def gene_ligaNúmero(x, y):
    ''' Esta função sorteia um número para a proporção dos elementos no problema da liga
    ternária.
    
    Args:
        x: primeiro número já sorteado (caso haja algum).
        y: segundo número já sorteado (caso haja algum).
        
    Return:
        Um número aleatório possível para a proporção dos elementos que seja maior do que
        5 e tal que x + y + z = 100.
    '''
    máximo = 91 - (x + y)
    if (x!=0) and (y!=0):
        número = máximo
    else:
        número = random.randint(6,91)

    return número


# ------------------------------- INDIVÍDUO:

def indivíduo_cb(n):
    ''' Esta função gera um indivíduo para o problema das caixas binárias.
    
    Args:
        n: número de genes de cada indivíduo.

    Return:
        Uma lista com n genes.
    '''
    indivíduo = []
    for _ in range(n):
        gene = gene_cb()
        indivíduo.append(gene)

    return indivíduo


def indivíduo_cnb(n, x):
    ''' Esta função gera um indivíduo para o problema das caixas não-binárias.
    
    Args:
        n: número de genes de cada indivíduo.
        x: valor máximo para cada gene.

    Return:
        Uma lista com n genes.
    '''
    indivíduo = []
    for _ in range(n):
        gene = gene_cnb(x)
        indivíduo.append(gene)

    return indivíduo


def indivíduo_senha(n, letras):
    ''' Esta função gera um indivíduo para o problema da senha.

    Args:
        n: número representando o tamanho total da senha.
        letras: letras possíveis de serem sorteadas.

    Return:
        Uma lista com  n letras.
    '''
    indivíduo = []
    for _ in range(n):
        gene = gene_letra(letras)
        indivíduo.append(gene)

    return indivíduo


def indivíduo_liga(elementos):
    ''' Esta função gera um indivíduo com três elementos aleatórios em três quantidades
    aleatórias para o problema da liga ternária mais cara.
    
    Args:
        elementos: uma lista de elementos possíveis de serem sorteados.
        
    Return:
        Um indivíduo com 3 elementos sorteados A, B e C e 3 quantidades x, y e z.
    '''
    elementos_temp = elementos.copy()
    indivíduo = []
    x = 0
    y = 0
    for _ in range(3):
        número = gene_ligaNúmero(x,y)
        
        if x==0:
            x = número
        elif y==0:
            y = número

        elemento = gene_ligaElemento(elementos_temp)
        elementos_temp.remove(elemento)

        indivíduo.append([número, elemento])

    return indivíduo


def indivíduo_cv(cidades):
    ''' Esta função sorteia um caminho possível no problema do caixeiro viajante.

    Args:
        cidades: dicionário onde as chaves são os nomes das cidades e os valores são as
    coordenadas das cidades.

    Return:
        Retorna uma lista de nomes de cidades formando um caminho onde visitamos cada
    cidade apenas uma vez.
    '''
    nomes = list(cidades.keys())
    random.shuffle(nomes)

    return nomes


# ------------------------------- POPULAÇÃO:

def população_cb(tamanho, n):
    ''' Esta função cria uma população no problema das caixas binárias.

    Args:
        tamanho: tamanho da população em indivíduos.
        n: número de genes de um indivíduo.

    Return:
        Uma lista onde cada item é um indivíduo.
    '''
    população = []
    for _ in range(tamanho):
        indivíduo = indivíduo_cb(n)
        população.append(indivíduo)

    return população


def população_cnb(tamanho, n, x):
    ''' Esta função cria uma população no problema das caixas não-binárias.

    Args:
        tamanho: tamanho da população em indivíduos.
        n: número de genes de um indivíduo.
        x: valor máximo para cada gene.

    Return:
        Uma lista onde cada item é um indivíduo.
    '''
    população = []
    for _ in range(tamanho):
        indivíduo = indivíduo_cnb(n,x)
        população.append(indivíduo)

    return população


def população_senha(tamanho, n, letras):
    ''' Esta função cria uma população no problema da senha.

    Args:
        tamanho: tamanho da população em indivíduos.
        n: número representando o tamanho total da senha.
        letras: letras possíveis de serem sorteadas.

    Returns:
        Uma lista onda cada item é um indivíduo no problema da senha.   
    '''
    população = []
    for _ in range(tamanho):
        indivíduo = indivíduo_senha(n, letras)
        população.append(indivíduo)
    
    return população


def população_liga(tamanho, elementos):
    ''' Esta função cria uma população de indivíduos no problema da liga ternária mais
    cara.

    Args:
        tamanho: tamanho da população em indivíduos.
        elementos: lista de elementos possíveis de serem sorteados.

    Returns:
        Uma lista onde cada item é um indivíduo no problema da liga mais cara.
    '''
    população = []
    for _ in range(tamanho):
        indivíduo = indivíduo_liga(elementos)
        população.append(indivíduo)

    return população


def população_cv(tamanho, cidades):
    ''' Esta função cria a população inicial no problema do caixeiro viajante.

    Args:
        tamanho: tamanho da população.
        cidades: dicionário onde as chaves são os nomes das cidades e os valores são as
    coordenadas das cidades.

    Returns:
        Lista com todos os indivíduos da população no problema do caixeiro viajante.
    '''
    população = []
    for _ in range(tamanho):
        população.append(indivíduo_cv(cidades))

    return população


# ------------------------------- FUNÇÃO OBJETIVO:

def funçãoObjetivo_cb(indivíduo):
    ''' Esta função computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os n genes.

    Return:
        A soma dos genes de um indivíduo.
    '''
    soma = sum(indivíduo) + 1
    
    return soma


def funçãoObjetivo_senha(indivíduo, senha_verdadeira):
    '''Esta função computa a função objetivo de um indivíduo no problema da senha.
    
    Args:
        indivíduo: lista contendo as letras da senha.
        senha_verdadeira: a senha que você está tentando descobrir no problema.

    Returns:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é medida
        letra por letra, e quanto mais distante uma letra for, maior o valor.
    '''
    diferença = 0

    for letra_candidato, letra_oficial in zip(indivíduo, senha_verdadeira):
        diferença = diferença + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferença


def funçãoObjetivo_ligaCara(indivíduo, preços_kg):
    '''Esta função computa a função objetivo de um indivíduo no problema da liga ternária
    mais cara.
    
    Args:
        indivíduo: lista contendo três números e três elementos intercalados.
        preços_kg: lista com todos os elementos possíveis e seus preços por kg.

    Returns:
        O preço total de um kilograma da liga escolhida.
    '''
    preço_total = 0
    números = []
    elementos = []

    for i in range(3):
        números.append(indivíduo[i][0])
        elementos.append(indivíduo[i][1])

    contador = 0

    for número, elemento in zip(números, elementos):
        preço_total += número * (preços_kg[elemento]/1000)
        contador += 2

    return preço_total


def funçãoObjetivo_cv(indivíduo, cidades):
    ''' Esta função computa a função objetivo de um indivíduo no problema do caixeiro
    viajante.

    Args:
        indivídiuo: lista contendo a ordem das cidades que serão visitadas
        cidades: dicionário onde as chaves são os nomes das cidades e os valores são as
    coordenadas das cidades.

    Returns:
        A distância percorrida pelo caixeiro seguindo o caminho contido no
    `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
    caixeiro retorna para a cidade original de onde começou sua viagem.
    '''
    distância = 0
    for posição in range(len(indivíduo)-1):
        partida = cidades[indivíduo[posição]]
        chegada = cidades[indivíduo[posição+1]]

        percurso = distânciaDoisPontos(partida, chegada)
        distância += percurso
    
    # caminho de volta pra cidade inicial!
    partida = cidades[indivíduo[-1]]
    chegada = cidades[indivíduo[0]]

    percurso = distânciaDoisPontos(partida, chegada)
    distância += percurso

    return distância

def funçãoObjetivo_mochila(indivíduo, objetos, limite, ordem_dos_nomes):
    ''' Esta função computa a função objetivo de um candidato no problema da mochila.
    
    Args:
        indivíduo: lista binária contendo a informação de quais objetos serão selecionados.
        objetos: dicionário onde as chaves são os nomes dos objetos e os valores são
    dicionários com a informação do peso e valor.
        limite: número indicando o limite de peso que a mochila aguenta.
        ordem_dos_nomes: lista contendo a ordem dos nomes dos objetos.

    Returns:
        Valor total dos itens inseridos na mochila considerando a penalidade paraquando o
    peso excede o limite.
    '''
    valor_mochila, peso_mochila = computaMochila(indivíduo, objetos, ordem_dos_nomes)
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila
    

# ------------------------------- FUNÇÃO OBJETIVO POPULAÇÃO:

def funçãoObjetivoPopulação_cb(população):
    ''' Esta função calcula a função objetivo para todos os membros de uma população.

    Args:
        população: lista com todos os indivíduos da população.

    Return:
        Lista de valores representando a fitness de cada um dos indivíduos da população.
    '''
    fitness = []

    for indivíduo in população:
        fobj = funçãoObjetivo_cb(indivíduo)
        fitness.append(fobj)

    return fitness


def funçãoObjetivoPopulação_senha(população, senha_verdadeira):
    ''' Esta função computa a função objetivo para todos os membros de uma população.

    Args:
        população: lista com todos os indivíduos da população.
        senha_verdadeira: a senha que você está tentando descobrir no problema.

    Returns:
        Uma lista contendo os valores da métrica de distância entre senhas.
    '''
    fitness = []

    for indivíduo in população:
        fobj = funçãoObjetivo_senha(indivíduo, senha_verdadeira)
        fitness.append(fobj)

    return fitness


def funçãoObjetivoPopulação_ligaCara(população, preços_kg):
    ''' Esta função computa a função objetivo para todos os membros de uma população.

    Args:
        população: lista com todos os indivíduos da população.
        preços_kg: lista com todos os elementos possíveis e seus preços por kg.

    Returns:
        Uma lista contendo os preços totais de cada indivíduo.
    '''
    fitness = []

    for indivíduo in população:
        fobj = funçãoObjetivo_ligaCara(indivíduo, preços_kg)
        fitness.append(fobj)

    return fitness


def funçãoObjetivoPopulação_cv(população, cidades):
    ''' Esta função computa a função objetivo de uma população no problema do caixeiro
    viajante.

    Args:
        população: lista com todos os inviduos da população
        cidades: dicionário onde as chaves são os nomes das cidades e os valores são as
    coordenadas das cidades.
    
    Returns:
        Lista contendo a distância percorrida pelo caixeiro para todos os indivíduos da
    população.
    '''
    resultado = []
    for indivíduo in população:
        resultado.append(funçãoObjetivo_cv(indivíduo, cidades))

    return resultado


def funçãoObjetivoPopulação_mochila(população, objetos, limite, ordem_dos_nomes):
    ''' Esta função computa a função objetivo de uma população no problema da mochila.

    Args:
        população: lista com todos os indivíduos da população
        objetos: dicionário onde as chaves são os nomes dos objetos e os valores são
    dicionários com a informação do peso e valor.
        limite: número indicando o limite de peso que a mochila aguenta.
        ordem_dos_nomes: lista contendo a ordem dos nomes dos objetos.
    
    Returns:
        Lista contendo a distância percorrida pelo caixeiro para todos os indivíduos da
    população.
    '''
    resultado = []
    for indivíduo in população:
        resultado.append(funçãoObjetivo_mochila(indivíduo, objetos, limite, ordem_dos_nomes))

    return resultado


# ------------------------------- SELEÇÃO:

def seleçãoRoletaMax(população, fitness):
    ''' Esta função seleciona indivíduos de uma população utilizando o método da roleta.

    Nota: implementadas apenas para problemas de maximização.

    Args:
        população: lista com todos os indivíduos da população.
        fitness: lista com o valor da função objetivo para cada indivíduo da população.

    Return:
        População dos indivíduos selecionados.
    '''
    população_selecionada = random.choices(população, weights = fitness, k = len(população))

    return população_selecionada


def seleçãoTorneioMin(população, fitness, tamanho_torneio = 3):
    '''Esta função seleciona indivíduos de uma população por meio de torneio.
    
    Nota: implementada apenas para problemas de minimização.

    Args:
        população: lista com todos os indivíduos da população.
        fitness: lista com o valor da função objetivo para cada indivíduo.
        tamanho_torneio: quantidade de indivíduos que batalham entre si.

    Return:
        População de indivíduos selecionados; do mesmo tamanho do argumento 'população'.
    '''
    selecionados = []

    # associando cada indivíduo com seu valor de fitness:
    par_população_fitness = list(zip(população, fitness))

    # fazendo os torneios:
    for _ in range(len(população)):
        combatentes = random.sample(par_população_fitness, tamanho_torneio)
        mínimo_fitness = float("inf")

        for par_indivíduo_fitness in combatentes:
            indivíduo = par_indivíduo_fitness[0]
            fit = par_indivíduo_fitness[1]
            if fit < mínimo_fitness:
                selecionado = indivíduo
                mínimo_fitness = fit
        selecionados.append(selecionado)

    return selecionados


# ------------------------------- CRUZAMENTO:

def cruzamentoPontoSimples(pai, mãe):
    ''' Esta função representa o operador de cruzamento/crossover de ponto simples.

    Args:
        pai: um indivíduo qualquer selecionado como progenitor.
        mãe: outro indivíduo qualquer selecionado como progenitor.

    Returns:
        Duas listas, cada uma correspondendo a um filho de cada pai usado como argumento.
    '''
    ponto_de_corte = random.randint(1, len(mãe)-1)
    filho1 = pai[:ponto_de_corte] + mãe[ponto_de_corte:]
    filho2 = mãe[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2


def cruzamentoOrdenado(pai, mãe):
    ''' Esta função representa o operador de cruzamento ordenado.

    Args:
        pai: um indivíduo qualquer selecionado como progenitor.
        mãe: outro indivíduo qualquer selecionado como progenitor.

    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os
    argumentos. Estas listas mantém os genes originais dos pais, porém altera a ordem
    deles.
    '''
    corte1 = random.randint(0, len(mãe) - 2)
    corte2 = random.randint(corte1 + 1, len(mãe)-1)

    filho1 = pai[corte1:corte2]
    for gene in mãe:
        if gene not in filho1:
            filho1.append(gene)

    filho2 = mãe[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)

    return filho1, filho2


# ------------------------------- MUTAÇÃO:

def mutação_cb(indivíduo):
    ''' Esta função realiza uma mutação de um gene no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias.
    Return:
        Um indivíduo com o gene mutado.
    '''
    gene_mutado = random.randint(0, len(indivíduo)-1)
    indivíduo[gene_mutado] = gene_cb()

    return indivíduo


def mutação_cnb(indivíduo, x):
    ''' Esta função realiza uma mutação de um gene no problema das caixas não-binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas não-binárias.
        x: valor máximo para cada gene.
    Return:
        Um indivíduo com o gene mutado.
    '''
    gene_mutado = random.randint(0, len(indivíduo)-1)
    indivíduo[gene_mutado] = gene_cnb(x)

    return indivíduo

def mutação_senha(indivíduo, letras):
    ''' Esta função realiza a mutação de um gene no problema da senha.

    Args:
        indivíduo: uma lista representando um indivíduo no problema da senha.
        letras: letras possíveis de serem sorteadas.

    Return:
        Um indivíduo (senha) com um gene mutado.
    '''
    gene_mutado = random.randint(0, len(indivíduo)-1)
    indivíduo[gene_mutado] = gene_letra(letras)

    return indivíduo


def mutação_liga(indivíduo, elementos):
    ''' Esta função realiza a mutação de um dos elementos do gene no problema da liga
    mais cara.

    Args:
        indivíduo: uma lista representando um indivíduo no problema da liga mais cara.
        elementos: uma lista com todos os elementos possíveis.

    Return:
        Um indivíduo com apenas o elemento de um gene ([número, elemento]) mutado.
    '''
    elementos_temp = elementos.copy()

    for elemento in indivíduo:
        if elemento in elementos_temp:
            elementos_temp.remove(elemento)
            
    gene_mutado = random.randint(0, len(indivíduo)-1)
    número = indivíduo[gene_mutado][0]
    indivíduo[gene_mutado] = [número,gene_ligaElemento(elementos_temp)]

    return indivíduo


def mutaçãoDeTroca(indivíduo):
    ''' Esta função realiza a mutação de troca, trocando o valor de dois genes.

    Args:
        indivíduo: uma lista representado um indivíduo.

    Return:
        O indivíduo recebido como argumento, porém com dois dos seus genes
    trocados de posição.
    '''
    índices = list(range(len(indivíduo)))
    índice1, índice2 = random.sample(índices, k=2)
    indivíduo[índice1], indivíduo[índice2] = indivíduo[índice2], indivíduo[índice1]

    return indivíduo