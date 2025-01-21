def get_cats_info(path):
    try:
        cats_info = []
    
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats_dict = {"id": id, "name": name, "age": age}
                cats_info.append(cats_dict)

        return cats_info
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return None, None
    except ValueError:
        print(f"Помилка при обробці файлу '{path}'. Перевірте формат даних.")
        return None, None
cats_info = get_cats_info("C:/Users/Серёжа/git/first_nepo/cats_file.txt")
print(cats_info)
