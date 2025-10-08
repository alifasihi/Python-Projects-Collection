from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address):
    geolocator = Nominatim(user_agent='distance_calculator')
    location = geolocator.geocode(address)
    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates):
    if home and target:
        distance = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance


def get_distance_km(home: str, target: str):
    home_coordinates = get_coordinates(home)
    target_coordinates = get_coordinates(target)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home} -> {target}')
        print(f'{distance:.2f} kilometers')
        return distance
    else:
        print('No Distance')


def main():
    home_address = 'Kerman , Iran'
    print(f'home address :{home_address}')

    target_address = input('Enter an address: >>')
    print('Calculating...')

    get_distance_km(home_address, target_address)


if __name__ == '__main__':
    main()
