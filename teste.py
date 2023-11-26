import machine
import time

pin = machine.Pin(5, machine.Pin.IN)

def callback(p):
    print("Pino acionado")
    time.sleep(2)
    
    
pin.irq(trigger=machine.Pin.IRQ_RISING
             | machine.Pin.IRQ_FALLING, handler=callback)


# while True:
#     # Lê o estado do pino
#     pin_value = pin.value()
#     
#     # Imprime o estado do pino
#     print("O valor do pino D1 é:", pin_value)
#     
#     # Aguarda um segundo antes de ler o estado do pino novamente
#     time.sleep(1)