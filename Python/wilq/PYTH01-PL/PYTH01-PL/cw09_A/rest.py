import requests


def stacje_w_miejscowosci(miejscowosc):
    dane_str = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/findAll')
    dane_json = dane_str.json()
    lista_stacji = [stacja for stacja in dane_json if stacja['city']['name'] == miejscowosc]
    for stacja in lista_stacji:
        print(f"{stacja['id']:7} "
              f"{stacja['stationName']:30} "
              f"({stacja['gegrLat']}, {stacja['gegrLon']})   "
              f"{stacja['addressStreet']}")


if __name__ == '__main__':
    stacje_w_miejscowosci('Wałbrzych')
