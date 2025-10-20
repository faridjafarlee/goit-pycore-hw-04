def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        cat_id, name, age = line.split(',')
                        cat_dict = {
                            "id": cat_id,
                            "name": name,
                            "age": age
                        }
                        cats_list.append(cat_dict)
                    except ValueError:
                        print(f"Помилка у форматі рядка: {line}")
                        continue
        
        return cats_list
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []


if __name__ == "__main__":
    import json
    cats_info = get_cats_info("cats_file.txt")
    print(json.dumps(cats_info, indent=4, ensure_ascii=False))