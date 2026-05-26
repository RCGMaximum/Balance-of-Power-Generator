#!/usr/bin/env python3

import os

# ============================================================
# ИНТЕРФЕЙС (русский / English)
# ============================================================
UI = {
    'ru': {
        'lang': 'ru',
        'title': "ГЕНЕРАТОР BALANCE OF POWER ДЛЯ HOI4",
        'tag_prompt': "Введите тег вашей страны (3 буквы, например GER). Если не знаете, нажмите Enter: ",
        'bop_id': "Введите ID Balance of Power (например, TAG_struggle_for_power_balance): ",
        'initial_value': "Начальное значение (по умолчанию 0.0): ",
        'left_side_id': "ID левой стороны: ",
        'left_side_icon': "Иконка левой стороны (GFX_...): ",
        'neutral_title': "НЕЙТРАЛЬНЫЙ ДИАПАЗОН",
        'neutral_id': "ID нейтрального диапазона: ",
        'neutral_min': "min (по умолчанию 0): ",
        'neutral_max': "max (по умолчанию 0): ",
        'right_side_id': "ID правой стороны: ",
        'right_side_icon': "Иконка правой стороны (GFX_...): ",
        'side_title_left': "ЛЕВАЯ СТОРОНА",
        'side_title_right': "ПРАВАЯ СТОРОНА",
        'add_range': "Добавить {} диапазон? (y/n): ",
        'range_id': "ID диапазона: ",
        'range_min': "min: ",
        'range_max': "max: ",
        'modifiers_prompt': "Модификаторы (например: political_power_factor=0.15, Enter для завершения): ",
        'modifier_input': "  модификатор: ",
        'on_activate_prompt': "Введите код on_activate (Enter - оставить пустым, 'DONE' - завершить): ",
        'on_deactivate_prompt': "Введите код on_deactivate (Enter - оставить пустым, 'DONE' - завершить): ",
        'decisions_category_prompt': "ID категории решений (Enter, если нет): ",
        'add_decision': "Добавить решение? (y/n): ",
        'decision_id': "ID решения: ",
        'decision_icon': "Иконка (Enter, если нет): ",
        'decision_allowed': "allowed (Enter - пропустить, или код, 'DONE' - завершить): ",
        'decision_available': "available (Enter - пропустить, или код, 'DONE' - завершить): ",
        'decision_visible': "visible (Enter - пропустить, или код, 'DONE' - завершить): ",
        'decision_ai': "ai_will_do (Enter - пропустить, или код, 'DONE' - завершить): ",
        'decision_complete': "complete_effect (Enter - пропустить, или код, 'DONE' - завершить): ",
        'category_allowed': "allowed категории (Enter - пропустить, или код, 'DONE' - завершить): ",
        'category_visible': "visible категории (Enter - пропустить, или код, 'DONE' - завершить): ",
        'loc_lang_choice': "Языки локализации (1=англ, 2=рус, 3=оба, 0=нет): ",
        'loc_en': "АНГЛИЙСКАЯ ЛОКАЛИЗАЦИЯ",
        'loc_ru': "РУССКАЯ ЛОКАЛИЗАЦИЯ",
        'loc_key_prompt': "  {} [Enter → \"{}\"]: ",
        'save_dir': "Папка для сохранения (по умолчанию 'generated_bop'): ",
        'done': "ГОТОВО!",
        'files_created': "Файлы созданы в папке: {}",
        'instruction_tag_known': "Инструкция:\n1. Скопируйте содержимое папки '{}' в ваш мод.\n2. В файл common/national_focus/{} добавьте в любой фокус:\n    completion_reward = {{\n        set_power_balance = {{\n            id = {}\n            left_side = {}\n            right_side = {}\n            set_value = {}\n        }}\n    }}",
        'instruction_tag_unknown': "Инструкция:\n1. Скопируйте содержимое папки '{}' в ваш мод.\n2. В файл common/national_focus/TAG (замените TAG на тег вашей страны) добавьте в любой фокус:\n    completion_reward = {{\n        set_power_balance = {{\n            id = {}\n            left_side = {}\n            right_side = {}\n            set_value = {}\n        }}\n    }}",
        'scale_title': "ШКАЛА БАЛАНСА СИЛ",
        'scale_left': "Левая",
        'scale_right': "Правая",
        'scale_neutral': "Нейтр.",
    },
    'en': {
        'lang': 'en',
        'title': "HOI4 BALANCE OF POWER GENERATOR",
        'choose_lang': "Select the interface language (1 - Russian, 2 - English): ",
        'tag_prompt': "Enter your country's tag (3 letters, e.g., GER). Press Enter if unknown: ",
        'bop_id': "Enter Balance of Power ID (e.g., TAG_struggle_for_power_balance): ",
        'initial_value': "Initial value (default 0.0): ",
        'left_side_id': "Left side ID: ",
        'left_side_icon': "Left side icon (GFX_...): ",
        'neutral_title': "NEUTRAL RANGE",
        'neutral_id': "Neutral range ID: ",
        'neutral_min': "min (default 0): ",
        'neutral_max': "max (default 0): ",
        'right_side_id': "Right side ID: ",
        'right_side_icon': "Right side icon (GFX_...): ",
        'side_title_left': "LEFT SIDE",
        'side_title_right': "RIGHT SIDE",
        'add_range': "Add {} range? (y/n): ",
        'range_id': "Range ID: ",
        'range_min': "min: ",
        'range_max': "max: ",
        'modifiers_prompt': "Modifiers (e.g., political_power_factor=0.15, Enter to finish): ",
        'modifier_input': "  modifier: ",
        'on_activate_prompt': "Enter on_activate code (Enter - skip, 'DONE' - finish): ",
        'on_deactivate_prompt': "Enter on_deactivate code (Enter - skip, 'DONE' - finish): ",
        'decisions_category_prompt': "Decision category ID (Enter if none): ",
        'add_decision': "Add decision? (y/n): ",
        'decision_id': "Decision ID: ",
        'decision_icon': "Icon (Enter if none): ",
        'decision_allowed': "allowed (Enter - skip, or code, 'DONE' - finish): ",
        'decision_available': "available (Enter - skip, or code, 'DONE' - finish): ",
        'decision_visible': "visible (Enter - skip, or code, 'DONE' - finish): ",
        'decision_ai': "ai_will_do (Enter - skip, or code, 'DONE' - finish): ",
        'decision_complete': "complete_effect (Enter - skip, or code, 'DONE' - finish): ",
        'category_allowed': "allowed for category (Enter - skip, or code, 'DONE' - finish): ",
        'category_visible': "visible for category (Enter - skip, or code, 'DONE' - finish): ",
        'loc_lang_choice': "Localisation languages (1=English, 2=Russian, 3=Both, 0=None): ",
        'loc_en': "ENGLISH LOCALISATION",
        'loc_ru': "RUSSIAN LOCALISATION",
        'loc_key_prompt': "  {} [Enter → \"{}\"]: ",
        'save_dir': "Output folder (default 'generated_bop'): ",
        'done': "DONE!",
        'files_created': "Files created in: {}",
        'instruction_tag_known': "Instructions:\n1. Copy the '{}' folder into your mod.\n2. In the file common/national_focus/{} add to any focus:\n    completion_reward = {{\n        set_power_balance = {{\n            id = {}\n            left_side = {}\n            right_side = {}\n            set_value = {}\n        }}\n    }}",
        'instruction_tag_unknown': "Instructions:\n1. Copy the '{}' folder into your mod.\n2. In the file common/national_focus/TAG (replace TAG with your country's tag) add to any focus:\n    completion_reward = {{\n        set_power_balance = {{\n            id = {}\n            left_side = {}\n            right_side = {}\n            set_value = {}\n        }}\n    }}",
        'scale_title': "BALANCE OF POWER SCALE",
        'scale_left': "Left",
        'scale_right': "Right",
        'scale_neutral': "Neutr.",
    }
}

