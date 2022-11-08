class Cereal:
    def __init__(self, values: dict = None) -> None:
        self.id = None
        self.name = None
        self.mfr = None
        self.type = None
        self.calories = None
        self.protein = None
        self.fat = None
        self.sodium = None
        self.fiber = None
        self.carbo = None
        self.sugars = None
        self.potass = None
        self.vitamins = None
        self.shelf = None
        self.weight = None
        self.cups = None
        self.rating = None

        if values is not None:
            for k, v in values.items():
                if hasattr(self, k.lower()):
                    setattr(self, k.lower(), v)

    @property
    def get_values(self):
        return (
                self.name,
                self.mfr,
                self.type,
                self.calories,
                self.protein,
                self.fat,
                self.sodium,
                self.fiber,
                self.carbo,
                self.sugars,
                self.potass,
                self.vitamins,
                self.shelf,
                self.weight,
                self.cups,
                self.rating,
            )

    def __str__(self) -> str:
        return self.name

    @property
    def get_mfr(self) -> str:
        match(self.mfr.upper()):
            case 'A':
                return "American Home Food Products"
            case 'G':
                return "General Mills"
            case 'K':
                return "Kelloggs"
            case 'N':
                return "Nabisco"
            case 'P':
                return "Post"
            case 'Q':
                return "Quaker Oats"
            case 'R':
                return "Ralston Purina"
            case _:
                return "Probably Nestlé"

    @property
    def get_type(self) -> str:
        match(self.type.upper()):
            case 'C':
                return "Cold"
            case 'H':
                return "Hot"
            case _:
                return "Soggy"
