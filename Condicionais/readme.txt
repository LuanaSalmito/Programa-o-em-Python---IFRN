#Maior média ponderada:#

Ao entrar na faculdade Eduzinho se deparou com um professor que fazia a avaliação de forma um pouco diferente dos tradicionais. O semestre na universidade de Eduzinho é dividido em exatamente 2 etapas e1 e e2, cada uma com um peso diferente p1 e p2. Dessa forma o cálculo da média m é feito pela fórmula
O professor Faísca, para permitir uma flexibilidade maior aos alunos realiza, em cada etapa, 2 avaliações, sendo a11 e a12 as duas avaliações da primeira etapa e a21 e a22 as duas avaliações da segunda etapa. Assim o professor Faísca permite que o aluno escolha qual média será usada entre 2 (duas) possível médias. A primeira média possível, m1 ser usada é a utilização da avaliação 1 em cada uma das etapas, sendo calculada pela fórmula
A segunda média, m2 é calculada usando a avaliação 2 em cada uma das etapas, pela fórmula
Como Eduzinho não gosta de fazer contas e o professor Faísca usa a avaliação de acordo com a escolha do aluno, ele pediu sua ajudar para decidir se diz ao professor Faísca para usar a avaliação 1 ou a avaliação 2. Caso as médias sejam iguais Eduzinho vai sempre escolher a primeira média, m1.
Input:
A entrada é composta de 3 (três) linhas. A primeira linha contém dois números inteiros a11 e a21 (0 ≤ a11, a21 ≤ 108), que são as notas da avaliação 1 para as etapas 1 e 2, respectivamente. A segunda linha possui dois inteiros a12 e a22 (0 ≤ a12, a22 ≤ 108), que são as notas da avaliação 2 pas etapas 1 e 2, respectivamente. A terceira linha contém 2 (dois) números inteiros p1 e p2 (1 ≤ p1, p2 ≤ 103), os pesos das etapas 1 e 2, respectivamente.
Output:
Seu programa deve mostrar uma única linha com um número inteiro a informando qual avaliação Eduzinho vai pedir ao professor Faísca para usar. Todos os cálculos devem ser feitos utilizando valores inteiros, desprezando-se as casas decimais.



#Máquina de Café:#
O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 andares. Em determinadas épocas do ano, os funcionários da SBC bebem muito café. Por conta disso, a presidência da SBC decidiu presentear os funcionários com uma nova máquina de expresso. Esta máquina deve ser instalada em um dos 3 andares, mas a instalação deve ser feita de forma que as pessoas não percam muito tempo subindo e descendo escadas.
Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do andar onde trabalha até o andar onde está a máquina e voltar para seu posto de trabalho. Todo funcionário leva 1 minuto para subir ou descer um andar. Como a SBC se importa muito com a eficiência, ela quer posicionar a máquina de forma a minimizar o tempo total gasto subindo e descendo escadas.
Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a minimizar o tempo total gasto pelos funcionários subindo e descendo escadas.
Input:
A entrada consiste em 3 números, A1 , A2 , A3 (0 ≤ A1, A2, A3 ≤ 1000), um por linha, onde Ai representa o número de pessoas que trabalham no i-ésimo andar.
Output:
Seu programa deve imprimir uma única linha, contendo o número total de minutos a serem gastos com o melhor posicionamento possível da máquina.


#Escolha difícil.#

Em um longo voo, companhias aéreas oferecem uma refeição aos seus passageiros. Geralmente as aeromoças conduzem carrinhos contendo as refeições pelos corredores do avião. Quando o carrinho chega em sua fileira, você é questionado imediatamente: "Frango, bife, ou massa?". Você sabe suas opções, mas você tem apenas alguns segundos para escolher e você não sabe qual a aparência de sua escolha pois seu vizinho ainda não abriu o embrulho ...
A aeromoça deste voo decidiu alterar o procedimento. Primeiro ela vai perguntar a todos os passageiros qual sua escolha de refeição, e depois vai checar se o número de refeições disponíveis neste voo para cada escolha é suficiente.
Por exemplo, considere que o número de refeições de frango, bife e massa disponíveis são respectivamente (80, 20, 40), enquanto o número de passageiros que escolheu frango, bife e massa seja respectivamente (45, 23, 48). Neste caso, onze pessoas seguramente ficaram sem suas respectivas escolhas de refeição, já que três passageiros que queriam bife e oito que gostariam de massa não poderão ser atendidos.
Dada a quantidade de refeições disponíveis para cada escolha e o número de refeições pedidas para cada escolha, você poderia por favor ajudar a aeromoça a determinar quantos passageiros seguramente não poderão ser atendidos?
Input:
A primeira linha contem três inteiros Ca, Ba e Pa (0 ≤ Ca, Ba, Pa ≤ 100), representando respectivamente o número de refeições disponíveis de frango, bife e massa. A segunda linha contem três inteiros Cr, Br e Pr (0 ≤ Cr, Br, Pr ≤ 100), indicando respectivamente o número de refeições requisitadas de frango, bife e massa respectivamente.
Output:
Imprima uma única linha com um inteiro representando o número de passageiros que seguramente não receberão sua escolha de refeição.


