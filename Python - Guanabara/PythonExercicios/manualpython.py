''' o input serve para fazer uma interação com o usuário,
sendo o que você escrever, aparecerá para o usuário
'''

'''o print serve para você exibir na tela uma mensagem, entre aspas'''

'''o sinal de igual (=) significa "recebe", pro python.
ou seja, atribuir um valor a uma variável'''

'''o sinal de mais (+) serve para juntar (literalmente)
termos. E às vezes para somar'''


''' 
                tipos primitivos básicos  ---> Muito importantes!!!
'''

'''
int - (a função int) é, basicamente, números inteiros. Serve para dizer que
o número digitado será inteiro para o python.
Usado para somar corretemente os números. 
e usado logo antes do input:  int(input(.......))

ex: 7, -4, 0, 9875. Então os números positivos, negativos ou nulo,
são valores inteiros para o python.


float - são números reais, ou de ponto flutuantes (basicamente são
números decimais, mas como o python entende a vírgula (,) como 
um ponto (.), se chama ponto flutuante). Ou seja, o ponto é igual
a vírgula.

ex: 4.5, 0.076, -15.223, pi (3,14), 7.0 > Esse "sete" e o de cima
                   ^                      tem o mesmo valor. Apenas esse tem
                   ^                      a parte flutuante (número real)
                   ^                      e o outro, é inteiro.
                   ^
obs: Aquele número ^, não é 15.223 (quinze mil, duzentos e 
vinte três), é 15,223. lembra que a gente usa a vírgula para 
separar números reais, mas o python e o padrão internacional
utilizam o ponto (.) no lugar dela. Então esse é um número
real e negativo ou flutuante e negativo.

obs2: quinze mil no python seria assim: 15000 --> sem ponto.


bool - valores lógicos ou booleanos. Aceitam apenas dois valores:
verdadeiro (True) e falso (False). Obs: sempre que for utilizar 
a palavra "True" ou "False", como valor booleano, um valor lógico,
coloca o "T" maiúsculo. Eo "F" do "False" também.

Então você vai botar True e/ou False como capitalizado, isto é,
como a primeira letra capitalized, ou seja, de forma maiúscula.

obs: As outras letras tem sempre que ser minúsculas também.


str - valores caracteres ou strings. 

ex: 'Olá', '7.5', ''      obs: Lembrando que todas as palavras tem que
             ^    ^          estar entre aspas (duplas ou simples)
             ^    ^                             
             ^    ^
             ^----^---------> Esse "sete e meio" não é flutuante. Ele é
                  ^            uma string porque está entre aspas!
                  ^
                  ^
É possível ter também uma string vazia,
que é representada pelas aspas sem nenhum
conteúdo dentro. Isso significa que 
é uma string vazia.
        
'''

# obs: todos esses tipo primitivos são udados
# logo antes do input !!!!!!

'''
ex:

str(input(......))
bool(input(......))
float(input(.....))
etc


Obs: Também é possível usar mais de um tipo primitivo básico
na mesma linha 

ex: 

str(float(input('Digite um número'))) 
........
'''

'''
as máscaras ({} = chaves) são usadas para facilitar o código e 
deixá-lo mais curto. Para elas funcionarem, é preciso usar
o .format(). E é nesse parênteses que a variável ficará
para ser formatada. 

ex1:
n1 = 'um número'
n2 = 'outro número'
r = n1 + n2 
print('o resultado de n1 com n2 é {}').format(r)

prefiro este.
'''

'''
Também pode-se utilizar o .format() para formatar variáveis 
em situações específicas: 

ex2: 

n1 = 'um número'
n2 = 'outro número'
print('O resultado é {}'.format(n1 + n2)

Usa-se isso no lugar de criar uma variável pré-pronta e apenas formatá-la, 
que nem no exemplo acima deste, no caso o "r".

Mas quando que eu uso com variável (ex1) e sem variável 
(ex2)?

Se você usar com variável,é porque, provavelmente, vai precisar
desse resultado DEPOIS.

Como nesse caso (ex2) eu quero pegar os números, somar
e a soma não serve para mais nada, a não ser mostrar na tela,
pode colocar desta maneira.
'''

'''
E para formatar mais de uma variável no .format(), usa-se a vírgula (,).
O número de máscaras é o mesmo número de variáveis, se fizer como o ex1,
que está lá em cima.

ex:  

n1 = 'um número'
n2 = 'outro número'
n3 = n1 + n2 
n4 = n1 * n2
print('A soma dos números é igual a {} e o produto {}'.format(n3, n4))
'''

'''                       Ordem de Precedência

1º()   - resolve os parênteses primeiro
2º**   - depois todas as potências
3º* / // %  - depois o que apareceu primeiro (a multiplicação, 
4º + -                            a divisão, a divisão inteira 
     ^                                    ou o resto da divisão)
     ^   
     ^---> e por fim, a soma ou a subtração
'''

'''
Explicando a divisão, divisão inteira e o resto da divisão:

Divisão: 

ex: 5 / 2 (5 dividido p/ 2). Se eu pego 5 e divido por 2, não
vai me dar um número inteiro, mas sim, flutuante (decimal). Que no
caso é 2.5. A / (barra) = divisão exata, ou não inteira.

Divisão inteira: divisão sem a vírgula (ponto no python).

Ex: Se eu faço 5 // 2, vai dar 2. Porque 3 x 2 passa de 5.
2 x 2 = 4, para 5, resta 1. E para por aí, porque se dividir 
o 1, vai ser decimal (com vírgula).  

Resto da divisão: o que sobra em uma divisão inteira. 

Ex: 5 // 2. Lembra que a gente viu ali em cima que sobra 1. Então.
Esse é o resto da divisão. É literalmente o que sobra de uma divisão
inteira.


Eu posso também, em vez de usar os asteriscos (** = potência),
usar a função power: pow(4,3) = 64 . A mesma coisa: 4**3 = 64
'''

'''
E uma dica para raíz quadrada: como a raíz quadrada de 81 é 9 (um exemplo),
podemos fazer assim: 81**(1/2) = 9. Ou seja, 81 elevado a meio.
 
Então eu estou forçando o python a calcular 1 dividido por 2,
que = 0,5 (meio) e potenciando o 81 por meio.

Ou seja, calcular a raíz quadrada de um número é a mesma coisa
que potenciá-lo por meio (0,5). outro ex: 25**(1/2) = 5.
'''

