def total_salary(path):
    try:
        total_sum = 0
        count = 0

        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_sum += int(salary)
                count += 1

        average_salary = total_sum / count
        return total_sum, average_salary
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None
    except ValueError:
        print(f"Помилка при обробці файлу '{path}'. Перевірте формат даних.")
        return None, None
total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")