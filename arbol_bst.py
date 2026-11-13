# arbol_bst.py
# Práctica: Actividades de Programación con Árboles Binarios
# Contiene toda la lógica (clases y funciones) de los 20 ejercicios.

from collections import deque


# =====================================================================
# 1. Nodo de árbol binario
# =====================================================================
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# =====================================================================
# Clase ArbolBST
# Cada método público llama a una función interna recursiva (_algo)
# que recibe el nodo actual. Así la recursión nunca "regresa" a la raíz.
# =====================================================================
class ArbolBST:
    def __init__(self):
        self.raiz = None

    # ============ PARTE I: FUNDAMENTOS ============

    # 2. Insertar respetando las reglas del BST (duplicados se ignoran)
    def insertar(self, valor):
        def _ins(n, v):
            if n is None:
                return Nodo(v)
            if v < n.valor:
                n.izquierdo = _ins(n.izquierdo, v)
            elif v > n.valor:
                n.derecho = _ins(n.derecho, v)
            return n
        self.raiz = _ins(self.raiz, valor)

    # 3. Recorridos
    def preorden(self):
        res = []
        def _pre(n):
            if n:
                res.append(n.valor)          # Raíz
                _pre(n.izquierdo)            # Izquierdo
                _pre(n.derecho)              # Derecho
        _pre(self.raiz)
        return res

    def inorden(self):
        res = []
        def _in(n):
            if n:
                _in(n.izquierdo)             # Izquierdo
                res.append(n.valor)          # Raíz
                _in(n.derecho)               # Derecho
        _in(self.raiz)
        return res

    def postorden(self):
        res = []
        def _post(n):
            if n:
                _post(n.izquierdo)           # Izquierdo
                _post(n.derecho)             # Derecho
                res.append(n.valor)          # Raíz
        _post(self.raiz)
        return res

    # 4. Buscar un valor
    def buscar(self, valor):
        n = self.raiz
        while n:
            if valor == n.valor:
                return True
            n = n.izquierdo if valor < n.valor else n.derecho
        return False

    # 5. Mínimo y máximo
    def minimo(self):
        if not self.raiz:
            return None
        n = self.raiz
        while n.izquierdo:
            n = n.izquierdo
        return n.valor

    def maximo(self):
        if not self.raiz:
            return None
        n = self.raiz
        while n.derecho:
            n = n.derecho
        return n.valor

    # 6. Altura (árbol vacío = 0, un solo nodo = 1)
    def altura(self):
        def _alt(n):
            if n is None:
                return 0
            return 1 + max(_alt(n.izquierdo), _alt(n.derecho))
        return _alt(self.raiz)

    # 7. Contar nodos
    def contar_nodos(self):
        def _cont(n):
            if n is None:
                return 0
            return 1 + _cont(n.izquierdo) + _cont(n.derecho)
        return _cont(self.raiz)

    # 8. Contar hojas
    def contar_hojas(self):
        def _hojas(n):
            if n is None:
                return 0
            if not n.izquierdo and not n.derecho:
                return 1
            return _hojas(n.izquierdo) + _hojas(n.derecho)
        return _hojas(self.raiz)

    # ============ PARTE II: MANIPULACIÓN INTERMEDIA ============

    # 9. Eliminar (sin hijos, un hijo, dos hijos)
    def eliminar(self, valor):
        def _min(n):
            while n.izquierdo:
                n = n.izquierdo
            return n

        def _del(n, v):
            if n is None:
                return None
            if v < n.valor:
                n.izquierdo = _del(n.izquierdo, v)
            elif v > n.valor:
                n.derecho = _del(n.derecho, v)
            else:
                if not n.izquierdo and not n.derecho:   # sin hijos
                    return None
                if not n.izquierdo:                     # solo hijo derecho
                    return n.derecho
                if not n.derecho:                       # solo hijo izquierdo
                    return n.izquierdo
                suc = _min(n.derecho)                   # dos hijos: sucesor inorden
                n.valor = suc.valor
                n.derecho = _del(n.derecho, suc.valor)
            return n
        self.raiz = _del(self.raiz, valor)

    # 10. Ver función suelta son_identicos() al final del archivo

    # 11. Convertir el árbol en su espejo
    def espejo(self):
        def _esp(n):
            if n is None:
                return
            n.izquierdo, n.derecho = n.derecho, n.izquierdo
            _esp(n.izquierdo)
            _esp(n.derecho)
        _esp(self.raiz)

    # 12. Recorrido por niveles (BFS)
    def por_niveles(self):
        if not self.raiz:
            return []
        res, cola = [], deque([self.raiz])
        while cola:
            nivel = []
            for _ in range(len(cola)):
                n = cola.popleft()
                nivel.append(n.valor)
                if n.izquierdo:
                    cola.append(n.izquierdo)
                if n.derecho:
                    cola.append(n.derecho)
            res.append(nivel)
        return res

    # 13. Nodos con exactamente un hijo
    def contar_un_hijo(self):
        def _uno(n):
            if n is None:
                return 0
            c = 1 if (n.izquierdo is None) != (n.derecho is None) else 0
            return c + _uno(n.izquierdo) + _uno(n.derecho)
        return _uno(self.raiz)

    # 14. Verificar si es un BST válido (cada nodo dentro de un rango)
    def es_bst_valido(self):
        def _val(n, mini, maxi):
            if n is None:
                return True
            if (mini is not None and n.valor <= mini) or \
               (maxi is not None and n.valor >= maxi):
                return False
            return _val(n.izquierdo, mini, n.valor) and _val(n.derecho, n.valor, maxi)
        return _val(self.raiz, None, None)

    # ============ PARTE III: APLICACIONES ============

    # 15. Suma de todos los nodos
    def suma(self):
        def _suma(n):
            if n is None:
                return 0
            return n.valor + _suma(n.izquierdo) + _suma(n.derecho)
        return _suma(self.raiz)

    # 16. Caminos de la raíz a las hojas
    def caminos_hoja(self):
        res = []
        def _dfs(n, camino):
            if n is None:
                return
            camino.append(n.valor)
            if not n.izquierdo and not n.derecho:
                res.append(camino[:])
            else:
                _dfs(n.izquierdo, camino)
                _dfs(n.derecho, camino)
            camino.pop()        # retroceso
        _dfs(self.raiz, [])
        return res

    # 17. Nivel (profundidad) de un nodo. Raíz = nivel 0; -1 si no existe
    def nivel_de(self, valor):
        def _niv(n, nivel):
            if n is None:
                return -1
            if n.valor == valor:
                return nivel
            izq = _niv(n.izquierdo, nivel + 1)
            if izq != -1:
                return izq
            return _niv(n.derecho, nivel + 1)
        return _niv(self.raiz, 0)

    # 18. Ver función suelta construir_desde_pre_in() al final del archivo

    # 19. Balancear el árbol a partir de su inorden
    def balancear(self):
        valores = self.inorden()
        def _build(lista):
            if not lista:
                return None
            m = len(lista) // 2
            n = Nodo(lista[m])
            n.izquierdo = _build(lista[:m])
            n.derecho = _build(lista[m + 1:])
            return n
        self.raiz = _build(valores)

    # ============ EXTRAS ============

    def copiar(self):
        """Devuelve un nuevo ArbolBST igual a este (para pruebas)."""
        def _cop(n):
            if n is None:
                return None
            nuevo = Nodo(n.valor)
            nuevo.izquierdo = _cop(n.izquierdo)
            nuevo.derecho = _cop(n.derecho)
            return nuevo
        otro = ArbolBST()
        otro.raiz = _cop(self.raiz)
        return otro

    def dibujar(self):
        def _dib(n, nivel, prefijo):
            if n is not None:
                print("    " * nivel + prefijo + str(n.valor))
                _dib(n.izquierdo, nivel + 1, "L--- ")
                _dib(n.derecho, nivel + 1, "R--- ")
        if self.raiz is None:
            print("(árbol vacío)")
        else:
            _dib(self.raiz, 0, "Raíz: ")


