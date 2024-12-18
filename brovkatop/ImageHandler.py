from PIL import Image 
from .ImageProcessor import *
class ImageHandler (): 
    def __init__(self, path): 
        try: 
            self.img = Image.open(path) 
            self.format = self.img.format 
            self.path = path 
            self.filename = self.img.filename 
            self.processor = ImageProcessor(img=self.img) 
        except: 
            raise FileNotFoundError("Укажите действительный путь к файлу!") 
    def save(self, name): 
        self.img.save(f'{name}.{self.format}') 
    def thumbnail(self): 
        try: 
            max_size = (200, 200) 
            self.img.thumbnail(max_size) 
        except: 
            raise AttributeError("Ошибка! Проверьте корректность данных!") 