class Empleado:
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.direccion=direccion
        self.antiguedad=antiguedad
        self.telefono=telefono
        self.salario=salario
    def imprimir(self):
        print("Nombre: ", self.nombre , " Apellido: " , self.apellido , " DNI: " , self.dni ,
              " Dirección: " , self.direccion , " Antigüedad: " , self.antiguedad ,
              "Telefono: " , self.telefono , "Salario: " , self.salario)
    def cambiarSupervisor(self, supervisor):
        self.supervisor=supervisor
        print("El nuevo supervisor es: ", supervisor)
    def incrementarSalario(self, incremento):
        self.salario= (self.salario * incremento)/100 + self.salario
        print("El salario incrementado es: ", self.salario)
empleado1=Empleado("Jorge","Bermudez","99999999R","Calle periodista",1,645893081,2000)
empleado2=Empleado("Ana","Lopez","23893409E","Calle Mesones",2,576091234,1500)
empleado1.imprimir()
empleado1.incrementarSalario(2)
print("FIN")

class Secretario(Empleado):
    def __init__(self,nombre, apellido, dni, direccion, antiguedad, telefono, salario, fax, despacho, puesto):
        Empleado.__init__(self,nombre, apellido, dni, direccion, antiguedad, telefono, salario)
        self.fax=fax
        self.despacho=despacho
        self.puesto=puesto

    def incrementarSalario(self):
        super(Secretario, self).incrementarSalario(5)

    def imprimir(self):
        super(Secretario, self).imprimir()
        print("Puesto: " + str(self.puesto))
secretario1=Secretario("Jose","Martinez","09234573Z","Calle colera",2,61295815,3000, "7834567213","D1","Secretario")
secretario2=Secretario("Lucia","Romeroo","23869023U","Calle colera",3,683457612,3500, "1029856385","D2","Secretario")
secretario1.imprimir()
secretario2.imprimir()
print(
    "El fax del secretario ", secretario1.nombre, " es: ", secretario1.fax,
    "El despacho de secretario ", secretario1.nombre, " es el: ", secretario1.despacho,
    "Su puesto en la empresa es ", secretario1.puesto)
print(
    "El fax del secretario ", secretario2.nombre, " es: ", secretario2.fax,
    "El despacho de secretario ", secretario2.nombre, " es el: ", secretario2.despacho,
    "Su puesto en la empresa es ", secretario2.puesto)
secretario1.incrementarSalario()
secretario2.incrementarSalario()

print("FIN")

class Coche:
    def __init__(self,matricula, marca, modelo):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
coche1 = Coche("26894YTR","Mercedes","Benz")
coche2 = Coche("28945WRT","Audi","R8")
coche3 = Coche("28945WRT","Audi","R8")

listaClientes = ["Pepe","Luis","Jorge"]
class Vendedor(Empleado):
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario, coche2, area, comision, listaClientes ):
        Empleado.__init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario)
        self.coche = coche2
        self.area=area
        self.comision=comision
        self.listaClientes=listaClientes
    def alta(self, nombre):
        self.listaClientes.append(nombre)
    def baja(self, nombre):
        self.listaClientes.remove(nombre)
    def cambiarCoche(self, coche):
        self.coche=coche
        print("El nuevo coche es: ", coche.marca)
    def incrementarSalario(self):
        super(Vendedor, self).incrementarSalario(10)

listaVendedores=["Ramon","Alex","Manolo"]
vendedor1=Vendedor("Bryan","Cervilla","47593894B","Calle Don",4,247898904,2000, coche1, "Ventas", 4, listaClientes)
vendedor1.imprimir()
print(
    "Marcar de coche: ", vendedor1.coche.marca,
    "Area de trabajo: ", vendedor1.area,
    "Comisión: ", vendedor1.comision,
    "Lista de clientes: ", vendedor1.listaClientes)
vendedor1.incrementarSalario()
print("FIN")


class Jefe(Empleado):
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario, secretario1, coche3, despacho, listaVendedores ):
        Empleado.__init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario)
        self.secretario=secretario1
        self.coche=coche3
        self.despacho=despacho
        self.listaVendedores=listaVendedores
    def incrementarSalario(self):
        super(Jefe, self).incrementarSalario(20)
    def cambiarSecretario(self, secretario):
        self.secretario=secretario
        print("El nuevo secretario es: ", secretario.nombre)
    def cambiarCoche(self, coche):
        self.coche=coche
        print("El nuevo coche es: ", coche.marca)
    def altaVendedor(self, nombre):
        self.listaVendedores.append(nombre)
    def bajaVendedor(self, nombre):
        self.listaVendedores.remove(nombre)

jefe1=Jefe("Juan","Ordoñez","59358702F","Calle Granada",3,349093748,4000,secretario1,coche2,"Direccion",listaVendedores)
jefe1.imprimir()
print(
    "Secretario: ", jefe1.secretario.nombre,
    "Marca coche: ", jefe1.coche.marca,
    "Despacho: ", jefe1.despacho,
    "Lista de vendedores: ", jefe1.listaVendedores)
jefe1.incrementarSalario()
print("FIN")
