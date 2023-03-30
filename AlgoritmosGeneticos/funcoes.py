# Imports:

import random

# Funções:

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
    candidato = []
    for _ in range(n):
        candidato.append(gene_letra(letras))

    return candidato


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
        tamanho: tamanho da população.
        n: número representando o tamanho total da senha.
        letras: letras possíveis de serem sorteadas.

    Returns:
        Uma lista onda cada item é um indivíduo no problema da senha.   
    '''
    população = []
    for _ in range(tamanho):
        população.append(indivíduo_senha(n, letras))
    
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
        insivíduo: lista contendo as letras da senha.
        senha_verdadeira: a senha que você está tentando descobrir no problema.

    Returns:
        A "distância" entre a senha proposta e a senha verdadeira. Essa distância é
        medida letra por letra, e quanto mais distante uma letra for, maior o valor.
    '''
    diferença = 0

    for letra_candidato, letra_oficial in zip(indivíduo, senha_verdadeira):
        diferença = diferença + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferença


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