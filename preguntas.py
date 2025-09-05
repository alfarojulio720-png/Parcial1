# ------------------------------
# Clase Producto
# ------------------------------
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

# ------------------------------
# Clase Venta
# ------------------------------
class Venta:
    def __init__(self):
        self.items = []  # lista de tuplas: (producto, cantidad)

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.items)

# ------------------------------
# Clase ControlVentas
# ------------------------------
class ControlVentas:
    def __init__(self):
        self.ventas = []
        self.productos_vendidos = {}  # nombre_producto: [cantidad_total, ingresos_totales]

    def registrar_venta(self, venta):
        self.ventas.append(venta)
        for producto, cantidad in venta.items:
            if producto.nombre not in self.productos_vendidos:
                self.productos_vendidos[producto.nombre] = [0, 0.0]
            self.productos_vendidos[producto.nombre][0] += cantidad
            self.productos_vendidos[producto.nombre][1] += producto.precio * cantidad

    def ingresos_totales(self):
        return sum(venta.calcular_total() for venta in self.ventas)

    def generar_reporte(self, ordenar_por="ingresos"):
        print("\n📊 REPORTE DE VENTAS 📊")
        print(f"{'Producto':<15}{'Cantidad':<10}{'Ingresos ($)':<12}")
        print("-" * 37)
        datos = self.productos_vendidos.items()

        if ordenar_por == "ingresos":
            datos = sorted(datos, key=lambda x: x[1][1], reverse=True)
        elif ordenar_por == "cantidad":
            datos = sorted(datos, key=lambda x: x[1][0], reverse=True)

        for nombre, (cantidad, ingresos) in datos:
            print(f"{nombre:<15}{cantidad:<10}{ingresos:<12.2f}")

        print(f"\n💰 Ingresos totales: ${self.ingresos_totales():.2f}")

# ------------------------------
# Ejemplo de uso del sistema
# ------------------------------
def main():
    # Crear productos
    arroz = Producto("Arroz", 1.25, "Granos")
    frijol = Producto("Frijol", 1.10, "Granos")
    leche = Producto("Leche", 0.95, "Lácteos")
    huevo = Producto("Huevo", 0.20, "Proteína")

    # Crear el sistema de control de ventas
    sistema = ControlVentas()

    # Registrar una venta 1
    venta1 = Venta()
    venta1.agregar_producto(arroz, 5)
    venta1.agregar_producto(frijol, 3)
    sistema.registrar_venta(venta1)

    # Registrar una venta 2
    venta2 = Venta()
    venta2.agregar_producto(leche, 10)
    venta2.agregar_producto(huevo, 12)
    sistema.registrar_venta(venta2)

    # Registrar una venta 3
    venta3 = Venta()
    venta3.agregar_producto(arroz, 2)
    venta3.agregar_producto(leche, 5)
    sistema.registrar_venta(venta3)

    # Generar reportes
    sistema.generar_reporte(ordenar_por="ingresos")  # o "cantidad"

if __name__ == "__main__":
    main()



git config --global user.name "alfarojulio720"

git config --global user.email "alfarojulio720@gmail.com"
