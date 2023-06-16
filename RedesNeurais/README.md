# Experimentos de redes neurais artificiais

Nesta pasta constam experimentos didáticos no formato de notebooks Jupyter. Os experimentos adicionados até o momento e uma breve descrição dos conceitos e funções introduzidos em cada um se encontra abaixo. Para mais informações sobre cada experimento, confira os arquivos em questão.

<hr>

## Experimentos coletivos realizados em sala:

<br>

* __Experimento R.01__ - _Derivadas_:
  * Relembrando o conceito de derivadas.


<br>

* __Experimento R.02__ - _Classes_:
  * Introdução ao conceito e uso de classes no Python;
  * Apresentação de métodos *dunder*.
  * Métodos do Python introduzidos:
```
class
__init__
__repr__
```

<br>

* __Experimento R.03__ - _Construindo um grafo automaticamente_:
  * Plotagem de um grafo representativo do conceito de *back propagation*.
  * Métodos do Python introduzidos:
```
__add__
__mul__
```
 * Funções introduzidas em [funcoes.py](funcoes.py):
```
plota_grafo()
```

<br>

* __Experimento R.04__ - _Computando os gradientes locais automaticamente_:
  * Complementação da classe `Valor` com a implementação de uma função que calcula e propaga os gradientes locais automaticamente.


<br>


* __Experimento R.05__ - _Finalizando a classe Valor_:
  * Adição de vários métodos à classe `Valor`;
  * Finalização da classe `Valor`;
  * Métodos do Python introduzidos:
```
__radd__
__rmul__
__truediv__
__pow__
__neg__
__sub__
__rsub__
```

<br>

* __Experimento R.06__ - _Redes neurais artificiais_:
  * Construção da nossa primeira rede MPL (Multilayer Perceptron);
  * Plotagem do grafo da RNA.


 <br>


* __Experimento R.07__ - _Treinando uma rede neural_:
  * Introdução à função de perda (_loss function_);
  * Treinamento da rede pela atualização dos parâmetros;
  * Implementação da descida do gradiente em um loop de épocas.


<br>

* __Experimento R.08__ - _Treinando uma rede neural usando pytorch_:
  * Apresentação ao método prático de construir RNAs a partir do módulo *PyTorch*.
  * Métodos, classes e módulos do PyTorch introduzidos:
```
tensor
nn.Module
nn.Sequential
forward
nn.Sequential
nn.Linear
nn.ReLU
nn.MSELoss
optim.Adam
inverse_transform
train
eval
no_grad
```