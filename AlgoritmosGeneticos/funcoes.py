# Imports:

import random

# Funções:

def gene_cb():
    ''' Esta função gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor 0 ou 1.
    '''
    valoresPossíveis = [0, 1]
    gene = random.choice(valoresPossíveis)

    return gene

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

def funçãoObjetivo_cb(indivíduo):
    ''' Esta função computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os n genes.

    Return:
        A soma dos genes de um indivíduo.
    '''
    soma = sum(indivíduo) + 1
    
    return soma

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

def seleçãoRoletaMax(população, fitness):
    ''' Esta função seleciona indivíduos de uma população utilizando o método da roleta.

    Nota: apenas para problemas de maximização.

    Args:
        população: lista com todos os indivíduos da população.
        fitness: lista com o valor da função objetivo para cada indivíduo da população.

    Return:
        População dos indivíduos selecionados.
    '''
    população_selecionada = random.choices(população, weights = fitness, k = len(população))

    return população_selecionada

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