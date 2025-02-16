    # Autor: EDSON JÚNIOR FROTA SILVA
    # DATA: 16/02/2025

import asyncio
import time

# Função assíncrona que simula uma chamada de rede
async def simular_chamada_rede(segundos):
    print(f"Iniciando chamada de rede que levará {segundos} segundos...")
    await asyncio.sleep(segundos)  # Simula uma operação que leva tempo
    print(f"Chamada de rede de {segundos} segundos concluída!")

# Função assíncrona principal que executa as três chamadas
async def main():
    # Inicia o cronômetro
    inicio = time.time()
    
    # Executa as três chamadas de rede de forma assíncrona
    await asyncio.gather(
        simular_chamada_rede(2),  # Chamada 1: 2 segundos
        simular_chamada_rede(3),  # Chamada 2: 3 segundos
        simular_chamada_rede(1)   # Chamada 3: 1 segundo
    )
    
    # Calcula o tempo total de execução
    tempo_total = time.time() - inicio
    print(f"Tempo total de execução: {tempo_total:.2f} segundos")

# Roda a função assíncrona principal
if __name__ == '__main__':
    asyncio.run(main())