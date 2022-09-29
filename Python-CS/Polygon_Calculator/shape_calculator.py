class Rectangle:

    def __init__(self, width, heigth) -> None:
        self.width = width
        self.height = heigth

    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, heigth) -> None:
        self.height = heigth

    def get_area(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self)-> str:
        if Rectangle.get_area(self) > 50:
            return "Too big for picture."
        line = int(Rectangle.get_area(self)) * '*'
        return '\n'.join(line[i:i+int(self.width)] for i in range(0, len(line), int(self.width))) + '\n'

    def get_amount_inside(self, shape) -> int: 
        return int(self.get_area()/shape.get_area())

    def __repr__(self) -> str:
        return f'Rectangle(width={int(self.width)}, height={int(self.height)})'
        
    


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side
    def set_side(self, side) -> None:
        self.width = side
        self.height = side
    def __repr__(self) -> str:
        return f'Square(side={int(self.width)})'