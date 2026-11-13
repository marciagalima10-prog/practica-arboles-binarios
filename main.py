# main.py
# Pruebas y ejemplos de las 20 actividades.

from arbol_bst import (ArbolBST, Nodo, son_identicos, construir_desde_pre_in,
                       crear_menu_ejemplo, mostrar_menu, navegar_menu)


def titulo(texto):
    print("\n" + "=" * 55)
    print(texto)
    print("=" * 55)


# ---------------- PARTE I ----------------
titulo("PARTE I: FUNDAMENTOS")

arbol = ArbolBST()
for v in [50, 30, 70, 20, 40, 60, 80, 35, 65]:      # 1 y 2
    arbol.insertar(v)

print("Dibujo del árbol:")
arbol.dibujar()
print()
print("3. Preorden :", arbol.preorden())
print("   Inorden  :", arbol.inorden())
print("   Postorden:", arbol.postorden())
print("4. Buscar 40:", arbol.buscar(40), "| Buscar 99:", arbol.buscar(99))
print("5. Mín/Máx  :", arbol.minimo(), "/", arbol.maximo())
print("6. Altura   :", arbol.altura())
print("7. Nodos    :", arbol.contar_nodos())
print("8. Hojas    :", arbol.contar_hojas())

# ---------------- PARTE II ----------------
titulo("PARTE II: MANIPULACIÓN INTERMEDIA")

prueba = arbol.copiar()
prueba.eliminar(20)
print("9. Eliminar 20 (sin hijos)   :", prueba.inorden())
prueba.eliminar(40)
print("   Eliminar 40 (un hijo)     :", prueba.inorden())
prueba.eliminar(50)
print("   Eliminar 50 (dos hijos)   :", prueba.inorden(), "-> nueva raíz:", prueba.raiz.valor)

copia = arbol.copiar()
print("\n10. ¿Árbol y su copia idénticos?      ", son_identicos(arbol.raiz, copia.raiz))
print("    ¿Árbol y el de eliminaciones?      ", son_identicos(arbol.raiz, prueba.raiz))

reflejo = arbol.copiar()
reflejo.espejo()
print("\n11. Espejo del árbol:")
reflejo.dibujar()

print("\n12. Por niveles (BFS):")
for i, nivel in enumerate(arbol.por_niveles()):
    print(f"    Nivel {i}: {nivel}")

print("\n13. Nodos con un solo hijo:", arbol.contar_un_hijo())

print("\n14. ¿Árbol original es BST válido?", arbol.es_bst_valido())
print("    ¿El espejo es BST válido?      ", reflejo.es_bst_valido())
trampa = ArbolBST()                       # 60 a la izquierda de 50: inválido
trampa.raiz = Nodo(50)
trampa.raiz.izquierdo = Nodo(30)
trampa.raiz.izquierdo.derecho = Nodo(60)
print("    ¿Árbol trampa es BST válido?   ", trampa.es_bst_valido())

# ---------------- PARTE III ----------------
titulo("PARTE III: APLICACIONES")

print("15. Suma de los nodos:", arbol.suma())

print("\n16. Caminos raíz -> hojas:")
for camino in arbol.caminos_hoja():
    print("    " + " -> ".join(map(str, camino)))

print("\n17. Nivel del 50:", arbol.nivel_de(50), "| del 40:", arbol.nivel_de(40),
      "| del 65:", arbol.nivel_de(65), "| del 99:", arbol.nivel_de(99))

pre, ino = arbol.preorden(), arbol.inorden()
reconstruido = construir_desde_pre_in(pre, ino)
print("\n18. Reconstruir desde preorden e inorden")
print("    ¿Idéntico al original?", son_identicos(arbol.raiz, reconstruido))

torcido = ArbolBST()
for v in range(1, 8):                     # insertar en orden lo desbalancea
    torcido.insertar(v)
print("\n19. Árbol desbalanceado (altura", torcido.altura(), "):")
torcido.dibujar()
torcido.balancear()
print("    Árbol balanceado (altura", torcido.altura(), "):")
torcido.dibujar()

print("\n20. Menú jerárquico:")
menu = crear_menu_ejemplo()
mostrar_menu(menu)
if input("\n¿Desea navegar el menú? (s/n): ").strip().lower() == "s":
    navegar_menu(menu)

print("\nFin de la práctica.")