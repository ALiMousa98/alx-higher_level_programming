class Base:
    """
    Base class representing a base object.

    Attributes:
        __nb_objects (int): Private class attribute to
            keep track of the number of objects created.
            id (int): Public instance attribute representin
        g the object's identifier.

    Methods:
        __init__(self, id=None): Class constructor to
        initialize a new Base object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base object.

        Args:
            id (int, optional): Identifier for the object.
            If provided, assign it to the id attribute.
            If not provided, increment __nb_objects and assign
            the new value to id.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
