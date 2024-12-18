from brovkatop import ImageHandler as ImageHandler
from brovkatop import ImageProcessor as ImageProcessor
images = [] 
 
decor = "=" * 22 
Status = True 
 
def print_menu(): 
    print(f"{decor} Выберите пункт меню {decor}") 
    print("1 - Загрузить изображение") 
    print("2 - Сохранить изображение") 
    print("3 - Использовать Thumbnail (200x200) для изображения") 
    print("4 - Использовать ImageProcessor (контур) для изображения") 
    print("5 - Использовать ImageProcessor (добавить текст в центр) для изображения") 
    print("6 - Список изображений в памяти программы") 
    print("7 - Просмотреть изображение из памяти программы") 
    print("8 - Завершить выполнение программы") 
    print(decor * 2) 
 
def print_images (): 
    print(decor * 2) 
    counter = 0 
    for image in images: 
        counter += 1 
        print(f"{counter}. {image.filename}") 
    print() 
 
while Status: 
    print_menu() 
    input_data = input("Введите нужное значение: ") 
    try: 
        input_data = int(input_data) 
    except ValueError: 
        print("Введите корректное значение!") 
    if input_data == 1: 
        print(decor * 2) 
        input_data = input("Укажите путь до изображения, которое хотите загрузить в память: ") 
        try: 
            images.append(ImageHandler(input_data)) 
            print("Изображение успешно добавлено!") 
        except FileNotFoundError: 
            print("Файл не найден. Проверьте корректность введенных данных") 
    elif input_data == 2: 
        print_images() 
        input_data = input("Выберите изображение, которое хотите сохранить: ") 
        try: 
            input_data = int(input_data) 
            name = input("Введите название сохраняемого изображения: ") 
            images[input_data - 1].save(name) 
            print("Успешно сохранено!")
        except: 
            print("Не удалось найти изображение. Проверьте корректность введенных данных!") 
    elif input_data == 3: 
        print_images() 
        input_data = input("Выберите изображение, на котором хотите использовать Thumbnail (200x200): ") 
        try: 
            input_data = int(input_data) 
            images[input_data - 1].thumbnail() 
            print("Thumbnail (200x200) для изображения успешно применен!") 
        except FileNotFoundError: 
            print("Файл не найден. Проверьте корректность введенных данных") 
    elif input_data == 4: 
        print_images() 
        input_data = input("Выберите изображение, на котором хотите использовать ImageProcessor (контур): ") 
        try: 
            input_data = int(input_data) 
            images[input_data - 1].processor.contour(images[input_data - 1]) 
            print("ImageProcessor (контур) для изображения успешно применен!") 
        except FileNotFoundError: 
            print("Файл не найден. Проверьте корректность введенных данных") 
    elif input_data == 5: 
        print_images() 
        input_data = input("Выберите изображение, на котором хотите использовать ImageProcessor (добавить текст в центр): ") 
        try: 
            input_data = int(input_data) 
            images[input_data - 1].processor.apply_text(images[input_data - 1]) 
            print("ImageProcessor (добавить текст в центр) для изображения успешно применен!") 
        except FileNotFoundError: 
            print("Файл не найден. Проверьте корректность введенных данных") 
    elif input_data == 6: 
        print("Вот список изображений в памяти программы: ") 
        print_images() 
    elif input_data == 7: 
        print_images() 
        input_data = input("Выберите изображение, которое хотите просмотреть: ") 
        try: 
            input_data = int(input_data) 
            images[input_data - 1].img.show() 
        except FileNotFoundError: 
            print("Файл не найден. Проверьте корректность введенных данных") 
    elif input_data == 8: 
        print("Завершаю выполнение программы...") 
        Status = False