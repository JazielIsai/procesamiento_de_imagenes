# procesamiento_de_imagenes
Operaciones Puntuales sobre imágenes

1.- Operador identidad
la entrada es igual a la salida: P = Q

2.- Operador inverso o negativo
la salida es igual a a la entrada: Q = P EJEMPLO: Q = 255 - P  = 0

3.- Operador Umbral
     q = 0 para p <= p,
     q = 255 para p > p

4.- Operador intervalo de umbral binario
    p1, p2 
    
    q =  255 para p <= p1, ó p >= p2
    q =  0 para p1 < p < p2 

5.- Operador intervalo umbral binario invertido

    q =  0 para p <= p1, ó p >= p2
    q =  255 para p1, < p < p2 

6.- Operador umbral de la escala grises
   
    q = 255 para p <= p1 ó p >= p2
    q = p para p1 < p < p2

7.- Operador umbral de la escala grises
   
    q = 255 para p <= p1 ó p >= p2
    q = p para p1 < p < p2

8.- Operar umbral escala grises invertidos

    q = 255 para p <= p1 ó p >= p2
    q = 255 - p para p1 < p < p2

9.- Operador extensión 

    q  = 0  para p <= p1 ó p >= p2
    (p - p1) 255 / p2 - p1 para p1 < p < p2

10.- Operador reducción nivel gris
    
    q = 0 para p <= p1
    -q1 = para p1 < p <= p2
    q2 = para p2 < p <= p3
    .
    .
    qn para pn-1 < p <= 255

=
