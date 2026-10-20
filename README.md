Servicio de Internet — NUMERO 36 VALDIVIA

Reto individual

Consultar el frente de la cola sin modificarla.

Código base

Se conserva la estructura y los nombres de las clases del código inicial (Nodo, ListaEnlazada, Pila y Cola). Se completan los cinco TODO y se añade el método consultar_frente() a la clase Cola.

Datos de prueba

DATO 1: Sin señal
DATO 2: Lentitud
DATO 3: Router

Ejecutar

En una terminal, dentro de la carpeta donde está main.py, ejecuta:

python main.py

Método del reto

consultar_frente() devuelve self.items[0] sin usar pop(0), por lo que consulta el primer elemento de la cola sin retirarlo ni modificar su orden. Si la cola está vacía, devuelve None.