# =====================================================================
# Funciones sueltas
# =====================================================================

# 10. Verificar si dos árboles son idénticos (recibe las raíces)
def son_identicos(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.valor == b.valor and
            son_identicos(a.izquierdo, b.izquierdo) and
            son_identicos(a.derecho, b.derecho))


# 18. Construir un árbol a partir de preorden e inorden
#     El primer valor del preorden es la raíz; en el inorden, lo que está
#     a su izquierda es el subárbol izquierdo y lo de la derecha, el derecho.
def construir_desde_pre_in(preorden, inorden):
    if not preorden or not inorden:
        return None
    raiz = Nodo(preorden[0])
    idx = inorden.index(preorden[0])
    raiz.izquierdo = construir_desde_pre_in(preorden[1:idx + 1], inorden[:idx])
    raiz.derecho = construir_desde_pre_in(preorden[idx + 1:], inorden[idx + 1:])
    return raiz


# =====================================================================
# 20. Menú jerárquico con árbol binario
#     Representación "hijo izquierdo - hermano derecho":
#       izquierdo -> primera subopción
#       derecho   -> siguiente opción del mismo nivel
# =====================================================================
class OpcionMenu(Nodo):
    def agregar_subopcion(self, titulo):
        nueva = OpcionMenu(titulo)
        if self.izquierdo is None:
            self.izquierdo = nueva
        else:
            n = self.izquierdo
            while n.derecho:
                n = n.derecho
            n.derecho = nueva
        return nueva

    def subopciones(self):
        lista, n = [], self.izquierdo
        while n:
            lista.append(n)
            n = n.derecho
        return lista


