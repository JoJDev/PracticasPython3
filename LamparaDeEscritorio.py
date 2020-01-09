class LamparaDeEscritorio:

    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    #método de instancia "Self"
    #método __init__ es el constructor
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


#definiendo la función run() ----> inicializar el programa, despegar la clase

def run():
    lamp = LamparaDeEscritorio(is_turned_on=False)

#Loop de ejecución:

    while True:
        command = str(input('''
        ¿Qué deseas hacer?

        [p]render
        [a]pagar
        [s]alir'''


        ))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break



#punto de acceso:

if __name__ == '__main__':
    run()