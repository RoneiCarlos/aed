#lista do odômetro em cada segmento da viagem
l_odometro = [22495, 22841, 23185, 23400, 23772, 24055, 24434, 24804, 25276]

#lista de consumo por segmento da viagem
l_consumo = [36.6, 33.9, 31.5, 33.0, 36.6, 44.1, 42.9, 45.6]

#lista de km por segmento de viagem
l_km_segmento = []

#lista do consumo por litro de cada segmento da viagem
l_km_por_l = []

#lista do consumo médio cumulativo da viagem
l_consumo_cumulativo = []

#calcula a quilometragem de cada segmento da viagem
for i in range(0,len(l_odometro)-1):
    km_segmento = l_odometro[(i+1)] - l_odometro[i]
    l_km_segmento.append(km_segmento)

#calcula o consumo por km de cada segmento
for i in range(0,len(l_km_segmento)):
    var = l_km_segmento[i]/l_consumo[i]
    l_km_por_l.append(round(var,2))

#calcula o cunsumo médio cumulativo
consumo_cumulativo = 0
odometro_cumulativo = 0
for i in range(0,len(l_km_segmento)):
    odometro_cumulativo += l_km_segmento[i]
    consumo_cumulativo += l_consumo[i]
    l_consumo_cumulativo.append(round(odometro_cumulativo/consumo_cumulativo,2))

#imprime na tela os resultados
print('quilômetro rodado por segmento da viagem:', l_km_segmento)
print('consumo de combustivel por segmento da viagem:', l_consumo)
print('consumo médio de combustível por litro de cada segmento da viagem:', l_km_por_l)
print('consumo médio cumulativo dos segmentos da viagem:', l_consumo_cumulativo)