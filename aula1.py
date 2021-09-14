#Programa recebe dados do usuário e informa se pode ser doador de sangue.
#Não pode doar: Não pode ter idade menor que 19 anos e mais que 69 anos | Peso menor que 50kg 
#| Ingestao de alcool nas ultimas 12hs | Ter feito tatuagem no ultimo ano.

#Declaração de variaveis
imped_idade =''
imped_peso =''
imped_bebida =''
imped_tatuagem =''
idade = int (input('Digite a idade:'))
peso = int (input('Digite o peso:'))
bebida = int (input('Ingeriu bebida alcolica nas ultimas 12hs? Digite: 1- Para sim ou 2- Para não: '))
tatuagem = int (input('Fez alguma tatuagem no ultimo ano? Digite: 1- Para sim ou 2- Para não: '))
#Testes de apto ou inapto
if idade < 19 or idade > 69:
    imped_idade = "Idade fora da faixa de doação."

if peso < 50:
    imped_peso = 'Peso inferior a 50kg.'

if bebida ==1:
    imped_bebida ='Ingestão de bebida alcoólica.'

if tatuagem ==1:
    imped_tatuagem ="Tatuagem recente."        

if (imped_idade !='') or (imped_peso !='') or (imped_bebida !='') or (imped_tatuagem !='') :
    print ('Não pode doar, motivo: ' + imped_idade + " " + imped_peso + " " + imped_bebida + " " + imped_tatuagem)

else: 
    print ('Pode doar sangue')