'''
sabemos que, se fizermos 'Oi' + 'Olá', vai dar 'OIOlá'. isso é, vai juntar
as mensagens. concatená-las. Mas se eu fizer 'Oi'*5? ou seja, multiplicar
a mensagem 'Oi' cinco vezes: isso é igual a 'OiOiOiOiOi'.

Ou '='*20. Ou seja, o sinal de igual vezes vinte: = '===================='.

Então eu consigo dar um print nisso: print('='*20) = ====================. 
Sem as aspas. Então eu consigo printar o igual 20 vezes, por exemplo.
'''

'''
OBS: Ao executar um programa e funcionar, não significa
que ela está totalmente certo. Você pode estar obtendo
um resultado errado. Isso se dá devido a ORDEM de PRECEDÊNCIA
'''

'''
Quando eu quero testar se uma coisa é igual a outra, no python, 
utilizaremos dois símbolos de igual =
                                    =. até porque
um só símbolo de igual é o sinal de atruibuição (lemos como "recebe")
'''

'''
Dica: não copiar ou colar nada: sempre escrever todo o código 
para aprender a estrutura e conhecer mais o código. 
esrevendo você aprende muito.
'''

'''
Dica: É possível também utilizar, nas chaves do .format, uma 
"abreviação" de casas decimais: 

ex: 

n1 = 'um número'
n2 = 'outro número'
d = n1 / n2
print('O resultado da divisão é {:.3f}'.format(d)) 
                              >----^
                              ^    
Aqueles "dois pontos, ponto, 3f", diz pro python que
deve exibir apenas 3 casas flutuantes (decimais = depois da vírgula)

Então se eu fizesse: 4 / 3 (4 dividido por 3), daria: 1.3333333333333333....
Mas com o {:.3f}, apareceria: 1.333. 
Bem mais organizado!

obs: Para arrendondar um valor de núemero flutuante, ou seja,
os números depois da vírgula (ponto), essa função também serve!
Funciona tbm com 2 e 1 casa flutuante. E para esconder a casa
flutuante, usa-se o 0 nas chaves: {:.0f}
'''

'''
Dica: para não quebrar a linha do código, por exemplo, pelo uso
de dois prits, botamos end=' ' (no caso o end, igual a um espaço) 
no final do código. Mas tem que estar dentro do parêntes do print.

ex:

n1 = 'um número'
n2 = 'outro número'
print('O resultado da soma desses números é {}'.format(n1 + n2) end=' ')
print(' E o resultado da multiplicação é {}'.format(n1 *  n2))

Fazendo isso, os dois prints aparecerão na mesma linha.
'''

'''
Eu também posso quebrar a linha no meio do print, em vez
de criar vários prints, eu uso o \n

ex:

print('O resultado da divisão é {} \n e da adição é {}'.format())

Aí será exibido a mensagem toda, antes do \n, normalmente,
e a mensagem depois, embaixo da mesma. tipo:

O resultado da divisão é (o resultado)
e da adição é (o outro resultado)

Assim.
'''

# resumindo: para quebrar a linha \n
# para continuar end=''

'''
                módulos

Há duas maneiras de importar módulos:


import - que importa todas as funcionalidades de um módulo. Que 
é mais generalista.


from import - importa apenas as funcionalidades escolhidas 
por mim. Um pouco mais específico.


ex: a biblioteca math; tem nela, algumas funcionalidades como:


ceil - que faz um arredondamento para cima, de um número.


floor - que, de maneira similar, faz o arredondamento
para baixo.


trunc - a função truncate, que trunca o número, isto é,
elimina os números da vírgula para frente, sem arredondar.


pow - = power = potência, que funciona parecido com os 
dois asteriscos (** = potência também)


sqrt - a square root, que calcula a raiz quadrada.


factorial - calcula o fatorial de um número.


Aí, supondo que você queira importar a biblioteca math:

Se você der: import math, todas as funcionalidades
serão importadas.


Mas supondo também, que você queira usar uma função 
específica desta biblioteca: from math import       <--- (e a função que
                                                         você quer usar da
                                                        biblioteca math)


Mas se eu precisar importar mais de uma função específica?

Você fará a mesma coisa, apenas adicione a vírgula depois
da função desejada e a outra função desejada.

ex: from math import ceil, sqrt
'''

'''
obs: se você importar uma biblioteca, você terá que 
atribuir ela a uma variável e fazer referência a ela,
juntamente com a função que você quer utilizar dela,
depois de um ponto:

ex: 

import math
co = int(input('Valor do cateto oposto: '))
ca = int(input('Valor do cateto adjacente'))
h = math.hypot(co, ca) ---------------------> aqui ó: falo referência a
print('A hipotenusa vale {}'.format(h))       biblioteca, boto um ponto
                                              e escolho a função que eu
                                                       quero.

agora: (mesmo exemplo)

from math import hypot  ---> como eu uso o "from import", escolho uma 
co = int(input('Valor do cateto oposto: ))          função específica
ca = int(input('Valor do cateto adjacente: ))      da bilioteca...
h = hypot(co, ca) -------------------------
print('A hipotenusa vale {}'.format(h))   |---> ... por isso não
                                             preciso fazer referência
                                                     à biblioteca.

Parece algo bobo, mas quando tem que fazer várias vezes,
faz diferença
'''

'''
Para o python, uma lista de alguma coisa, fica entre colchetes [].
Então você coloca os colchetes e coloca os elementos que 
tem dentro da lista, dentro dos colchetes.

ex: lista de compras:

compras = ['pão', 'leite', 'arroz']

Tendeu?


Eu também posso botar a lista, dentro do parêntes do random,
por exemplo, para escolher aleatoriamente o elemento:

ex: 

from random import choice  --> usei o "from" porque queria usar
n1 = 'batata'                          apenas a função "choice"
n2 = 'cenoura'                         da biblioteca random.
n3 = 'beterraba' 
c = choice([n1, n2, n3])
print('Eu vou comprar então a {}'.format(c))
'''

'''
Para embaralhar uma sequência de alguma coisa, use-se
o "shuffle", da biblioteca random

ex: 

from random import shuffle
n1 = 'anel'
n2 = 'chaveiro'
n3 = colher
l = [n1, n2, n3]
shuffle(l)  ---> Isto é, vai embaralhar os objetos (no caso, a lista)
print(l) ----> e vai mostar na tela a lista já embaralhada.


Obs: não precisa atribuir o shuffle a alguma variável. Pode
usá-lo direto, sem .format e os caramba.
'''


