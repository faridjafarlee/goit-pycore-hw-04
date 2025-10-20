def total_salary(path):
    try:
        total = 0
        count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        name, salary = line.split(',')
                        total += float(salary)
                        count += 1
                    except ValueError:
                        print(f"Помилка у форматі рядка: {line}")
                        continue
        
        if count == 0:
            return (0, 0)
        
        average = int(total / count)
        return (int(total), average)
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")