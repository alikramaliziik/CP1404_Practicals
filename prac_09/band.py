from musician import Musician


class Band:
    """Band class for managing a group of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the Band."""
        if isinstance(musician, Musician):
            self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the Band."""
        musician_strs = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strs)})"

    def play(self):
        """Return a string showing what each musician is playing."""
        return '\n'.join(musician.play() for musician in self.musicians)
"""band (str)
Extreme (Nuno Bettencourt ([Washburn N4 (1990) : $2,499.95, Takamine acoustic (1986) : $1,200.00]), Gary Cherone ([]), Pat Badger ([Mouradian CS-74 Bass (2009) : $1,500.00]), Kevin Figueiredo ([]))
band.play()
Nuno Bettencourt is playing: Washburn N4 (1990) : $2,499.95
Gary Cherone needs an instrument!
Pat Badger is playing: Mouradian CS-74 Bass (2009) : $1,500.00
Kevin Figueiredo needs an instrument!
"""