'''
Para randomizar, ou seja, gerar algo aleatoriamente, pode-se usar a 
biblioteca random. 
E para gerar números inteiros aleatórios, usa-se a função randint
da biblioteca random.
E você também pode fazer assim: randint(0, 5) = vai gerar um 
número inteiro aleatório entre 0 e 5.
'''


'''
A biblioteca pygame serve para criar jogos, jogos tem músicas,
então pode ser usado também para reproduzir música. Ele também
carrega imagens, sons, vídeos etc.

Como a gente quer tocar um mp3, vamos até a internet e pesquisemos
o vídeo que queremos baixar no site de conversor de vídeo
para mp3. Depois de baixado, no explorador de arquivo, o copiamos
e no pycharm, clicamos com o botão direito no projeto e clicamos em
"paste". 

Obs: Dê um nome curto para o arquivo mp3. 


Agora, voltando para o pygame:

Para baixá-lo, bota: import pygame -  na linha onde digita o 
código, e, no pycharm, clica na lâmpada vermelha e clica em
"install package pygame".

A primeira coisa a fazer é iniciar o pygame. Então tu bota:
pygame.init(). Aí você inica o uso da biblioteca pygame.

A gente vai agora ver o mixer do pygame.

Então a linha já está assim até agora:

import pygame
pygame.init()

Agora vamos adicionar o mixer:  pygame.mixer.music.load()  ---> e aqui
você põe o nome do arquivo que você salvou entre aspas.
vai ficar assim:

import pygame
pygame.init()
pygame.mixer.music.load() --> o nome do arquivo mp3

Depois, adiciona: pygame.mixer.music.play()  --> deixa o parêntes 
vazio mesmo. E um: input(), na linha debaixo

Assim ó:

import pygame
pygame.init()
pygame.mixer.music.load()
pygame.mixer.music.play()
input()


E por fim, para ele (o python) esperar o evento terminar (a música),
para encerrar o programa, adicionamos: pygame.event.wait 

O código todo fica assim:

import pygame  --> para importar a biblioteca
pygame.init()  --> para iniciar a biblioteca (ou seu uso) 
pygame.mixer.music.load()  --> para carregar o arquivo (a música)
pygame.mixer.music.play()  --> para tocar a música (ou rodar
input()  --> não sei pra que serve                   o programa)
pygame.event.wait()  --> para esperar o programa acabar para 
                                    encerraro programa.
                                    
Pronto.
'''

'''
Pode-se importar uma funcionalidade da biblioteca time, que é o 
sleep. Que faz o computador meio que "dormir" por alguns segundos.
Você usa assim: escreve o que quer que aparece e coloca 
sleep() ---> Dentro do parênteses você coloca quanto tempo você 
quer que o computador "durma". 
Ex: Eu quero que o cumputador durma por 5 segundos. Aí eu ponho:
sleep(5)
'''

'''
                 Operações com string
                 

Vamos começar: eu vou pegar uma frase com exemplo e jogar
dentro de uma variável do tipo string. Assim:

frase = 'Curso em Vídeo Python'  --> Essa forma, de como 
está escrita, é a de forma de atribuiçãode de uma string,
dentro de uma variável.

Explicação: Quando eu faço esse tipo de atribuição, o python 
coloca esses dados (essa frase) na memória do computador.
Só que ela não vai inteira; o python vai criar mini espaços,
dentro da memória do computador, e dentro de cada mini espaço
desse, ele vai colocar cada uma das letras.

Tipo assim: Curso em VídeoPython
            -------------------- 

frase = 'Curso em Vídeo Python'  --> imagina que cada letra
está dentro de^ um mini quadradinho, começando do c e terminando
no n.         ^
Perceba que entre "Curso" e "em", tem um espaço: esses espaços
também ocupam um mini espaço.
                        |       Curso em Vídeo Python
ex:                     |       ---------------------
                        '>>          ^  ^     ^

E cada um desses mini espaços vão receber um ínidce, que é
um número sequencial começando do 0, até o nº de letras
necessários para caber todas as letras/caracteres dentro
da memória.

Assim: 

| C u r s o   e m   V í d e o   P y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | --> esses números aqui
|                     0 1 2 3 4 5 6 7 8 9 0 |  -> são os índices!!!

numeração de 1 a 20 = 21 caracteres
Deu 21 caracteres porque começa a contagem da primeira letra, do
0 e os espaços também contam.
'''

