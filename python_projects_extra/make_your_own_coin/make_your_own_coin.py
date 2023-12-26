import random

class Coin:
    def __init__(self, original_value, clean_colour, rusty_colour, num_edges, diameter, thickness, mass):
        self.original_value = original_value
        self.clean_colour = clean_colour
        self.rusty_colour = rusty_colour
        self.num_edges = num_edges
        self.diameter = diameter
        self.thickness = thickness
        self.mass = mass
        self.is_rare = False
        self.is_clean = True
        self.heads = True  # Default value
        
        # Adjusting value and colour based on rarity and cleanliness
        self.value = self.original_value * 1.25 if self.is_rare else self.original_value
        self.colour = self.clean_colour if self.is_clean else self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        self.heads = random.choice([True, False])

    def __str__(self):
        if self.original_value >= 1.00:
            return f"{int(self.original_value)} coin"
        else:
            return f"{int(self.original_value * 100)}p coin"

class OnePence(Coin):
    def __init__(self):
        super().__init__(original_value=0.01, clean_colour="Bronze", rusty_colour="Brownish",
                         num_edges=1, diameter=20.3, thickness=1.52, mass=3.56)

class TwoPence(Coin):
    def __init__(self):
        super().__init__(original_value=0.02, clean_colour="Bronze", rusty_colour="Brownish",
                         num_edges=1, diameter=25.9, thickness=1.85, mass=7.12)

# Other coin denominations can follow a similar structure

# Instantiate coin objects
one_pence = OnePence()
two_pence = TwoPence()

# Display coin information
coins = [one_pence, two_pence]
for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{} - Colour: {}, Value: {}, Diameter: {}, Thickness: {}, Num Edges: {}, Mass (gms): {}".format(*arguments)
    print(string)
