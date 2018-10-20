# Entregable Tarea 03 
Vicente Guedelhoefer Sección 1

Para el cálculo de la demanda de la red, se calculará primero la demanda de las casas, en particular con las casas colgadas. El algoritmo va a partir recorriendo todos los nodos de la red que no tengan ningún nodo hijo y que sean casas. Para identificar las casas que no son padres de nadie, se va a recorrer la base de datos y se van a filtrar todos los id que no estén en casas_desde de casas. Cada nodo tendrá atributos que hacen referencia a sus nodos padres e hijos, a su demanda propia y a la clase de instalación que es. 

```python
class Nodo:

    def __init__(self, id, tipo, demanda_propia):
        self.id = id
        self.tipo = tipo
        self.demanda_propia = dp
        self.hijos = ListaMia()
        self.padres = ListaMia()
        self.demanda_calculada = None

```

Para el caso de las casas colgadas, simplemente se va a sumar su demanda a una variable global que mida la demanda y luego self.demanda_calculada = demanda_propia en ese caso. Luego de realizar esto para todas las casas sin hijos, subimos al nivel de las casas no colgadas (a través de la lista padres) y revisamos si estas están colgadas a otras casas o a una central distribuidora. Luego, revisamos los hijos de estas instalaciones entrando a la lista hijos (desde el nodo padre) y para cada hijo dentro de esa lista obtenemos:
**len(lista_padres)** , **demanda_calculada** y **id**. 
Con estos datos procedemos a calcular la demanda de ese nodo de la forma:

    P_padre = d_propia + Sum{P_hijo / len(lista_padre_hijo) / 1- (p * L_padre,hijo / S) , para cada hijo} 

Es importante destacar que la variable L_padre,hijo se obtiene usando los id de ambos buscando en la base de datos acorde al tipo de cada instalación. Este proceso se puede generalizar para los casos de las entidades de distribución, transmisión y elevadoras. En esos casos no la formulación cambia un poco ya que no necesitamos el largo de la lista de padres que tiene cada hijo (ya que sabemos que para estas entidades solo existe un padre). Por lo tanto, tenemos que el algoritmo generalizado sería: 

1. ```Obtener P_i de casas mediante lo anterior```
2. ```Subir a los padres de instancias (primer paso es de casas) ```
3. ```Obtener desde el nodo padre: id_hijo y P_i de cada hijo```
4. ```Usar id_hijo para obtener los largos Lpadre, hijo```
5. ```Computar P_padre mediante P_padre = d_propia + Sum{P_hijo / 1- (p * L_padre,hijo / S) , para cada hijo en lista de hijos}```
6. ```Sumar a variable de demanda global P_padre```
7. ```Volver a 1```

Para recorrer el grafo asociado al problema se implementará un algoritmo estilo BFS con algunas modificaciones, ya que con esto puedo obtener las demandas nivel a nivel en base a los datos recolectados. Esto funciona ya que se recorre el grafo por nivel y se van usando los datos obtenidos desde el nivel anterior para obtener una demanda total.
