class Rectangle:
    
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    
    def set_width(self,width):
        self.width=width
    
    def set_height(self,height):
        self.height=height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            string=''
            for _ in range(self.height):
                for __ in range(self.width):
                    string+="*"
                string+="\n"
            return string
    def get_amount_inside(self,shape):
        a1=shape.get_area()
        a2=self.get_area()
        return int(a2/a1)
    

class Square(Rectangle):

    def __init__(self,side):
        self.width=side
        self.height=side
    
    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self,side):
        self.width=side
        self.height=side

    def set_width(self,side):
        self.width=side
        self.height=side
    
    def set_height(self,side):
        self.height=side
        self.width=side