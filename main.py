# Пример словаря с кодами МКБ-10 для некоторых заболеваний
icd10_codes = {
    "ИнТулинозависимый сахарный диабет с неврологическими осложнениями": "E10.4",
    "Астма неуточненная": "J45.9",
    "ипертензия первичная (эссенциальная)": "I10",
    # Добавьте другие коды по мере необходимости
}

# Функция для получения кода МКБ-10 по первым 3 символам названия заболевания
def get_icd10_code_partial(diagnosis_partial):
    for diagnosis, code in icd10_codes.items():
        if diagnosis.lower().startswith(diagnosis_partial.lower()):
            return diagnosis, code
    return None, "Код не найден"

# Ввод заболевания пользователем
user_input = input("Введите первые 3 символа названия заболевания: ")
diagnosis, code = get_icd10_code_partial(user_input)

# Отображение результата
print(f"Диагноз: {diagnosis}, Код МКБ-10: {code}")
