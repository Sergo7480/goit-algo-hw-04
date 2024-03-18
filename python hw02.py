def get_cats_info(path):
    try:
        cats_list = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": cat_age
                }
                cats_list.append(cat_info)
        return cats_list
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except ValueError:
        print(f"Помилка при обробці файлу '{path}'. Перевірте формат даних.")
        return []
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
