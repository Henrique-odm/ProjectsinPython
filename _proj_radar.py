"""
variáveis reduzidas
"""

Velocidade = 75 #velocidade atual do carro
local_carro = 102 #local onde o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distância onde o radar pega

velocidade_radar_1 = Velocidade > RADAR_1
velocidade_radar_2 = Velocidade < RADAR_1
radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_radar_2:
    print("carro passou no radar") 

if radar and velocidade_radar_1:
    print("carro multado")