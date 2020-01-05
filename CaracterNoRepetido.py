

def primerCaracterNoRepetido(secuenciaCaracteres):
    caracteres = {};

    if secuenciaCaracteres == "":
        return "_";
    else:
        for letra in secuenciaCaracteres:
            caracteres[letra] = 0;

        for letra in secuenciaCaracteres:
            caracteres[letra] +=1;

        for letra in secuenciaCaracteres:
            if caracteres[letra] == 1:
                return letra;
        
        return "_";


if __name__ == "__main__":
    secuenciaCaracteres = input("Ingresa tu secuencia de caracteres: \n");

    resultado = primerCaracterNoRepetido(secuenciaCaracteres);

    if resultado == "_":
        print("Todos los caracteres se repiten");
    else:
        print("El primer caracter que no se repite primero es: {}".format(resultado));
