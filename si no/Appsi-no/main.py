import flet as ft


def main(page: ft.Page):
    page.title = "¿me perdonas?"
    page.bgcolor="pink"
    page.horizontal_aligment=ft.CrossAxisAlignment.center()
    page.vertical_aligment=ft.MainAxisAlignment.CENTER
    
    lbl1 = ft.text("¿me perdonas?",
                    style=fty.textStyle(size=40,veight="bold"))
    img1=ft.image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("si",
                            color="green",
                            width=100,
                            height=50
                            )
    page.add(
        ft.column(
            (
                lbl1,
                img1,
                ft.Row(
                    (btnSi,btnNo)
                )
            )
        )
    )


ft.app(main)