'''
         Operações com cadeia de caracteres
         
         
Fatiamento - fatiar uma string é conseguir pegar pedaços dela.
ex: Seu mandar escrever, por exemplo, frase[9] ("frase", que é
o nome da minha variável e 9 entre colchetes) 

Obs: O símbolo de colchete, é o identificador de uma estrutura 
de dados no python, chamada lista.

Voltando...

Então se eu mandar escrever, por exemplo, print(frase), só 
print(frase), ele vai escrever: Curso em Vídeo Python, que
é o texto atruibuído à variável "frase": frase = 'Curso em Vídeo
Python'.

Agora, se eu mandar escrever frase[9], ele vai conseguir 
identificar, dentro da cadeia de caracteres, somente o caracter
9, que, no caso é o 10º caracter, ou o "V" (maíusculo).    
Isso porque começa a contar do 0.       |    Curso em Vídeo Python  
                                        '> -----------^

Obs: o python diferencia maíusculas de minúsculas: V maíusculo
não é a mesma coisa que v minúsculo.          
         
Então a forma mais simples de fatiamento é conseguir pegar uma letra.
para eu pegar uma letra, eu tenho que dizer o nome da variável, 
no caso o "frase" e entre colchetes eu coloco um número, que 
é o número do índice dentro daquela string.


Outro ex de fatiamento:

frase[9:13]

É o seguinte: 9 é o V (maiúsculo), e 13 é o "o" (letra o):

                        _         _
   | C u r s o   e m   |V| í d e |o|   P y t h o n |
   | 0 1 2 3 4 5 6 7 8 |9| 1 1 1 |1| 1 1 1 1 1 1 2 | 
   |                   |_| 0 1 2 |3| 4 5 6 7 8 9 0 |  
                                 |_|

Enfim. Fazendo isso, ele vai começar no 9(V) e vai até o 13(o).
Só que o 13 será excluído. Ou seja ele vai pegar somente "Víde".
O o não vai entrar na lista. Assim:

                     _______
| C u r s o   e m   |V í d e| o   P y t h o n |
| 0 1 2 3 4 5 6 7 8 |9 1 1 1| 1 1 1 1 1 1 1 2 | 
|                   |  0 1 2| 3 4 5 6 7 8 9 0 |    
                    |_______|
         
Então se eu der frase[9:13], nesse exemplo, vou ter Víde
como resultado.

Mas se eu quisesse pegar o o também???

Aí você teria que dar frase[9:14], porque ele vai pegar
até o 13. É sempre 1 a menos no final (por causa do 0).     
         
         
Então lembra: Quando eu tô trabalhando com range (nesse caso
fatiamento de string), o último valor não entra na contagem.

Então [9:13] significa: vai do 9 até o 13, incluindo o 9, e 
removendo o 13. Ou seja, [9:13] = vai do 9 até o 12 (um a menos!)   


Mais um exemplo de fatiamento:

frase[9:21] 

Aí tu pode falar que vai dar erro, porque o 9 eu tenho, mas 
21 não. Aí tu se lembra: o último valor não é contabilizado.
Então no caso, [9:21], elevai começar no 9 e para no 20.

Logo, vai ficar assim:

                     ________________________
| C u r s o   e m   |V í d e o   P y t h o n |
| 0 1 2 3 4 5 6 7 8 |9 1 1 1 1 1 1 1 1 1 1 2 | 
|                   |  0 1 2 3 4 5 6 7 8 9 0 |
                    |________________________|
                                        ^
Então ele vai fatiar somente essa parte ^  

É possível colocar apenas uma unidade a cima da máxima, como 
nesse caso.

Mas essa não é a melhor forma de fatiar, pondo um valor que 
não existe.


Outro exemplo: 

frase[9:21:2]

Eu também posso fazer desse jeito aí: [9:21:2]
                                            ^
Mas o que é isso?                           ^--<^    
                                                |
Eu vou começar no 9, vou parar no 2, e, aquele 2 ali é
pulando de 2 em 2. Ou seja, ele vai me mostrar o V,
pular 2 e me mostrar o "d", pular 2 e me mostrar o "o",
pular 2 e me mostrar o "p", fazer de novo e me mostrar
o "t", de novo, me mostrando o "o" e pluar o "n" (não 
vai contabilizar o n). 

Assim:
                        ^-----^-----^-----^-----^-----^----> O restante 
| C u r s o   e m   |V| í |d| e |o|   |P| y |t| h |o| n |  será ignorado.
| 0 1 2 3 4 5 6 7 8 |9| 1 |1| 1 |1| 1 |1| 1 |1| 1 |1| 2 | 
|                   | | 0 |1| 2 |3| 4 |5| 6 |7| 8 |9| 0 |

Então ele vai de 9 até 21, pulando de 2 em 2.

Então se eu desse print nisso:  print(frase[9:21:2]), apareceria
V d o  P t o, de Curso em Vídeo Python.
  
  
Outro exemplo: 
  
frase[:5]

Um parênteses: antes dos dois pontos (:), é onde ele começa
a fatiar, então depois dos : é onde ele vai terminar, excetuando
esse valor. 

Quando eu não coloco onde ele vai começar, ou seja, quando
eu omito o início, ele começa do caracter 0.

Então quando eu dou [:5], ele começa do 0 e vai até o 5,
sem contabilizá-lo, contando o 4. Então ele vai fazer do 0
até o 4, ficando assim: 

 __________
| C u r s o|   e m   V í d e o   P y t h o n |
| 0 1 2 3 4| 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|          |           0 1 2 3 4 5 6 7 8 9 0 |
|----------|  
  
Vai fatiar somente a palavra "Curso".
  
  
Outro exemplo:

frase[15:]
  
É o mesmo raciocínio: [15], sozinho, seria o P maiúsculo da 
frase, mas eu botei 15: (15, dois pontos). OU seja, eu indiquei
o início, mas eu não sei o final.

Fazendo isso, não sabendo o final, você diz pro python que 
quer do 15 até o final:

                                 ____________
| C u r s o   e m   V í d e o   |P y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 |1 1 1 1 1 2 | 
|                     0 1 2 3 4 |5 6 7 8 9 0 |
                                |------------|              
  
Então fatiará a palavra "Python", para mim inteira.

É igual o recurso utilizado no exemplo [:21] (algum valor, dois 
pontos, 21), nesse caso, porque não existe o 21, ele para no 20.   
  
Dica: Se você não sabe qual é o último caracter, pode-se
colocar nada (nenhum valor)no final dos : (dois pontos), 
se você quiser fatiar até o final da string.   
  
  
Mais exemplos:

frase[9::3]
  
Se liga, começa no 9 (V), e falta um número um : e outro,
o segundo número depois do primeiro :, é o final.
Como eu não estou colocando, omitindo, ele vai até o final,
ou até a última letra. 
Então vai começar no V e terminar no n e, como aida tem o 3,
significa que vai pular de 3 em 3:    
  
                        ^_^_____^_^_____^_^_____^_^_____> todos
| C u r s o   e m   |V| í d |e| o   |P| y t |h| o n |  esses serão
| 0 1 2 3 4 5 6 7 8 |9| 1 1 |1| 1 1 |1| 1 1 |1| 1 2 |  ignorados!!
|                   | | 0 1 |2| 3 4 |5| 6 7 |8| 9 0 | 
  
Então nsse caso, frase[9::3], me mostraria: V  e  P  h. 
 
 
Mais operações com cadeias de string 
 
Análise - é, possivelmente, a operação a ser mais utilizada.
Analisar uma string é saber algumas infomações sobre ela, tipo
seu tamanho, qual a letra inicial, qual a final, qual a primeira
palavra inteira, etc. Ou seja, analisar essa string.
  
  
exemplos:

len(frase) - "len" vem de lenf = comprimento. 
Então se eu mandar mostrar o len de frase, eu estou pedindo
pro python mostrar o comprimento da frase.  
  
Já sabemos que "Curso em Vídeo Ptyhon" tem 21 caracteres, ou seja,
21 espaços, 21 microespaços na memória. Tendo esses 21 microespaços,
ele tem 21 caracteres, logo, len(frase) (o "len" de "frase") tem
21 caracteres.
  
Guardar ela com apreço, porque será muito utilizada mais pra 
frente.  
  
  
Mais formas de análise:
             ^> Obs: Isso é um o (letra o) entre aspas!
count.count('o') - nesse comando eu peço para o python contar
quantas vezes aparecem a letra o, minúscula: 
  
           _                   _             _        Obs: count = contar
| C u r s |o|   e m   V í d e |o|   P y t h |o| n |
| 0 1 2 3 |4| 5 6 7 8 9 1 1 1 |1| 1 1 1 1 1 |1| 2 | 
|         | |           0 1 2 |3| 4 5 6 7 8 |9| 0 | 
           -                   -             -
           
Então nesse caso, frase.count('o') - "o" entre aspas, senão
ele vai achar que é uma variável -, vai contar quantas vezes
existe a letra o. Que no caso é 3. Se você der um 
print(frase.count('o')), ele irá te mostrar o valor 3.
    
    
Alteração sugerida no comando:

frase.count('o', 0, 13) - esse 0 e 13 adicionais, significa
uma contagem já com fatiamento. 
Então com esse comando, ele vai considerar do 0 até o 13
(lembrando que o 13 não será incluído, indo do 0 até o 12),
ele vai me imprimir o valor 1.
Porque: entre o caracter 0 e 13, sem contabilizá-lo, ou seja,
do 0 ao 12, eu tenho apenas uma letra o. Por isso o 1.   
    
           _                  ^---> Esse será ignorado, pois o 
| C u r s |o|   e m   V í d e o   P y t h o n |  último valor
| 0 1 2 3 |4| 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 |   não é contado.
|         | |           0 1 2 3 4 5 6 7 8 9 0 | 
           - 
 
Então vai me mostrar o valor 1. 
    
    
Outra:

frase.find('deo') - vai me dizer quantas vezes ele encontrou, 
porque "find" = encontrar, "deo" (d, e, o). Dentro de
"Curso em Vídeo Python", eu tenho "deo". Só que ele vai
dizer em que momento começou "deo". 

                         ^--> começou aqui!
| C u r s o   e m   V í |d e o|   P y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 |1 1 1| 1 1 1 1 1 1 2 | 
|                     0 |1 2 3| 4 5 6 7 8 9 0 |    
                         -----

O "deo" foi encontrado no 11,12,13 mas começou na posição 11.
Então frase.find('deo') vai me mostrar 11 porque o "deo" 
foi encontrado começando na posição 11.        
    

Outro ex com o find:

frase.find('Android')     
    
Dentro da string (Curso em Vídeo Python) não tem Android.

Se você coloca dentro do find uma string que não existe, ele
te retorna o valor -1. Não existe posição -1, ele começa no 0.
Então se você receber o valor -1, significa que o find não
achou a string que você pediu, dentro da cadeia de string 
original. Ou seja, ex: O find não achou 'Android' em 
'Curso em Vídeo Python':. 

frase.find('Android') = -1.  Lembrando que: frase = 'Curso em Vídeo'
                                                        Pyhton
O que, ou seja, -1 = não foi encontrado.     
    
    
Outro de análise:

'Curso' in frase  = existe a palavra "Curso" dentro (in) de
frase (variável)?   
    
Obs: Para dizer em qual posição está, é preciso usar o find.
O operador "in", trabalha com True e Falsa, com o começo
maiúsculo.

Então: 'Curso' in frase - ou seja, existe Curso em frase?
- sim. Dentro de frase eu tenho, sim, a palavra "Curso".
Então ele vai escrever: True.   


Agora vamos para outra categoria de funcionalidades que podem
ser feitas em string:


Transformação - via de regra, uma lista de string, é imutável
(não da pra mudar; mexer nela), mas é possível mudar ela,
através dos métodos. Não consigo mexer diretamentenos 
elementos, mas indiretamente com os métodos.

ex:
        ^--> = trocar; reposicionar
frase.replace('Python', 'Android') - esse comando vai procurar 
por "Python", depois de encontrar, ele vai substituir por
Android.
Então onde tiver Python, ele vai substituir por Android:


| C u r s o   e m   V í d e o   P y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|                     0 1 2 3 4 5 6 7 8 9 0 |

Então se eu desse: print(frase.replace('Python', 'Android')), 
ficaria "Curso em Vídeo Android": 


| C u r s o   e m   V í d e o   A n d r o i d |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 1 |
|                     0 1 2 3 4 5 6 7 8 9 0 3 |


Perceba que para colocar "android", será necessário adicionar 
uma letra no final: o próprio python faz isso!  


Tem também o:

            ^> Tem abrir e fechar parênteses!
frase.upper() - upper = pra cima. Então significa que vai ficar
em maiúsculas as letras. Então em "Curso em Vídeo Python", eu
tenho somente o c, o v, e p, maiúsculo (as letras C, V, P
maiúsculas). 

Então ele vai vazer o seguinte: o  que já for maiúsculo
ele mantém e todas as letras minúsculas, ele troca;
transforma em maiúsculas. 


| C U R S O   E M   V Í D E O   P Y T H O N | --> tudo ficou maiúsculo!
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|                     0 1 2 3 4 5 6 7 8 9 0 |



Outro:
            ^> põe o parênteses também!
frase.lower() - é o contrário o upper, mantendo entãoo que era
minúsculo e substitui o que estava em maiúsculo por minúsculo.

Assim:  


| c u r s o   e m   v í d e o   p y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|                     0 1 2 3 4 5 6 7 8 9 0 |

Note que o c, v, p estavam em maiúsculas, agora estão em 
minúsculas.


mais de transformação:
                |> também bota o parenteses
frase.capitalize() - pega uma string inteira, vai jogar tudo
para minúsculo e a primeira letra maiúsucla. Mas só a primeira.


Assim: 


| C u r s o   e m   v í d e o   p y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|                     0 1 2 3 4 5 6 7 8 9 0 |

Só o c ficou maiúsculo. 


de maneneira similar, temos o:

            ^> bota o parenteses
frase.title() - analisa quatas palavras tem essa string, por meio
dos espaços entre elas, fazendo uma quebra de palavras onde
tiver espaços. Então ele vai fazer igual o capitalize, só que
palavrapor palavra: 


| C u r s o   E m   V í d e o   P y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|                     0 1 2 3 4 5 6 7 8 9 0 |

Veja que todas as palavras agora começam com letras maiúsculas.
O restante é mantido em minúsculo.
 

Mais de transformação, mas mudemos o exemplo:

ex: frase =  |       A p r e n d a   P y t h o n     |    
             | 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 |
             |                     0 1 2 3 4 5 6 7 8 |

Perceba que agora tem esses espaços antes e depois da string:
eles podem ser inúteis, por isso, existem algumas funções

como por exemplo o

            ^> tbm põe o parenteses
frase.strip() - remove todos os espaços inúteis no início e no
final da string. O espaço do meio será mantido.         

Assim: 


| A p r e n d a   P y t h o n |  --> perceba que os espaços inúteis
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 |    sumiram e o "A" que tinha o índice
|                    0 1 2 3  |   3, agora é 0. 

Ou seja, "A" passou a ser o primeiro caractr e a contagem
segue normamente até o 13, visto que os espaços da direita
também foram removidos.


De forma similar temos o

      ^> Esse "r" = right = direita - Obs: muitas funcionalidades dentro       
frase.rstrip()  - bota o parenteses também.    do python que tratam strings, 
                                                    tem a variação r.
Dica: tem algumas funcionalidades que você pode 
colocar um r na frente para começar a tratar pela direita.
              

Sobre o rstrip: se eu boto rstrip, ele vai remover somente os
espaços da direita ou os últimos espaços. Se tiver espaços no
início, ele não vai remover. 

Assim:


|       A p r e n d a   P y t h o n | --> removeu os dois espaços!    
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 |
|                     0 1 2 3 4 5 6 |

Então minha string vai de 0 a 16, tendo agora um len, ou seja,
um lenf = comprimento de 17 caracteres.


E de forma idêntica temos o

      ^> Esse "l" = left = esquerda
frase.lstrip() - bota o parênteses - vai remover os espaços da
esquerda e mantém os da direita.

Assim:


| A p r e n d a   P y t h o n     |    
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 |
|                     0 1 2 3 4 5 |



Então se no seu programa você quiser tirar só os espaços da
direita: rstrip, só os da esquerda: lstrip, quer tirar todos
os espaços das extremidades: strip


Vamos agora voltar pro ex: Curso em vídeo Python e passar para
funcionalidades de 

Divisão - é possível dividr strings - essa é uma funcionalidade
útil para desafios que você encontrar na vida de programador. 


Primeira função a ser vista:

       ^> split = divisão. E põe o parenteses!
frase.split() - por padrão, o split é feito em seus espaços.
Vai ocorrer uma divisão dentro da sua string, considerando
os espaços. Ele vai pegar onde tiver espaço e criar uma
divisão, um split. 

Então: Curso em Vídeo Python, antes era assim:


| C u r s o   e m   v í d e o   p y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 | 
|                     0 1 2 3 4 5 6 7 8 9 0 |


Com o split ficará assim:

 _________     ___     _________     ___________
|C u r s o|   |e m|   |v í d e o|   |p y t h o n|
|0 1 2 3 4|   |0 1|   |0 1 2 3 4|   |0 1 2 3 4 5| 
 ---------     ---     ---------     -----------   

Perceba que de "curso" para "em" a numeração recomeçou, 
refazendo os índices e ele dividiu as palavras e que
cada uma recebe indexação nova.

E cada uma delas é colocada dentro de uma outra lista, 
então o split gera, tecnicamente, uma lista em todas 
as palavras de uma cadeia de caracteres.

Então ele vai separar em pedaços e eles terão numerações:

 __________     ___     _________    ___________
| C u r s o|   |e m|   |v í d e o|  |p y t h o n|
| 0 1 2 3 4|   |0 1|   |0 1 2 3 4|  |0 1 2 3 4 5| 
|          |   |   |   |         |  |           |
 ----------     ---     ---------    -----------
     0           1          2             3


Ou seja: a palavra 0 é "Curso", a palavra 1 é "em", a
palavra 2 é "Vídeo" e a palavra 3 é "Python".

Então o split vai dividir uma string em uma lista, onde
cada elemtento será separada pelo seu splitador, caracter
de split, que por padrão é o espaço ( ).

* dar uma pesquisada no split.


E parecido com o split, considerando a divisão feita acima,
da funcionalidade 

Junção - Serve para juntar stings separadas.


Temos o 

'-'.join(frase) - se eu tenho nomes separados em listas, eu 
 | consigo utilizar o "join" para juntar uma coisa na outra.
 |
 > aqui eu botei uma string (tracinho).join(frase) - que 
significa que vai juntar todos os elentos de ^>frase (0, 1
2 e 3) e vai usar aquele separador, que é o "tracinho" (-)

Então estava assim: 


 __________     ___     _________    ___________
| C u r s o|   |e m|   |v í d e o|  |p y t h o n|
| 0 1 2 3 4|   |0 1|   |0 1 2 3 4|  |0 1 2 3 4 5| 
|          |   |   |   |         |  |           |
 ----------     ---     ---------    -----------
     0           1          2             3

E com o '-'.join(frase), ele me geraria uma string única,
de novo uma cadeia de caracteres, com essa configuação:

    
| C u r s o - e m - v í d e o - p y t h o n |
| 0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 |  
|                     0 1 2 3 4 5 6 7 8 9 0 |


Note que quando eu tinha espaços, ela juntou um com outro e
colocou um - (tracinho), que é exatamente o tracinho do '-'.join(frase)
                                                '--------^

Se você quiser que tenha, no lugar do tracinho tenha espaços, é só
colocar um espaço em branco dentro das aspas do .join.
        
Assim: ' '.join(frase) 
        '-> *Espaço em branco!*
'''

