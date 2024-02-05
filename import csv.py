import csv

def check_credentials(username, password, filename):
    with open(filename, "r", newline='') as h:
        reader = csv.reader(h, delimiter=';')
        for row in reader:
            if len(row) > 2 and ((username == row[0] and password == row[1]) or (username == row[1] and password == row[2])):
                return True
    return False

# Пример использования
filename = "base.csv"  # Замените на фактическое имя вашего файла
log_text = "booker12"
pas_text = "1111"

if check_credentials(log_text, pas_text, filename):
    print("Вход разрешен")
else:
    print("Вход запрещен")