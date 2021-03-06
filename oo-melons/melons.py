"""Classes for melon orders."""
from random import randint


class AbstractMelonOrder():

    def __init__(self, species, qty, country_code=None):      
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.base_price = self.get_base_price()

    def get_base_price(self):
        base_price = randint(5, 10)
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas":
            self.base_price *= 1.5

        total = (1 + self.tax) * self.qty * self.base_price
        return total
   
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
       
        self.shipped = True

   


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        if self.qty < 10:
            total = super().get_total()
            total += 3
            return total
