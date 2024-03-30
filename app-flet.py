import flet as ft

def main(page: ft.Page):
    page.title = " Gerenciamento Financeiro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()
ft.app(target=main)