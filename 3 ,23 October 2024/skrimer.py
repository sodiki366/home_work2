import tkinter as tk
from tkinter import messagebox
import winsound
import threading
import time


# Функция для воспроизведения звука и показа изображения
def show_scare():
    # Воспроизведение звука
    winsound.PlaySound("scary_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    # Создание окна с изображением
    scare_window = tk.Toplevel()
    scare_window.attributes("-fullscreen", True)  # Полноэкранный режим
    scare_window.attributes("-topmost", True)  # Поверх всех окон

    # Загрузка изображения
    img = tk.PhotoImage(file="scary_image.png")
    label = tk.Label(scare_window, image=img)
    label.pack(fill="both", expand=True)

    # Закрытие окна через 2 секунды
    scare_window.after(20, scare_window.destroy)


# Основное окно
root = tk.Tk()
root.title("Скример")
root.geometry("300x200")

# Кнопка для "взятия объекта"
button = tk.Button(root, text="Взять объект", command=show_scare)
button.pack(pady=50)

root.mainloop()