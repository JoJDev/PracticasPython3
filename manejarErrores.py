countries = {
	'mexico': 122,
	'colombia': 49,
	'argentina': 43,
	'chile': 18,
	'peru': 31
}

while True:
	country = str(input('Escribe el nombre de un país: ')).lower()

	try:
		print('La póblacion de {} es: {} millones'.format(country, countries[country]))
	except KeyError:
		print('No tenemos la póblacion del pais {}'.format(country))
		