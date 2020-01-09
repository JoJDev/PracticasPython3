def validate_credentials(func):
    def wrapper(user):
      if user == "Platzi":
        for i in user:
          print(i)
      else: 
        print("No funciona")    
    return wrapper

@validate_credentials
def validate_user(user):
    if user == "Platzi":
        print('El usuario {} es valido'.format(user))
    else:
        print("El usuario {} no es valido".format(user))


def main():
    user = str(input("Digita el usuario: "))
    validate_user(user)


if __name__ == '__main__':
    main()