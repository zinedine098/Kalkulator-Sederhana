import flet as ft

def main(page: ft.Page):
    page.title = "Aplikasi Pertamaku"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text = ft.Text(
        value="Kalkulator Sederhana",
        text_align=ft.TextAlign.CENTER,
        size=30,
        weight=ft.FontWeight.BOLD,
    )
    number1 = ft.TextField(label="Angka Pertama")
    number2 = ft.TextField(label="Angka Kedua")
    result = ft.Text()

    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def add(e):
        if not is_number(number1.value) or not is_number(number2.value):
            result.value = "Masukkan input yang valid"
        else:
            result.value = int(number1.value) + int(number2.value)
        page.update()

    def min(e):
        if not is_number(number1.value) or not is_number(number2.value):
            result.value = "Masukkan input yang valid"
        else:
            result.value = int(number1.value) - int(number2.value)
        page.update()

    def kali(e):
        if not is_number(number1.value) or not is_number(number2.value):
            result.value = "Masukkan input yang valid"
        else:
            result.value = int(number1.value) * int(number2.value)
        page.update()

    def bagi(e):
        if not is_number(number1.value) or not is_number(number2.value):
            result.value = "Masukkan input yang valid"
        else:
            try:
                result.value = float(number1.value) / float(number2.value)
            except ZeroDivisionError:
                result.value = "Tidak bisa dibagi nol"
        page.update()

    # Tombol dalam satu baris
    buttons_row = ft.Row(
        controls=[
            ft.ElevatedButton("Tambah", on_click=add, color="blue", bgcolor="black"),
            ft.ElevatedButton("Kurang", on_click=min, color="yellow", bgcolor="black"),
            ft.ElevatedButton("Kali", on_click=kali, color="green", bgcolor="black"),
            ft.ElevatedButton("Bagi", on_click=bagi, color="red", bgcolor="black")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
    )

    page.add(text, number1, number2, buttons_row, result)

if __name__ == "__main__":
    ft.app(target=main)
