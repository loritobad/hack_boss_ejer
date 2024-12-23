class Address:
    """Clase que representa una dirección."""
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"