'''
Se você tiver um texto grande e quiser dar um print nele (mostrar
na tela), basta, antes do texto, abrir aspas três vezes,e no
final do texto, fecha aspas três vezes:

Ex:
print("""blablablablablablablalablablablablabalbalablablabalbalbalbalbal
blablablablablablabalbalbalbalalabblablabalbalbalbalbalabalblablabla
blablabalbalbalbalbalblablablablbalbalbalabblablabalbalbal""")

Pode fazer com aspas simples também!
'''

'''
No python, tudo é um objeto: então você pode botar alguma coisa
. (ponto) alguma coisa.

ex: 

frase = 'Curso em Vídeo Python'
print(frase.upper().count('o'))
   |                '-> é só usar uma em seguida da outra.
   '-> Aqui eu jogo a frase para maiúscula e conto quantas
   vezes aparece a letra o.
   
Então você combinar uma coisa com a outra.


Você também pode colocar essas funções dentro do parênteses
do .format, direto

Ex:

n = str(input('Digite seu nome: '))                ^> Aqui ó!
print('Seu nome em maiúsculo fica assim'.format(n.upper()))  
'''

'''
Você também pode mostrar o primeiro item da lista:

ex:

frase = 'Curso em Vídeo Python'
dividido = frase.spit()
print(dividido)

Esse programa vai mostrar a lista: ['Curso', 'em', 'Vídeo', 'Pyhton']

Mas com um colchete e um número (por exemplo o 0), mostra algum
item da lista:

ex: frase = Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0]) --> esse primeiro colchete mostra o 1º item 
                                                      da lista
Então o programa vai exibir: Curso


E o segundo colchete é para mostrar a letra:

ex:

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3]) --> aqui eu tô dizendo: pega o divido 2,
que é "Vídeo" e me mostre a letra 3.

o programa vai exibir então a letra e. Porque é a 3ª letra
'''

