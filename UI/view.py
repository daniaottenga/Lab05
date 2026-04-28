import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.ddCorso = None
        self.btnCercaIscritti = None
        self.txtMatricola = None
        self.txtNome = None
        self.txtCognome = None
        self.btnCercaStudente = None
        self.btnCercaCorsi = None
        self.btnIscrivi = None
        self.txt_result = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddCorso = ft.Dropdown(label = "Selezionare un corso",
                                   width = 400)
        self._controller.fillddCorso()
        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                  on_click=self._controller.handleCercaIscritti)
        row1 = ft.Row([self.ddCorso, self.btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        self.txtMatricola = ft.TextField(
            label="matricola",
            width=100,
        )
        self.txtNome = ft.TextField(
            label="nome",
            width=200,
            read_only=True
        )
        self.txtCognome = ft.TextField(
            label="cognome",
            width=200,
            read_only=True
        )
        row2 = ft.Row([self.txtMatricola, self.txtNome, self.txtCognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                  on_click=self._controller.handleCercaStudente)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi",
                                                  on_click=self._controller.handleCercaCorsi)

        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
