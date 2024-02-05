import tkinter as tk
from g4f import ChatCompletion

def send_and_receive_message():
    user_message = user_input.get()

    # Виведення питання у Label
    question_label.config(text=f"User: {user_message}")

    # Задавання питання тільки, якщо стосується Marvel
    if "Marvel" or "marvel" in user_message:
        # Виклик g4f.ChatCompletion.create для отримання відповіді
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            stream=True,
        )

        # Отримання відповіді горизонтально
        response_text = ' '.join([str(message) for message in response])
        response_text = response_text[:200]
        # Виведення відповіді у Label
        response_label.config(text=f"AI: {response_text}")
    else:
        # Якщо питання не стосується Marvel, виведення відповіді у Label
        response_label.config(text="AI: Sorry, I can only answer questions related to Marvel.")

# Створення головного вікна
app = tk.Tk()
app.title("Marvel Chat Application")
app.geometry('344x582')
app.config(bg='#5F0000')

# Створення елементів у вікні
user_input = tk.Entry(app, width=34)
send_button = tk.Button(app, text="Надіслати", command=send_and_receive_message)
question_label = tk.Label(app, text="", wraplength=300, justify="left", fg='white', bg='#5F0000')
response_label = tk.Label(app, text="", wraplength=300, justify="left", fg='white', bg='#5F0000')

user_input.place(x=15, y=550)
send_button.place(x=257, y=546)
question_label.place(x=10, y=10)
response_label.place(x=10, y=30)

# Запуск головного циклу подій
app.mainloop()
