from constants import IMAGE_DIR

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
            # If `Cereal` contains a field with the name of `k`, set the value of said field.
            for k, v in values.items():
                if hasattr(self, k.lower()):
                    setattr(self, k.lower(), v)

    @property
    def get_values(self):
        """Gets the fields needed to insert into database.
        """
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


    @property
    def get_values_for_update(self):
        """Gets the fields needed to update in database.
        """
        return self.get_values + (self.id,)


    def __str__(self) -> str:
        return self.name


    @property
    def get_mfr(self) -> str:
        """Returns the 'proper' value of Manufacturer `Char` value.
        """
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
        """Returns the 'proper' value of Type `Char` value.
        """
        match(self.type.upper()):
            case 'C':
                return "Cold"
            case 'H':
                return "Hot"
            case _:
                return "Soggy"

    @property
    def get_img(self) -> str:
        from os import listdir
        for x in listdir(IMAGE_DIR):
            if x.startswith(str(self.id)):
                return f"{IMAGE_DIR}\\{x}"
        return ""