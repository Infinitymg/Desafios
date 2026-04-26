from ex1 import numeros
from ex1 import frutas

print("\nOperações com listas:")
# Adicionar elemento
frutas.append("morango")
print("Após append:", frutas)
# Remover elemento
frutas.remove("banana")
print("Após remove:", frutas)

# Modificar elemento
frutas[1] = "kiwi"
print("Após modificação:", frutas)

# Concatenar listas
nova_lista = frutas + ["uva", "manga"]
print("Após concatenação:", nova_lista)
