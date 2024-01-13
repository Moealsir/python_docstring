#!/usr/bin/python3

"""
Square module
"""


class Square:
    """
    Square - Add a brief here.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ - Add a brief here.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position
    @property

    def position(self):
        """
        position - Add a brief here.
        """
        return self.__position
    @position.setter

    def position(self, value):
        """
        position - Add a brief here.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    @property

    def size(self):
        """
        size - Add a brief here.
        """
        return self.__size
    @size.setter

    def size(self, value):
        """
        size - Add a brief here.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area - Add a brief here.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        my_print - Add a brief here.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

"""
Square1 module
"""


class Square1:
    """
    Square1 - Add a brief here.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ - Add a brief here.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position
    @property

    def position1(self):
        """
        position1 - Add a brief here.
        """
        return self.__position
    @position.setter

    def position1(self, value):
        """
        position1 - Add a brief here.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    @property

    def size1(self):
        """
        size1 - Add a brief here.
        """
        return self.__size
    @size.setter

    def size1(self, value):
        """
        size1 - Add a brief here.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area1(self):
        """
        area1 - Add a brief here.
        """
        return self.__size * self.__size

    def my_print1(self):
        """
        my_print1 - Add a brief here.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

"""
create_backup - Add a brief here.
"""

def create_backup(file_path):
    """
    create_backup - Add a brief here.
    """

    backup_path = file_path + ".bak"
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")

"""
create_backup1 - Add a brief here.
"""

def create_backup1(file_path):
    """
    create_backup1 - Add a brief here.
    """

    backup_path = file_path + ".bak"
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created: {backup_path}")
