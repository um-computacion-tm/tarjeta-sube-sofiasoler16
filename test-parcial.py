import unittest

from tarjeta_sube import (
    NoHaySaldoException, 
    PRIMARIO, #constantes
    UNIVERSITARIO,
    SECUNDARIO,
    PRECIO_TICKET,
    Sube, #es una clase
    UsuarioDesactivadoException,
    DESACTIVADO, #constantes
    ACTIVADO,
    EstadoNoExistenteException
)


class TestSube(unittest.TestCase):
    def setUp(self): #En todos los test se reinicia a estos valores
        self.sube = Sube()
        self.sube.saldo = 1000 #saldo instancia de sube

    def test_init(self):
        self.assertEqual(self.sube.saldo, 1000)
        self.assertEqual(self.sube.grupo_beneficiario, None)
        self.assertEqual(self.sube.estado, ACTIVADO)

    def test_obtener_precio_ticket(self):
        precio_ticket = self.sube.obtener_precio_ticket()
    
        self.assertEqual(precio_ticket, PRECIO_TICKET)
 
    def test_obtener_precio_ticket_con_grupo_beneficiario_PRIMARIO(self): #agregar descuento de grupo beneficiario
        sube = Sube()
        sube.saldo = 1000
        sube.grupo_beneficiario = PRIMARIO

        precio_ticket = sube.obtener_precio_ticket()
        
        self.assertEqual(precio_ticket, 35)
    
    def test_obtener_precio_ticket_con_grupo_beneficiario_UNIVERSITARIO(self): #agregar descuento de grupo beneficiario
        sube = Sube()
        sube.saldo = 1000
        sube.grupo_beneficiario = UNIVERSITARIO

        precio_ticket = sube.obtener_precio_ticket()
        
        self.assertEqual(precio_ticket, 56)

    def test_pagar_pasaje_con_saldo(self):
        self.sube.pagar_pasaje() #pagar metodo de 
        self.assertEqual(
            self.sube.saldo,
            930,
        )

    def test_imposible_pagar_pasaje_sin_saldo(self):
        sube = Sube()
        sube.saldo = 50 
        with self.assertRaises(NoHaySaldoException):
            sube.pagar_pasaje()

    def test_imposible_pagar_pasaje_con_usuario_desactivado(self):
        sube = Sube()
        sube.saldo = 500
        sube.estado = DESACTIVADO
        
        with self.assertRaises(UsuarioDesactivadoException):
            sube.pagar_pasaje()

    def test_pagar_pasaje_con_grupo_beneficiario(self):
        sube = Sube()
        sube.saldo = 35
        sube.grupo_beneficiario = PRIMARIO
        
        sube.pagar_pasaje()

        self.assertEqual(
            sube.saldo,
            0,
        )

    def test_cambiar_estado_sube_a_desactivado(self):
        estado = DESACTIVADO
        self.sube.cambiar_estado(estado)

        self.assertEqual(
            self.sube.estado, #para llamar un atributo de una clase self.nombreclase.nombreatributo
            DESACTIVADO,
        )

    def test_cambiar_estado_sube_a_activado(self):
        estado = ACTIVADO
        self.sube.cambiar_estado(estado)

        self.assertEqual(
            self.sube.estado,
            ACTIVADO,
        )

    def test_imposible_cambiar_a_estado_no_existente(self):
        estado = 'pendiente'

        with self.assertRaises(EstadoNoExistenteException):
            self.sube.cambiar_estado(estado)


if __name__ == '__main__':
    unittest.main()