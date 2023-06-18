from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle object.

    Inherits:
        Base: Base class for basic object functionality.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle's position.
        y (int): Y-coordinate of the rectangle's position.
        id (int): Identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Class constructor to initialize a new Rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle's position.
                               Default is 0.
            y (int, optional): Y-coordinate of the rectangle's position.
                               Default is 0.
            id (int, optional): Identifier for the rectangle.
                                If provided, use it as the id.
                    If not provided, let the Base class assign an id.

        Returns:
            None

        Raises:
            TypeError: If any attribute (width, height, x, y)
            is not an integer.
            ValueError: If width or height is less than or equal to 0,
                        or if x or y is less than 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): New width value.

        Returns:
            None

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): New height value.

        Returns:
            None

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: X-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): New x-coordinate value.

        Returns:
            None

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: Y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): New y-coordinate value.

        Returns:
            None

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ Methods """
    def area(self):
        """
        Calculate and return the area of the Rectangle instance.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with '#' characters.

        Returns:
            None
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
