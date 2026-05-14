"""
Exponenciacion binaria:

¿Cómo calcular a^n eficientemente para n muy grande?

Nótese que nos ahorramos casi la mitad de las multiplicaciones en cada paso recursivo,
ya que en lugar de multiplicar por a n/2 veces simplemente ponemos el resultado en una
variable y la multiplicamos una vez por sí misma.

"""

def potencia(a, b):
	if b == 0:
		return 1
	
	s = potencia(a, b//2)
	
	if b % 2 == 0: 
		return s*s
	else: 
		return s * s * a

