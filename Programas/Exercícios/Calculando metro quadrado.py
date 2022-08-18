#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Qual a altura da parede?: '))
largura = float(input('Qual a largura da parede? '))
m2 = largura * altura #valor do metro quadrado
print(f'Sua parede tem {m2:.2f}m² para pintar ela você vai precisar de  {m2 / 2:.2f}L de tinta') 

#o :.2f serve para só 
# aparecer duas casas depois da virgula por conta do float. Ex: 10.01 duas casas, 
# com 3 ficaria ":.3f" = 10.012