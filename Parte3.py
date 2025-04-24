import random

def simular_test(n_simulaciones=1_000_000):
    positivos_totales = 0           # Casos de test positivos
    positivos_con_enfermedad = 0    # Casos de test positivos que efectivamente tienen la enfermedad

    for _ in range(n_simulaciones):
        # Determinar si la persona tiene la enfermedad
        tiene_enfermedad = random.random() < 0.0001

        if tiene_enfermedad:
            # Si la tiene, 99% de dar positivo
            test_positivo = random.random() > 0.01  # 1% de falso negativo
        else:
            # Si NO la tiene, 2% de dar falso positivo
            test_positivo = random.random() < 0.02

        # Si el test es positivo, aumenta el contador de casos de tests positivos
        # Si ademas tiene la enfermedad, aumenta el otro contador.
        if test_positivo:
            positivos_totales += 1
            if tiene_enfermedad:
                positivos_con_enfermedad += 1

    if positivos_totales == 0:
        return 0
    else:
        return positivos_con_enfermedad / positivos_totales # Calculo de la probabilidad

# Ejecutar simulación
resultado_estimado = simular_test()
#  Resultado con 5 decimales
print(f"Probabilidad estimada de tener la enfermedad dado que el test dio positivo: {resultado_estimado:.5f}") 