'''
Lembre-se: "A teoria só te leva até certo ponto". 
Ou seja, praticando você irá encontrar detalhes que não
observou na teoria.
'''

'''
Quando o exercício é grande, é recomendado reolver ele em partes:
faz um pouco, vê se está funcionando e continua
'''

'''
É importante também, mesmo que você tenha resolvido o exercício
corrtamente, assistir o vídeo de resolução dele, pois pode
descobrir outras funções e recebendo dicas que não foram
dadas durante aula.  
Mas claro que você pode pular a vinheta, ir logo para a 
resolução e pular o final tbm (depois que o exercício
já foi resolvido e explicado).
'''

'''
É possível usar o .strip(), e qualquer outra funcionalidade, direto 
na linha depois da input, depois de você dizer pro python que
está trabalhando com strings:

Ex:

     ^> Aqui tu diz que está trabalhando com string  
nome = str(input('Digite seu nome completo: ')).strip() --> strip, para 
                                                            remover os 
Então aqui eu faço: a leitura de um nome completo,           espaços!
sendo uma string cortada; ou seja, já vai ser uma
string com os espaços eliminados antes e depois. 
Muito útil essa função!

Obs: Para usar esse .strip(), e qualquer outra função no final
da linha, é preciso dizer que se está trabalhando com string
(O str na frente do input)!!!
O .strip() é só um exemplo. Pode-se usar qualquer outra função
na mesma linha. 


Também pode-se verificar quantos espaços há entre as letras
(strings): .count(' ')  --> o count vai contar quantos espaços
tem, ou seja, a quantiade de espaços entre as letras.

E também pode remover os espaços entre as letras diminuindo do
.count(' ')

Ex de cima:

nome = str(input('Digite seu nome todo: ')).strip()
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
                                               ^-<_
Então aqui eu tô fazendo, (começando a partir do len): o tamanho
do nome menos quantos espaços tem; isto é, a quantidade de 
letras ao todo com espaço (len(nome)) - (menos) quantos
espaços tem (nome.count(' ')).


E você ainda pode, ainda no exemplo anterior:

pesquisar dentro do nome, o primeiro espaço:

Ex: 

nome = str(imput('Digite seu nome todo: ')).split()       ^> Espaço vazio!
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

Ou

Eu posso separar os nomes e pô-los dentro de uma lista:

nome = str(input('Digite seu nome todo: ')).split()
separa = nome.split()  --> isso vai criar uma lista com os nomes
print('Seu primeiro nome tem {} letras'.format(separa[0], len(separa[0])))
                                             ^                 ^
Para eu saber o primeiro nome, basta mostrar ^ o primeiro item ^ da 
lista, que é o item (elemento) 0. Então: separa[0] é o primeiro^
nome (item/elemento), e ele tem tantas letras.                 ^
Para saber quantas letras ele tem, eu faço o len de separa[0]->^, 
isto é, quantas letras tem o primeiro nome.
'''

