area_terreno = 1500
ca = 2
area_computavel = area_terreno * ca
areas_adicionais = area_computavel * 0.15
area_privativa = areas_adicionais + area_computavel
eficiencia = 0.6
area_construida = area_privativa / eficiencia
area_construida

def calculo_area_construida(area_terreno, ca):
  area_computavel = area_terreno * ca
  areas_adicionais = area_computavel * 0.15
  area_privativa = area_adicionais + area_computavel
  eficiencia = 0.6
  area_construida = area_privativa / eficiencia
  return area_construida

calculo_area_construida(1200, 3)