def crear_menu_ejemplo():
    menu = OpcionMenu("Menú principal")

    archivo = menu.agregar_subopcion("Archivo")
    archivo.agregar_subopcion("Nuevo")
    archivo.agregar_subopcion("Abrir")
    guardar = archivo.agregar_subopcion("Guardar")
    guardar.agregar_subopcion("Guardar")
    guardar.agregar_subopcion("Guardar como...")
    archivo.agregar_subopcion("Salir")

    editar = menu.agregar_subopcion("Editar")
    editar.agregar_subopcion("Copiar")
    editar.agregar_subopcion("Pegar")
    editar.agregar_subopcion("Deshacer")

    ayuda = menu.agregar_subopcion("Ayuda")
    ayuda.agregar_subopcion("Manual de usuario")
    ayuda.agregar_subopcion("Acerca de")
    return menu


def mostrar_menu(opcion, sangria=0):
    print("    " * sangria + "- " + opcion.valor)
    for sub in opcion.subopciones():
        mostrar_menu(sub, sangria + 1)


def navegar_menu(menu):
    pila = [menu]       # camino recorrido, para poder regresar
    while True:
        actual = pila[-1]
        subs = actual.subopciones()
        print(f"\n=== {actual.valor} ===")
        for i, sub in enumerate(subs, start=1):
            print(f"  {i}. {sub.valor}")
        print("  0. Regresar" if len(pila) > 1 else "  0. Salir del menú")

        op = input("Elija una opción: ").strip()
        if not op.isdigit() or int(op) > len(subs):
            print("Opción no válida.")
            continue
        op = int(op)
        if op == 0:
            if len(pila) == 1:
                print("Saliendo del menú...")
                return
            pila.pop()
        else:
            elegida = subs[op - 1]
            if elegida.izquierdo is None:
                print(f">> Ejecutando: {elegida.valor}")
            else:
                pila.append(elegida)