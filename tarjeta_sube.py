import unittest

class NoHaySaldoException (Exception):
    pass
class UsuarioDesactivadoException (Exception):
    pass
class EstadoNoExistenteException (Exception):
    pass

PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"

Descuentos = {
    PRIMARIO:50,
    SECUNDARIO:30,
    UNIVERSITARIO:20,
}
PRECIO_TICKET = 70
DESACTIVADO = "desactivadp"
ACTIVADO = "activado"

class Sube():
    def __init__ (self):
        self.saldo = None
        self.estado = ACTIVADO
        self.grupo_beneficiario = None
    
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario:
            precio_ticket = PRECIO_TICKET - ((Descuentos[self.grupo_beneficiario]/100))*PRECIO_TICKET
            return precio_ticket
        else:
            precio_ticket = PRECIO_TICKET
        return precio_ticket


    def pagar_pasaje(self):
        precio = self.obtener_precio_ticket() #Los otros metodos se llaman con self
        if self.saldo < precio:
            raise NoHaySaldoException()
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        else: 
            self.saldo -= precio
    
    def cambiar_estado(self, estado):
        if estado == DESACTIVADO:
            self.estado = DESACTIVADO
        elif estado == ACTIVADO:
            self.estado = ACTIVADO
        else:
            raise EstadoNoExistenteException()



    
    
    




if __name__ == "__main__":
    unittest.main()