#Triangulo#

Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.
Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.
Input:
A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

Output:
Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser 'S' caso seja possível formar o triângulo, ou 'N' caso não seja possível formar o triângulo.


#Frota de Taxi#

A Companhia de Táxi Tabajara (CTT) é uma das maiores empresas de transporte do país. Possui uma vasta frota de carros e opera em todas as grandes cidades. Recentemente a CTT modernizou a sua frota, adquirindo um lote de 500 carros bi-combustíveis (carros que podem utilizar como combustível tanto álcool quanto gasolina). Além do maior conforto para os passageiros e o menor gasto com manutenção, com os novos carros é possível uma redução adicional de custo: como o preço da gasolina está sujeito a variações muito bruscas e pode ser vantagem, em certos momentos, utilizar álcool como combustível. Entretanto, os carros possuem um melhor desempenho utilizando gasolina, ou seja, em geral, um carro percorre mais quilômetros por litro de gasolina do que por litro de álcool.

Você deve escrever um programa que, dados o preço do litro de álcool, o preço do litro de gasolina e os quilômetros por litro que um carro bi-combustível realiza com cada um desses combustíveis, determine se é mais econômico abastecer os carros da CTT com álcool ou com gasolina. No caso de não haver diferença de custo entre abastecer com álcool ou gasolina a CTT prefere utilizar gasolina.
Input:
A entrada é composta por uma linha contendo quatro números reais com precisão de duas casas decimais A e G (0.01 ≤ A, G ≤ 10.00) Ra e Rg (0.01 ≤ Ra, Rg ≤ 20.00) representando respectivamente o preço por litro do álcool, o preço por litro da gasolina, o rendimento (km/l) do carro utilizando álcool e o rendimento (km/l) do carro utilizando gasolina.
A entrada deve ser lida do dispositivo de entrada padrão (normalmente o teclado).
Output:
A saída deve ser composta por uma única linha contendo o caractere 'A' se é mais econômico abastecer a frota com álcool ou o caractere 'G' se é mais econômico ou indiferente abastecer a frota com gasolina.
A saída deve ser escrita no dispositivo de saída padrão (normalmente a tela).

#Tanque de Combustível#

Cássio alugou um carro para a viagem de férias. O carro tem consumo de combustível constante (em kilômetros rodados por litro de combustível), independente da velocidade com que trafega. Ao fim da viagem, Cássio deve devolver o carro no aeroporto. Cássio está terminando sua viagem de férias e está no momento na rodovia que leva ao aeroporto, em direção ao aeroporto para devolver o carro. Mais precisamente Cássio está no último posto de combustível existente na rodovia em que ele pode abastecer o carro antes de devolvê-lo. Para economizar o máximo possível em combustível, Cássio quer devolver o carro com o menor número de litros possível no tanque – idealmente, com o tanque zerado, ou seja, sem combustível. Dados o consumo do carro, a distância em que se encontra do aeroporto e a quantidade de combustível presente no tanque antes do abastecimento, determine qual deve ser a menor quantidade de combustível que Cássio deve comprar
Input:
A primeira linha contém um inteiro, C (1 ≤ C ≤ 50), o consumo do carro em kilômetros rodados por litro de combustível. A segunda linha contém um inteiro D (1 ≤ D ≤ 1000), a distância do aeroporto, em kilômetros. A terceira linha contém um inteiro T (1 ≤ T ≤ 100), o número de litros de combustível presente no tanque antes do abastecimento. Você pode assumir que o tanque tem capacidade suficiente para armazenar todo o combustível que Cássio comprar.
Output:
Seu programa deve produzir uma única linha, contendo um único valor, com um dígito de precisão, indicando a quantidade de combustível que Cássio deve comprar, para chegar ao aeroporto com o tanque contendo a menor quantidade de combustível possível.

#Maior de 5 numeros#

Escreva um programa que leia 5 números e mostre o maior dos 5.

Input:
A entrada é composta de 3 números inteiros a, b, c, d e e ( - 10000 ≤ a, b, c, d, e ≤ 10000), cada número em uma linha.

Output:
A saída deve conter uma única linha com um número inteiro, o maior dos 5 números lidos.

