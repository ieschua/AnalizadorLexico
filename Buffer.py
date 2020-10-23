#Principal.py
#Programado por Ieschua S.  - Compiladores / 4NV50


class Buffer:
    def cargar_buffer(self, filepath):
        arq = open(filepath, 'r')
        texto = arq.readline()

        buffer = []
        cont = 1

        # El tamaño del búfer se puede cambiar cambiando cont
        while texto != "":
            buffer.append(texto)
            texto = arq.readline()
            cont += 1

            if cont == 10 or texto == '':
                # Devuelve un búfer completo
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reiniciar el búfer
                buffer = []

        arq.close()

