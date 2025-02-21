class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso

    def mostrar_detalles(self):
        print(f'El nombre del curso es {self.nombre}')
        print(f'La código del curso es {self.codigo}')
        print(f'Descripción: {self.descripcion}')


    def actualizar_descripcion(self, nueva_descripcion):
        self.nueva_descripcion = nueva_descripcion

    def __str__(self):
        return f'{self.nombre}, {self.codigo}, {self.descripcion}

    def __repr__(self):

    @classmethod
    def desde_tupla(cls, tupla):

    @staticmethod
    def es_curso_abierto():
