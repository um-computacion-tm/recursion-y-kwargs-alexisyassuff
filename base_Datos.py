import unittest

# Construir una funcion que permita recibir los nombres y apellidos de una persona, para verificar si se encuentra en la base de datos. La
# función debería retornar el "id" o la key del diccionario que contiene a una persona con todos los nombres y apellidos pasados como
# parametros a la funcion buscar_datos()
# Ejemplo:
# Si busco una persona cuyo nombre sea "Pablo Diego Ruiz Picasso", entonces, la llamada a la función será:
# buscar_datos("Pablo", "Diego","Ruiz","Picasso", **database)
# Donde cada uno de los primeros argumetos serán los nombres y apellidos (no necesariamente ordenados) y el último parametro, indicado con
# asteriscos, sería la base de datos.
# En base a esta llamada a la función, se debería retornar el valor de la key del diccionario que contiene los valores "Pablo, Diego, Ruiz,
# Picasso"
# buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database) -> 1
# Donde 1 es la key que identifica al diccionario correspondiente que contiene todos esos valores (ni mas ni menos)

database = {
            "1":{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            "2":{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            "3":{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            }
}

def buscar_datos(*words, **kwords):
    for num, dic in kwords.items():
        if all(word in dic.values() for word in words) and len(dic.values()) == len(words):
            return num
    return None

class TestBusqueda(unittest.TestCase):
    def test_ordenado(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,"1")

    def test_ordenado_2(self):
        resultado = buscar_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", **database)
        self.assertEqual(resultado,"3")

    def test_no_ordenado(self):
        resultado = buscar_datos("Anci","Elio", **database)
        self.assertEqual(resultado,"2")

    def test_no_existente(self):
        resultado = buscar_datos("Marcelo", "Paez", **database)
        self.assertEqual(resultado,None)
    

if __name__ == '__main__':
    unittest.main()