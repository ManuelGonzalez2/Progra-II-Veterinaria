# src/clases.py
# Este fichero conendra las diferentes clases para el proyecto

# Importamos 'date' para manejar la fecha de nacimiento
from datetime import date 

class Cliente:
    # Un cliente tiene nombre, teléfono y correo
    def __init__(self, nombre: str, telefono: str, email: str):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.mascotas = [] # Creamos una lista para guardar las masotas de cada cliente

    def __str__(self):
        return f"Cliente: {self.nombre} , con mail ({self.email})"

class Mascota:
    # Una mascota tiene especie, raza y fecha de nacimiento 
    def __init__(self, nombre: str, especie: str, raza: str, fecha_nacimiento: date):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        # Creamos un historial medico de cad mascota donde se recogeran diferetes atributos
        self.historial_medico = {
            "vacunas": [],
            "peso": [],
            "observaciones": [],
            "tratamientos": []
        }

    def __str__(self):
        return f"Mascota: {self.nombre} (Especie: {self.especie})"

class Cita:
    # Una cita tiene fecha, hora, motivo y veterinario
    def __init__(self, fecha: date, hora: str, motivo: str, veterinario: str, mascota: Mascota):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.veterinario = veterinario
        self.mascota = mascota

    def __str__(self):
        return f"Usted tiene cita el {self.fecha} a las {self.hora} para {self.mascota.nombre}"


class Veterinaria:
    # Esta clase gestionará toda la lógica del negocio
    def __init__(self):
        self.clientes = [] # Una lista para guardar todos los clientes
        self.citas = []    # Una lista para guardar todas las citas

    # Funciones de Clientes 
    
    #Registrar al cliente
    def registrar_cliente(self, nombre, telefono, email):
        cliente_nuevo = Cliente(nombre, telefono, email)
        self.clientes.append(cliente_nuevo)
        print(f"Cliente '{nombre}' registrado con éxito.") # [cite: 24]
        return cliente_nuevo

    # Buscar un cliente 
    def buscar_cliente(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente 
        return None 

    #Elimnar clientes
    def eliminar_cliente(self, email):
        cliente_a_eliminar = self.buscar_cliente(email)
        
        if cliente_a_eliminar:
            self.clientes.remove(cliente_a_eliminar)
            print(f"El cliente '{cliente_a_eliminar.nombre}' se ha eeliminado con éxito.")
            return True
        else:
            print(f"Error: No se encontró ningun cliente con el email {email}.")
            return False

    #Funciones de Mascotas

    # Función designada a registrar una mascota
    def registrar_mascota(self, email_cliente, nombre_mascota, especie, raza, fecha_nacimiento):
        # Primero tenemos que encontrar a quien es el dueño de la mascota
        cliente = self.buscar_cliente(email_cliente)
        
        if cliente:
            mascota_nueva = Mascota(nombre_mascota, especie, raza, fecha_nacimiento)
            # Ahora tenemos que asignar la mascota a la lista de su dueño.
            cliente.mascotas.append(mascota_nueva)
            print(f"La mascota '{nombre_mascota}' ha sido registrada para el cliente {cliente.nombre}.")
            return mascota_nueva
        else:
            print(f"Error: No se pudo registrar la mascota. El cliente {email_cliente} no ha sido encontrado.")
            return None
    
    # Funciones de Citas 

    #Funcion designada pra crear la cita
    def crear_cita(self, fecha, hora, motivo, veterinario, mascota):
        nueva_cita = Cita(fecha, hora, motivo, veterinario, mascota)
        self.citas.append(nueva_cita)
        print(f"Cita creada para {mascota.nombre} el {fecha} a las {hora}.")
        return nueva_cita

    #Funcion designada a buscar tu cita
    def buscar_citas_por_fecha(self, fecha):
        citas_encontradas = []
        for cita in self.citas:
            if cita.fecha == fecha:
                citas_encontradas.append(cita)
        return citas_encontradas

    #Creamos otra funcion para modificar la cita
    def modificar_cita(self, id_cita, nuevo_motivo, nueva_hora):
        for cita in self.citas:
            if cita.id_cita == id_cita:
                cita.motivo = nuevo_motivo
                cita.hora = nueva_hora
                print(f"Cita {id_cita} modificada.")
                return True
        print(f"Error: Cita {id_cita} no encontrada.")
        return False

    #Funcion para eliminar una cita
    def eliminar_cita(self, id_cita):
        cita_a_eliminar = None
        for cita in self.citas:
            if cita.id_cita == id_cita:
                cita_a_eliminar = cita
                break
        
        if cita_a_eliminar:
            self.citas.remove(cita_a_eliminar)
            print(f"Cita {id_cita} eliminada.")
            return True
        else:
            print(f"Error: Cita {id_cita} no encontrada.")
            return False

    #Funciones de Historial Médico

    #Funcion para añadir vacuna
    def anadir_vacuna(self, mascota, nombre_vacuna, fecha):
        registro = f"Vacuna: {nombre_vacuna}, Fecha: {fecha}"
        mascota.historial_medico["vacunas"].append(registro)
        print(f"Vacuna añadida al historial de {mascota.nombre}.")

    #Funcion para añadir el peso de la mascota
    def anadir_peso(self, mascota: Mascota, peso_kg: float, fecha: date):
        registro = {"fecha": fecha, "peso": peso_kg}
        mascota.historial_medico["peso"].append(registro)
        print(f"Peso ({peso_kg}kg) añadido al historial de {mascota.nombre}.")

    #Funcion para añadir las observaciones del doctor
    def anadir_observacion(self, mascota: Mascota, observacion: str, fecha: date):
        registro = f"Fecha: {fecha} - Observación: {observacion}"
        mascota.historial_medico["observaciones"].append(registro)
        print(f"Observación añadida al historial de {mascota.nombre}.")

    #Funcion para añadir el tratamiento al que se va a someter
    def anadir_tratamiento(self, mascota: Mascota, tratamiento: str, fecha_inicio: date):
        registro = f"Tratamiento: {tratamiento}, Inicio: {fecha_inicio}"
        mascota.historial_medico["tratamientos"].append(registro)
        print(f"Tratamiento añadido al historial de {mascota.nombre}.")
