from time import sleep
print('|||||'*10)
print('  CALCULE SEU IMC - Jéssica Araújo NUTRICIONISTA')
print('|||||'*10)
nome = str(input('Qual seu nome? '))
print('''Qual seu sexo?
[ 1 ] - HOMEM
[ 2 ] - MULHER''')
sexo = int(input('Digite a opção: ').strip())
print('====' * 20)
if sexo == 1:
    print(f'''Seja bem-vindo {nome}, sou Jéssica Araújo nutricionista
e irei calcular seu IMC :D''')
else:
    print(f'Seja bem-vinda {nome}, sou Jéssica Araújo nutricionista e irei calcular seu IMC :D')
print('===='* 20)
peso = float(input(f'{nome}, me informa o seu peso atual: ').strip())
altura = float(input(f'Agora me informa a sua altura: ').strip())
print('====' * 20)
print(f'Só aguarda um momento {nome}, que irei calcular seu IMC...')
print('===='* 20)
sleep(2)
imc = peso / (altura**2)
if imc < 18.5:
    print(f'{nome}, seu IMC é de {imc:.2f} kg/m² e está abaixo do recomendado.  ')
elif 18.5 <= imc < 25:
    print(f'Parabéns, {nome}! Seu IMC é de {imc:.2f} kg/m² e você está no peso ideal. ')
elif 25 <= imc < 30:
    print(f'{nome}, seu IMC é de {imc:.2f} kg/m² (SOBREPESO). Hora rever seus hábitos alimentares!')
elif 30 <= imc < 40:
    print(f'CUIDADO! {nome}, seu IMC é de {imc:.2f} kg/m² e você está em um grau de OBESIDADE!'
          f' Procure um NUTRICIONISTA. ')
else:
    print(f'''PERIGO! {nome}, seu IMC é de {imc:.2f} kg/m² e está em um grau de OBESIDADE MÓRBIDA!!
     PROCURE IMEDIATAMENTE um NUTRICIONISTA!! ''')
    print('Entre em contato comigo!')