# ============================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================
def print_header(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

def input_multiline(prompt):
    """Многострочный ввод. Enter или DONE (любой регистр) на первой строке - пусто."""
    print(prompt)
    first_line = input()
    if first_line.strip() == '' or first_line.strip().upper() == 'DONE':
        return ''
    lines = [first_line]
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
    return '\n'.join(lines)

def input_modifiers(ui):
    """Ввод модификаторов, завершается пустой строкой (Enter)"""
    mods = {}
    print(ui['modifiers_prompt'])
    while True:
        inp = input(ui['modifier_input']).strip()
        if not inp:
            break
        if '=' in inp:
            k, v = inp.split('=', 1)
            try:
                mods[k.strip()] = float(v.strip())
            except ValueError:
                print("    [!] Значение должно быть числом." if ui['lang']=='ru' else "    [!] Value must be a number.")
        else:
            print("    [!] Формат: имя=значение" if ui['lang']=='ru' else "    [!] Format: name=value")
    return mods

def ask_on_off(ui, prompt):
    """Запрашивает on_activate или on_deactivate. Enter или DONE (любой регистр) на первой строке - пусто."""
    print(prompt)
    first_line = input()
    if first_line.strip() == '' or first_line.strip().upper() == 'DONE':
        return ''
    lines = [first_line]
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
    return '\n'.join(lines)

def ordinal(n, lang):
    """Правильная нумерация на русском и английском"""
    if lang == 'ru':
        return f"{n}-й"
    else:
        if 11 <= n % 100 <= 13:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
        return f"{n}{suffix}"

def make_readable(key):
    """Делает читаемую заглушку из ключа, обрезая тег страны если есть"""
    parts = key.split('_')
    if len(parts) >= 2 and len(parts[0]) == 3 and parts[0].isupper():
        parts = parts[1:]  # обрезаем тег
    return ' '.join(parts).title()

def extract_tag(bop_id):
    """Извлекает тег страны из ID баланса (первые 3 заглавные буквы до _). Если не найдено - пустая строка."""
    parts = bop_id.split('_')
    if parts and len(parts[0]) == 3 and parts[0].isupper():
        return parts[0]
    return ''

def icon_to_texture(icon_name):
    """GFX_something -> gfx/interface/bop/something.dds"""
    if icon_name.startswith('GFX_'):
        base = icon_name[4:]
        return f"gfx/interface/bop/{base}.dds"
    return f"gfx/interface/bop/{icon_name}.dds"

# ============================================================
# ВИЗУАЛИЗАЦИЯ ШКАЛЫ (один ряд уникальных границ)
# ============================================================
def draw_scale(left_ranges, neutral_range, right_ranges, ui):
    # Собираем все диапазоны
    segments = []
    for r in left_ranges:
        segments.append((r['min'], r['max']))
    segments.append((neutral_range['min'], neutral_range['max']))
    for r in right_ranges:
        segments.append((r['min'], r['max']))

    total_min, total_max = -1.0, 1.0
    # Ширина шкалы: ВЫЧИСЛЯЕМ ДО ИСПОЛЬЗОВАНИЯ
    width = 60 + len(segments) * 5

    def to_x(val):
        return int((val - total_min) / (total_max - total_min) * (width - 1))

    # Заголовок той же ширины, что и шкала (теперь width уже существует)
    print("\n" + "=" * width)
    print(ui['scale_title'])
    print("=" * width)

    # Строим шкалу с границами
    scale_line = [' '] * width
    for seg_min, seg_max in segments:
        x1 = to_x(seg_min)
        x2 = to_x(seg_max)
        if 0 <= x1 < width:
            scale_line[x1] = '|'
        if 0 <= x2 < width:
            scale_line[x2] = '|'
    for seg_min, seg_max in segments:
        x1 = to_x(seg_min)
        x2 = to_x(seg_max)
        for i in range(x1 + 1, x2):
            if 0 <= i < width and scale_line[i] == ' ':
                scale_line[i] = '-'
    print("".join(scale_line))

    # Цифры под границами
    value_line = [' '] * width
    for seg_min, seg_max in segments:
        for val in (seg_min, seg_max):
            x = to_x(val)
            label = f"{val:.2f}"
            for i, ch in enumerate(label):
                pos = x + i
                if 0 <= pos < width:
                    value_line[pos] = ch
    print("".join(value_line))

    # Подписи сторон
    left_label = f"{ui['scale_left']} <<"
    right_label = f">> {ui['scale_right']}"
    neutral_label = ui['scale_neutral']

    left_pos = max(0, width // 4 - len(left_label) // 2)
    neutral_pos = width // 2 - len(neutral_label) // 2
    right_pos = min(width - len(right_label), 3 * width // 4 - len(right_label) // 2)

    sub_line = [' '] * width
    for i, ch in enumerate(left_label):
        if left_pos + i < width:
            sub_line[left_pos + i] = ch
    for i, ch in enumerate(neutral_label):
        if neutral_pos + i < width:
            sub_line[neutral_pos + i] = ch
    for i, ch in enumerate(right_label):
        if right_pos + i < width:
            sub_line[right_pos + i] = ch
    print("".join(sub_line))

# ============================================================
# ГЕНЕРАТОРЫ ФАЙЛОВ
# ============================================================
def generate_bop_file(bop_id, initial_value, left_side_id, right_side_id,
                      left_side_icon, right_side_icon,
                      left_ranges, neutral_range, right_ranges, decision_category):
    lines = [f"{bop_id} = {{",
             f"    initial_value = {initial_value}",
             f"    left_side = {left_side_id}",
             f"    right_side = {right_side_id}"]
    if decision_category:
        lines.append(f"    decision_category = {decision_category}")
    lines.append("")

    # Нейтральный диапазон
    nr = neutral_range
    lines.append(f"    range = {{")
    lines.append(f"        id = {nr['id']}")
    lines.append(f"        min = {nr['min']}")
    lines.append(f"        max = {nr['max']}")
    lines.append(f"        modifier = {{")
    if nr['modifier']:
        for k, v in nr['modifier'].items():
            lines.append(f"            {k} = {v}")
    lines.append(f"        }}")
    if nr['on_activate']:
        lines.append(f"        on_activate = {{\n{nr['on_activate']}\n        }}")
    if nr['on_deactivate']:
        lines.append(f"        on_deactivate = {{\n{nr['on_deactivate']}\n        }}")
    lines.append(f"    }}")
    lines.append("")

    # левая сторона
    lines.append(f"    side = {{")
    lines.append(f"        id = {left_side_id}")
    lines.append(f"        icon = \"{left_side_icon}\"")
    lines.append("")
    for r in left_ranges:
        lines.append(f"        range = {{")
        lines.append(f"            id = {r['id']}")
        lines.append(f"            min = {r['min']}")
        lines.append(f"            max = {r['max']}")
        lines.append(f"            modifier = {{")
        if r['modifier']:
            for k, v in r['modifier'].items():
                lines.append(f"                {k} = {v}")
        lines.append(f"            }}")
        if r['on_activate']:
            lines.append(f"            on_activate = {{\n{r['on_activate']}\n            }}")
        if r['on_deactivate']:
            lines.append(f"            on_deactivate = {{\n{r['on_deactivate']}\n            }}")
        lines.append(f"        }}")
        lines.append("")
    lines.append(f"    }}")
    lines.append("")

    # Правая сторона
    lines.append(f"    side = {{")
    lines.append(f"        id = {right_side_id}")
    lines.append(f"        icon = \"{right_side_icon}\"")
    lines.append("")
    for r in right_ranges:
        lines.append(f"        range = {{")
        lines.append(f"            id = {r['id']}")
        lines.append(f"            min = {r['min']}")
        lines.append(f"            max = {r['max']}")
        lines.append(f"            modifier = {{")
        if r['modifier']:
            for k, v in r['modifier'].items():
                lines.append(f"                {k} = {v}")
        lines.append(f"            }}")
        if r['on_activate']:
            lines.append(f"            on_activate = {{\n{r['on_activate']}\n            }}")
        if r['on_deactivate']:
            lines.append(f"            on_deactivate = {{\n{r['on_deactivate']}\n            }}")
        lines.append(f"        }}")
        lines.append("")
    lines.append(f"    }}")
    lines.append("}")
    return '\n'.join(lines)

def generate_localisation_file(lang, translations):
    """Генерация файла локализации без лишних комментариев"""
    return "l_{}:\n".format(lang) + "\n".join(
        f" {key}:0 \"{text}\"" for key, text in translations.items()
    )

def generate_gfx_file(sprites):
    """Генерация GFX файла для спрайтов сторон"""
    lines = ["spriteTypes = {"]
    for s in sprites:
        lines.append(f"    SpriteType = {{")
        lines.append(f"        name = \"{s['name']}\"")
        lines.append(f"        texturefile = \"{s['texture']}\"")
        lines.append(f"    }}")
    lines.append("}")
    return '\n'.join(lines)

def generate_decision_category_file(cat_id, allowed_code, visible_code):
    lines = [f"{cat_id} = {{"]
    if allowed_code.strip():
        lines.append(f"    allowed = {{\n{allowed_code}\n    }}")
    if visible_code.strip():
        lines.append(f"    visible = {{\n{visible_code}\n    }}")
    lines.append("}")
    return '\n'.join(lines)

def generate_decisions_file(decisions):
    lines = []
    for dec in decisions:
        lines.append(f"{dec['id']} = {{")
        if dec.get('icon'):
            lines.append(f"    icon = {dec['icon']}")
        for field in ['allowed', 'available', 'visible', 'ai_will_do', 'complete_effect']:
            content = dec[field].strip()
            if content:
                lines.append(f"    {field} = {{\n{content}\n    }}")
        lines.append("}")
        lines.append("")
    return '\n'.join(lines)

# ============================================================
# ОСНОВНОЙ ПРОЦЕСС
# ============================================================
def main():
    # Выбор языка интерфейса
    while True:
        lang_choice = input(UI['en']['choose_lang']).strip()
        if lang_choice == '1':
            ui = UI['ru']
            break
        elif lang_choice == '2':
            ui = UI['en']
            break
        else:
            print("Please enter 1 or 2")

    # Правила заполнения
    if ui['lang'] == 'ru':
        rules = [
            "ПРАВИЛА ЗАПОЛНЕНИЯ",
            "• Все значения от -1.0 до 1.0 (игра не примет другие)",
            "• min < max (например: -0.8 < -0.5)",
            "• Диапазоны идут без разрывов (max одного = min следующего)",
            "• Диапазоны не пересекаются",
            "• Левая сторона: от -1.0 до нейтрального",
            "• Правая сторона: от нейтрального до +1.0",
            "• Нейтральный диапазон строго между сторонами",
            "• Все ID должны быть уникальными",
            "• Дробные числа: через точку или запятую (0.8 или 0,8)",
            "• Подробная инструкция будет сохранена в README.txt"
        ]
    else:
        rules = [
            "FILLING RULES",
            "• All values from -1.0 to 1.0 (game rejects others)",
            "• min < max (e.g.: -0.8 < -0.5)",
            "• Ranges go without gaps (max of one = min of next)",
            "• Ranges do not overlap",
            "• Left side: from -1.0 to neutral",
            "• Right side: from neutral to +1.0",
            "• Neutral range strictly between sides",
            "• All IDs must be unique",
            "• Decimals: dot or comma (0.8 or 0,8)",
            "• Detailed instructions will be saved in README.txt"
        ]

    print_header(rules[0])
    for line in rules[1:]:
        print(line)
    print()

    print_header(ui['title'])

    # 0. Тег страны (запрашиваем, потом извлекаем из ID при необходимости)
    while True:
        tag_input = input(ui['tag_prompt'])
        # Проверяем, что ввод не состоит только из пробелов
        if tag_input.strip() == '':
            if tag_input == '':
                # Пользователь просто нажал Enter - ок
                tag_input = ''
                break
            else:
                # Пользователь ввёл только пробелы - ошибка
                print("  [!] Тег должен состоять ровно из 3 букв (например, GER). Попробуйте снова.")
                continue
        tag_input = tag_input.strip().upper()
        if len(tag_input) == 3 and tag_input.isalpha():
            break
        print("  [!] Тег должен состоять ровно из 3 букв (например, GER). Попробуйте снова.")
    
    # 1. Базовые параметры
    while True:
        bop_id = input(ui['bop_id']).strip()
        if bop_id:
            break
        print("  [!] ID обязателен. Введите значение." if ui['lang']=='ru' else "  [!] ID is required. Please enter a value.")
    try:
        initial_value = float((input(ui['initial_value']) or "0.0").replace(',', '.'))
    except ValueError:
        initial_value = 0.0

    # Определяем тег страны (приоритет введённому, иначе извлекаем)
    if len(tag_input) == 3 and tag_input.isalpha():
        country_tag = tag_input
    else:
        country_tag = extract_tag(bop_id)
        if not country_tag:
            country_tag = 'TAG'  # fallback
    
    # 2. Левая сторона
    print_header(ui['side_title_left'])
    left_side_id = input(ui['left_side_id']).strip()
    left_side_icon = input(ui['left_side_icon']).strip()
    if not left_side_id or not left_side_icon:
        print("Ошибка: ID и иконка обязательны." if ui['lang']=='ru' else "Error: ID and icon required.")
        return

    left_ranges = []
    range_num = 1
    while True:
        ans = input(ui['add_range'].format(ordinal(range_num, ui['lang']))).strip().lower()
        if ans != 'y':
            break
        rid = input(ui['range_id']).strip()
        if not rid:
            print("  [!] ID не может быть пустым." if ui['lang']=='ru' else "  [!] ID cannot be empty.")
            continue
        try:
            rmin = float((input(ui['range_min']) or "0").replace(',', '.'))
            rmax = float((input(ui['range_max']) or "1").replace(',', '.'))
        except ValueError:
            print("  [!] min и max должны быть числами." if ui['lang']=='ru' else "  [!] min and max must be numbers.")
            continue
        mods = input_modifiers(ui)
        on_act = ask_on_off(ui, ui['on_activate_prompt'])
        on_deact = ask_on_off(ui, ui['on_deactivate_prompt'])
        left_ranges.append({
            'id': rid, 'min': rmin, 'max': rmax,
            'modifier': mods, 'on_activate': on_act, 'on_deactivate': on_deact
        })
        range_num += 1

    # 3. Нейтральный диапазон
    print_header(ui['neutral_title'])
    neutral_id = input(ui['neutral_id']).strip()
    neutral_min = float((input(ui['neutral_min']) or "0").replace(',', '.'))
    neutral_max = float((input(ui['neutral_max']) or "0").replace(',', '.'))
    neutral_mods = input_modifiers(ui)
    neutral_on_act = ask_on_off(ui, ui['on_activate_prompt'])
    neutral_on_deact = ask_on_off(ui, ui['on_deactivate_prompt'])
    neutral_range = {
        'id': neutral_id,
        'min': neutral_min,
        'max': neutral_max,
        'modifier': neutral_mods,
        'on_activate': neutral_on_act,
        'on_deactivate': neutral_on_deact
    }

    # 4. Правая сторона
    print_header(ui['side_title_right'])
    right_side_id = input(ui['right_side_id']).strip()
    right_side_icon = input(ui['right_side_icon']).strip()
    if not right_side_id or not right_side_icon:
        print("Ошибка: ID и иконка обязательны." if ui['lang']=='ru' else "Error: ID and icon required.")
        return

    right_ranges = []
    range_num = 1
    while True:
        ans = input(ui['add_range'].format(ordinal(range_num, ui['lang']))).strip().lower()
        if ans != 'y':
            break
        rid = input(ui['range_id']).strip()
        if not rid:
            print("  [!] ID не может быть пустым." if ui['lang']=='ru' else "  [!] ID cannot be empty.")
            continue
        try:
            rmin = float((input(ui['range_min']) or "0").replace(',', '.'))
            rmax = float((input(ui['range_max']) or "1").replace(',', '.'))
        except ValueError:
            print("  [!] min и max должны быть числами." if ui['lang']=='ru' else "  [!] min and max must be numbers.")
            continue
        mods = input_modifiers(ui)
        on_act = ask_on_off(ui, ui['on_activate_prompt'])
        on_deact = ask_on_off(ui, ui['on_deactivate_prompt'])
        right_ranges.append({
            'id': rid, 'min': rmin, 'max': rmax,
            'modifier': mods, 'on_activate': on_act, 'on_deactivate': on_deact
        })
        range_num += 1

    # 5. Категория решений и решения
    dec_cat = input(ui['decisions_category_prompt']).strip()
    decisions_list = []
    cat_allowed = cat_visible = ""
    if dec_cat:
        while True:
            ans = input(ui['add_decision']).strip().lower()
            if ans != 'y':
                break
            dec_id = input(ui['decision_id']).strip()
            if not dec_id:
                continue
            dec_icon = input(ui['decision_icon']).strip()
            dec_allowed = ask_on_off(ui, ui['decision_allowed'])
            dec_available = ask_on_off(ui, ui['decision_available'])
            dec_visible = ask_on_off(ui, ui['decision_visible'])
            dec_ai = ask_on_off(ui, ui['decision_ai'])
            dec_complete = ask_on_off(ui, ui['decision_complete'])
            decisions_list.append({
                'id': dec_id, 'icon': dec_icon,
                'allowed': dec_allowed, 'available': dec_available,
                'visible': dec_visible, 'ai_will_do': dec_ai,
                'complete_effect': dec_complete
            })
        cat_allowed = ask_on_off(ui, ui['category_allowed'])
        cat_visible = ask_on_off(ui, ui['category_visible'])

    # 6. Локализация
    all_keys = [bop_id, left_side_id, right_side_id, neutral_id]
    for r in left_ranges + right_ranges:
        all_keys.append(r['id'])
    if dec_cat:
        all_keys.append(dec_cat)
        for dec in decisions_list:
            all_keys.append(dec['id'])

    lang_choice_loc = input(ui['loc_lang_choice']).strip()
    translations = {}
    if lang_choice_loc in ('1', '2', '3'):
        langs = []
        if lang_choice_loc == '1':
            langs = ['english']
        elif lang_choice_loc == '2':
            langs = ['russian']
        else:
            langs = ['english', 'russian']
        for lang in langs:
            header = ui['loc_en'] if lang == 'english' else ui['loc_ru']
            print_header(header)
            trans = {}
            for key in all_keys:
                readable = make_readable(key)
                text = input(ui['loc_key_prompt'].format(key, readable)).strip()
                if not text:
                    text = readable
                trans[key] = text
            translations[lang] = trans

    # 7. Визуализация шкалы
    draw_scale(left_ranges, neutral_range, right_ranges, ui)

    # 8. Сохранение файлов
    base_dir = input(ui['save_dir']).strip() or "generated_bop"
    os.makedirs(base_dir, exist_ok=True)

    # BOP файл
    bop_content = generate_bop_file(
        bop_id, initial_value, left_side_id, right_side_id,
        left_side_icon, right_side_icon,
        left_ranges, neutral_range, right_ranges, dec_cat
    )
    bop_path = os.path.join(base_dir, "common", "bop", f"{bop_id}.txt")
    os.makedirs(os.path.dirname(bop_path), exist_ok=True)
    with open(bop_path, 'w', encoding='utf-8') as f:
        f.write(bop_content)
    print(f"[OK] {bop_path}")

    # GFX файл (автоматически из иконок, имя через тег)
    sprites = [
        {'name': left_side_icon, 'texture': icon_to_texture(left_side_icon)},
        {'name': right_side_icon, 'texture': icon_to_texture(right_side_icon)}
    ]
    gfx_filename = f"{country_tag}_bop.gfx" if country_tag != 'TAG' else "TAG_bop.gfx"
    gfx_path = os.path.join(base_dir, "interface", gfx_filename)
    os.makedirs(os.path.dirname(gfx_path), exist_ok=True)
    gfx_content = generate_gfx_file(sprites)
    with open(gfx_path, 'w', encoding='utf-8') as f:
        f.write(gfx_content)
    print(f"[OK] {gfx_path}")

    # Локализация
    for lang, trans in translations.items():
        loc_content = generate_localisation_file(lang, trans)
        loc_path = os.path.join(base_dir, "localisation", lang, f"{bop_id}_l_{lang}.yml")
        os.makedirs(os.path.dirname(loc_path), exist_ok=True)
        with open(loc_path, 'w', encoding='utf-8') as f:
            f.write(loc_content)
        print(f"[OK] {loc_path}")

    # Категория решений
    if dec_cat:
        cat_content = generate_decision_category_file(dec_cat, cat_allowed, cat_visible)
        cat_path = os.path.join(base_dir, "common", "decisions", "categories", f"{country_tag}_decision_categories.txt")
        os.makedirs(os.path.dirname(cat_path), exist_ok=True)
        with open(cat_path, 'w', encoding='utf-8') as f:
            f.write(cat_content)
        print(f"[OK] {cat_path}")

    # Решения
    if decisions_list:
        decs_content = generate_decisions_file(decisions_list)
        decs_path = os.path.join(base_dir, "common", "decisions", f"{country_tag}_decisions.txt")
        os.makedirs(os.path.dirname(decs_path), exist_ok=True)
        with open(decs_path, 'w', encoding='utf-8') as f:
            f.write(decs_content)
        print(f"[OK] {decs_path}")

    # Инструкция
    print_header(ui['done'])
    print(ui['files_created'].format(os.path.abspath(base_dir)))
    if country_tag != 'TAG':
        instruction = ui['instruction_tag_known'].format(
            base_dir, f"{country_tag}.txt", bop_id, left_side_id, right_side_id, initial_value
        )
    else:
        instruction = ui['instruction_tag_unknown'].format(
            base_dir, bop_id, left_side_id, right_side_id, initial_value
        )
    print(instruction)
    input("\n" + ("Нажмите Enter для выхода..." if ui['lang']=='ru' else "Press Enter to exit..."))

if __name__ == "__main__":
    main()