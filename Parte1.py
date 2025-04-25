import random


def monty_hall(cambiaPuerta, mostrar_detalles=False):
    puertaCorrecta = random.randint(1,3)
    puertaElegida = random.randint(1,3)

    puertaParaAbrir = [1,2,3]
    puertaParaAbrir.remove(puertaCorrecta)
    if puertaElegida != puertaCorrecta:
        puertaParaAbrir.remove(puertaElegida)
    
    puertaAbierta = random.choice(puertaParaAbrir)

    if cambiaPuerta:
        puertaSegundaElegida = [1,2,3]
        puertaSegundaElegida.remove(puertaAbierta)
        puertaSegundaElegida.remove(puertaElegida)
        puertaElegida = puertaSegundaElegida[0]

    #Al hacer muchas simulaciones puede ser poco eficiente mostrar los detalles de cada simulación
    if mostrar_detalles:
        print(f"La puerta correcta es {puertaCorrecta}, la puerta elegida es {puertaElegida} y la puerta abierta es {puertaAbierta}")
        if cambiaPuerta:
            print("Cambio de puerta")
            print("Nueva puerta elegida: ", puertaElegida)
        else:
            print("No cambio de puerta")
        if puertaElegida == puertaCorrecta:
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

    return puertaElegida == puertaCorrecta


def simularMontyHall(num_simulaciones, mostrar_detalles=False):
    victorias_cambio = 0
    victorias_no_cambio = 0
    
    if mostrar_detalles:
        print(f"\nSimulando {num_simulaciones} veces:")
        print("-" * 50)
    
    for i in range(num_simulaciones):
        if monty_hall(True, mostrar_detalles):
            victorias_cambio += 1
        if monty_hall(False, mostrar_detalles):
            victorias_no_cambio += 1
    
    prob_cambio = victorias_cambio / num_simulaciones
    prob_no_cambio = victorias_no_cambio / num_simulaciones
    
    if mostrar_detalles:
        print("\nResultados finales:")
        print(f"Con cambio de puerta: {victorias_cambio} victorias de {num_simulaciones} intentos")
        print(f"Probabilidad con cambio: {prob_cambio:.4f} ({prob_cambio*100:.2f}%)")
        print(f"Sin cambio de puerta: {victorias_no_cambio} victorias de {num_simulaciones} intentos")
        print(f"Probabilidad sin cambio: {prob_no_cambio:.4f} ({prob_no_cambio*100:.2f}%)")
    
    return prob_cambio, prob_no_cambio


if __name__ == "__main__":
    
    #print("\nPrueba con 10 simulaciones (mostrando detalles):")
    #simularMontyHall(10, mostrar_detalles=True)
    
    # Simulaciones
    print("\nSimulación con 1,000 intentos:")
    prob_cambio, prob_no_cambio = simularMontyHall(1000)
    print(f"Probabilidad con cambio: ({prob_cambio*100:.2f}%)")
    print(f"Probabilidad sin cambio: ({prob_no_cambio*100:.2f}%)")
    
    print("\nSimulación con 10,000 intentos:")
    prob_cambio, prob_no_cambio = simularMontyHall(10000)
    print(f"Probabilidad con cambio: ({prob_cambio*100:.2f}%)")
    print(f"Probabilidad sin cambio: ({prob_no_cambio*100:.2f}%)")
    
    print("\nSimulación con 100,000 intentos:")
    prob_cambio, prob_no_cambio = simularMontyHall(100000)
    print(f"Probabilidad con cambio: ({prob_cambio*100:.2f}%)")
    print(f"Probabilidad sin cambio: ({prob_no_cambio*100:.2f}%)")


























