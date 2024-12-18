from PIL import ImageFilter 
from PIL import ImageDraw 
from PIL import ImageFont 
class ImageProcessor(): 
    def __init__(self, img): 
        try: 
            self.img = img 
        except: 
            raise FileExistsError("Передайте корректное изображение!") 
    def contour (self, handler): 
        try: 
            self.img = self.img.filter(ImageFilter.CONTOUR) 
            handler.img = self.img 
        except: 
            raise AttributeError("Укажите действительный handler!") 
    def apply_text (self, handler): 
        font_size=32 
        try: 
            unicode_font = ImageFont.truetype("DejaVuSans.ttf", font_size) 
        except: 
            raise FileNotFoundError("Проверьте наличие шрифта в корневой папке с проектом!") 
        try: 
            message = "Вариант 3" 
            x, y = self.img.size 
            draw = ImageDraw.Draw(self.img) 
            _, _, w, h = draw.textbbox((0,0), message, unicode_font) 
            draw.text(((x-w) / 2, (y-h) / 2), message, font=unicode_font, fill=(255, 255, 255)) 
            handler.img = self.img 
        except: 
            raise AttributeError("Укажите действительный handler!") 