'''
Para verificar se algo é igual a outro, utiliza-se dois sinais
de igual (==).

Ex:

cid = input('Em que cidade você nasceu? ')
print(cid[:5] == 'Santo')  --> Aqui eu tô dizendo (verificando)
se a cidade (cid = nome da cidade) é igual a 'Santo'.
 
 
Ou assim:

cid = input('Em que cidade você nasceu? ').strip()
print(cid[:5].upper() == 'SANTO') --> desse jeito, qualquer 
maneira que for digitado, eu vou jogar tudo para maiúscula e 
na hora de testar, eu testo por maiúsculo.
'''

'''
Você como pogramador, tem que sempre pensar se o usuário
vai fazer besteira na hora e digitar. E na maioria das vezes,
ele faz.
'''

'''
É importante também você criar seus próprios exercícios, e 
usar sua imaginação para situações adversas (resolução de
problemas), e não fique preso aos exercícios do curso.
'''

'''
Estudando if: 

if - para estruturas simples
else - para estruturas compostas (2 ou +)

Ao usar if ou else, lembra de colocar : (dois pontos) do lado.

Ex:

tempo = int(input('Quantos anos tem seu carro?'))
if = tempo <=3: ----> aqui ó!
    print('carro novo')
else: ----> ó!
    print('carro velho')
    
obs: todo programa que tiver colado do lado esquerdo da tela,
será executado sempre! 
Agora todo programa que tiver mais afastado (uma tecla "tab"
de distância) pode ou não ser executado.

Então no nosso caso aqui (programa de cima, do tempo),
ou ele vai escrever "carro novo" ou vai escrever "carro velho".

Entenda: nunca vai acontecer uma situação onde: seu carro
é novo e seu carro é velho. Não existe essa possibilidade.

Você também pode fazer assim, o código:

tempo = int(input('Quantos anos tem seu carro?')
print('carro novo' if tempo<=3 else 'carro velho')

Ou seja: se o tempo for menor ou igual a 3, escreva 'carro novo'.
Caso não, ou seja, o tempo for maior, escreva 'carro velho'.

Então:

if = para condições simples
else = para condições compostas
if e else (na mesma linha) = é uma condição simplificada

Obs: if e else, não precisam necessariamente serem atribuídos à uma variável.
Mas para dizer que algo é igual, menor ou igual ou maior ou igual 
(==, <=, >=), tem que por a variável depois do if. Mas só no if.

Ex:
    ^> variável      ^>> e não esquece do bendito dois pontos!
if macaco == 'animal':

'''

'''
Lembrando: para igualar alguma coisa, tipo variáveis, não usa o sinal
de igual (=), usa dois (==). Um sinal só = pertence.
'''

