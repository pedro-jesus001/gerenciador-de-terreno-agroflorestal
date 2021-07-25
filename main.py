'''
authors: Los-had, pedro-jesus001
license: MIT
repository: https://github.com/pedro-jesus001/gerenciador-de-terreno-agroflorestal
'''
import math

def main():
  # menu do programa
  print('-' * 65)
  print('[1]. Calcular área.\n[2]. Calcular quantos objetos de um tamanho especifico é possível colocar em uma área.\n[3]. Sair')
  print('-' * 65)
  choice = input(' >  ')
  # calcula uma área retangular
  # 3 medidas são aceitas nessa função: KM, M e CM
  def CalcularArea(n1, n2, med):
    # verifica se alguma medida passada é menor ou igual a zero
    if (n1 <= 0) or (n2 <= 0):
      print('Nenhuma das medidas colocadas podem ser menor ou igual a zero.')
    else:
      try:
        resultado =  float(n1) * float(n2)
        if med == 'km':
          # converte km para m
          km_para_m = resultado * 1000 
          # converte km para cm
          km_para_cm = resultado * 100000
          print(f'Um terreno de {str(n1)}KM  x {str(n2)}KM tem a área de {str(resultado)}km², tem {str(km_para_m)}m² e também tem {str(km_para_cm)}cm²')
        elif med == 'm':
          # converte m para km
          m_para_km = resultado / 1000
          # converte m para cm
          m_para_cm = resultado * 100
          print(f'Um terreno de {str(n1)}M x {str(n2)}M tem a área de {str(resultado)}m², tem {str(m_para_km)}km² e também tem {str(m_para_cm)}cm²')
        elif med == 'cm':
          # converte cm para m
          cm_para_m = resultado / 100
          # converte cm para km
          cm_para_km = resultado / 100000
          print(f'Um terreno de {str(n1)}CM x {str(n2)}CM tem a área de {str(resultado)}cm², tem {str(cm_para_m)}m² e também tem {str(cm_para_km)}km²')
      except TypeError:
        # mostra um erro se o usuário colocar uma string
        print('Apenas números positivos são aceitos nas medidas e apenas suportamos KM, CM e M')
      except ZeroDivisionError:
        # verifica se algo foi dividido por zero, e se foi mostra um erro
        print('Nenhuma das medidas colocadas podem ser menor ou igual a zero.')
  # verifica a opção escolhida pelo usuário.
  if choice == '1':
    c = input('Comprimento\n >  ')
    l = input('Largura\n >  ')
    med = input('Nome da medida\n >  ')
    CalcularArea(c, l, med)

if __name__ == '__main__':
  main()