# Experimentos de otimização e algoritmos genéticos

Nesta pasta constam experimentos didáticos no formato de notebooks Jupyter. Os experimentos adicionados até o momento e uma breve descrição dos conceitos e funções introduzidos em cada um se encontra abaixo. Para mais informações sobre cada experimento, confira os arquivos em questão.

<hr>

## Experimentos coletivos realizados em sala:

<br>

* __Experimento A.01__ - _Busca aleatória_:
  * Introdução ao problema das caixas binárias;
  * Introdução a algoritmos de busca;
  * Resolução com o algoritmo de busca aleatória.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
gene_cb();
indivíduo_cb();
funçãoObjetivo_cb()
```
  
<br>

* __Experimento A.02__ - _Busca em grade_:
  * Resolução com o algorimto de busca em grade.
  
<br>

* __Experimento A.03__ - _Algoritmo genético_:
  * Introdução a algoritmos genéticos;
  * Resolução com um algoritmo genético.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
população_cb();
seleçãoRoletaMax();
funçãoObjetivoPopulação_cb();
cruzamentoPontoSimples();
mutação_cb()
```
  
<br>

* __Experimento A.04__ - _Caixas não-binárias_:
  * Introdução ao problema das caixas não-binárias;
  * Resolução com um algoritmo genético.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
gene_cnb();
indivíduo_cnb();
população_cnb();
mutação_cnb()
```
  
<br>

* __Experimento A.05__ - _Descobrindo a senha_:
  * Introdução ao problema de descoberta de uma senha;
  * Resolução com um algoritmo genético.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
indivíduo_senha();
população_senha();
seleçãoTorneioMin();
funçãoObjetivo_senha();
funçãoObjetivoPopulação_senha();
mutação_senha()
```

<br>

* __Experimento A.06__ - _O caixeiro viajante_:
  * Introdução ao problema do caixeiro viajante;
  * Resolução com um algoritmo genético.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
distânciaDoisPontos();
criaCidades();
indivíduo_cv();
população_cv();
funçãoObjetivo_cv();
funçãoObjetivoPopulação_cv();
cruzamentoOrdenado();
mutaçãoDeTroca()
```

<br>

* __Experimento A.07__ - _Aplicando restrições na busca_:
  * Introdução a problemas com restrições por meio do problema da mochila;
  * Resolução com um algoritmo genético.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
computaMochila();
funçãoObjetivo_mochila();
funçãoObjetivoPopulação_mochila()
```

<br>

* __Experimento A.08__ - _Usando o módulo DEAP_:
  * Introdução ao módulo DEAP;
  * Resolução do problema das caixas binárias com o DEAP.

<hr>

## Experimentos individuais realizados fora de sala:

<br>

* __Experimento GA.09__ - _A liga ternária mais cara_:
  * Introdução ao problema da liga ternária mais cara do mundo;
  * Resolução com um algoritmo genético.
  * Funções introduzidas em [funcoes.py](funcoes.py):
```
computaLiga();
gene_liga();
indivíduo_liga();
população_liga();
funçãoObjetivo_ligaCara();
funçãoObjetivoPopulação_ligaCara();
qualÉALiga()
```