'''
No if e no else, é possível escrever vários "prints" atribuídos 
a eles. Todos com um tab de distância.


É possível escrever vários IFs: quantos você quiser. Porém, não pode
colocar mais do que um ELSE.
Assim, se você escrever vários IFs, o ELSE serve para fechar os 
SEs (condições) que você escreveu, representando literalmente
SENÃO para se não for de acordo com os IFs.
Ou seja, o ELSE é qualquer outro evento que não seja esperado pelo
IF. Isto é, qualquer outra possibilidade.


É possível colocar um if depois (na linha debaixo) de um else.
Mas, obviamente, o else será executado antes do if, podendo 
alterar o resultado do seu código!
'''

'''
And = e. Serve para adicionar algo ou uma condição ao programa

Or = ou. Serve para. sla

Sinal de diferente no python: !=
Sinal de igual: == 
'''

'''
É importante que ponhamos comentários (feitos com #) para sabermos
o que estamos fazendo e em que parte do código estamos. Ponha comentários!
'''


'''
Sempre que você quiser representar uma cor em python, você vai começar
com \033[ (contrabarra, 0, 33, abre colchete). E fechar o código com um
m: \033[m. Entre esse colchete e esse "m", você vai colocar o código 
da cor.

Logo ficará assim:

\033[         m
        '----> Entre o colchete e o m, você pode colocar: nenhum código,
        1 código, 2 ou 3 códigos.

Ex: 

\033[0;33;44m

      
Todo código ANCI pra cor que a gente vai utilizar no python começa com
\033[3 valores: um p/ estilo, o 2º p/ texto e o 3º p/ fundo - lembrando
que todos são opicionais: você pode utilizar um e não utilizar outro
sem problema nenhum, pode também colocá-los em qualquer ordem - e, 
por fim, uma letra m, minúscula.


Existem vários códigos para estilo: 

0 - none - sem estilo nenhum - pode botar 0 ou não por nada, dá no mesmo
1 - bold - coloca o texto em negrito
4 - underline - coloca o texto em sublinhado
7 - negative - inverte as configurações: o que você colocou para fundo, 
ele coloca para letra, e o que você colocou para letra, ele vai pra fundo.


Cor do texto:

Todas começam com 3. É do 30 até o 37.

30 - branco 
31 - vermelho
32 - verde 
33 - amarelo
34 - azul
35 - magenta
36 - ciano
37 - cinza


Background ou Back ou simplesmente fundo:

Mesma coisa da cor do texto: tem as mesmas cores, só que em vez de 
ser do 30 até 37, é do 40 até 47.

40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - magenta
46 - ciano
47 - cinza
'''

'''
Você utiliza o \033[m dentro das aspas, indicando que é um texto, ou parte
dele, e logo antes da primeira letra do seu texto. Colado com a primeira 
palavra!!!

Ex:
             ^----> texto
print('\033[mOlá, Mundo!')
       '    '   
        '  '
         '
        código para cor
        

E para tirar as formatações no final (deixar do jeito original), basta
usar esse código no final do texto que você escreveu, mas antes das
aspas também. Para indicar que está mexendo com o texto.

Assim:

Ex:
                                ^----> Tira a formatação ao final do texto.
print('\033[1;31;43Olá, Mundo!\033[m')     Isto é, formata o texto e depois
        '---> formatação de texto                para de formatar. 
                                      (para qualquer coisa que venha depois)
                                      

Se você por um 7 no estilo, num código de cor, faz-se com que 
altere o que está sendo pedido:

Ex:

print('\033[33;44mOlá, Mundo!') - pelas configurações de cor, você
está querendo colocar o texto amarelo e o fundo azul.

Mas se você põe o 7 na frente, altera-se o que está sendo pedido:

print('\033[7;33;44mOlá, Mundo!') - Isso quer dizer que você quer
colocar fundo amarelo e texto de cor azul.

O 7 inverte o comando.


- pesquisar sobre o modo colorise. No python.org


É possível também colocar cor em números separados:

Ex:

a = 3    - até aqui você já sabe
b = 5
print('Os valores são {} e {}'.format(a, b))

- Mas se eu colocar códigos de cor antes das chaves....

a = 3    
b = 5
print('Os valores são \033[32m{} e \033[31m{}'.format(a, b))

Resultado: o 3 e o 5 sairão verde e vermelho!

Obs: o "e" também vai sair verde, pois não há nenhum código de cor
para deixá-lo normal: o código de cor amarelo para o 3, também 
atinge o "e".

Para consertar isso basta cancelar as cores, adicionando código de cor
sem nenhuma formatação. Assim como a gente fez no "olá mundo", lá em cima:

Ex:
                                                    ^---> para cancelar a cor depois do 5.
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
                                  '---> para cancelar a cor depois do 3.
        


Macete para se você não conseguir escrever os prints gigantes e quer deixar mais
organizado:

Ex:

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}!'.format(nome)) - até aqui você também já sabe       
        
Mas se você quiser trabalhar com cores.....   

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(nome))     

Você pode abrir mais chaves, para abrir o código de cor e outra para fechá-lo.
1ª chave - abre código de cor
2ª chave - nome
3ª - fecha o código de cor

Ficando assim:
                                             >----------------------------
nome = 'Guanabara'                         '-|--------------------|      |
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(\033[m, nome, \033[m)) 
                                         ´----------------^
          
Aí você decide a formatação que desejar. Mas o macete é esse.
        
        
 
E um último jeito: chamado dicionário.

Consiste em fazer uma lista com todos as ferramentas, no caso cores, que você vá precisar.


Ex:

nome = 'Guanabara'                     - Basicamente, eu criei cores no meu sistema, que 
cores = {'limpa':'\033[m',                    são limpa, azul, amarelo e pretoebranco
         'azul':'\033[34m',
         'amarelo':'\033m'
         'pretoebranco':'\033[7;30'}
print(Olá, Muito prazer {}{}{}!!.format(cores['amarelo'], nome, cores['limpa']       
                                                ^
                                                ^---> Aqui que você muda as cores:
                                se trocar para 'azul', o print vai sair azul (Olá, Muito
                                prazer......). Se trocar para 'pretoebranco', o 
                                print vai sair preto com fundo branco.
                                
Obs: você também pode mudar no último "cores" (no .format), mas aí, sairia uma
linha infinita com a cor que você selecionasse. Visto que o \033[m sozinho, 
cancela as formatações.                 
'''




