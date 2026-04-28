import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillddCorso(self):
        for c in self._model.getAllCorsi():
            self._view.ddCorso.options.append(ft.dropdown.Option(
                key = c.codins,
                text = c.__str__()
            ))


    def handleCercaIscritti(self, e):
        self._view.txt_result.controls.clear()
        corso = self._view.ddCorso.value

        if corso is None:
            (self._view.create_alert
             ("Attenzione, selezionare un periodo didattico."))
            self._view.update_page()
            return

        matricole = self._model.getIscritti(corso)
        iscritti = []
        for matricola in matricole:
            iscritti.append(self._model.getStudente(matricola))

        if not len(iscritti):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun iscritto trovato per il corso {corso}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito gli iscritti del corso {corso}:"))
        for c in iscritti:
            self._view.txt_result.controls.append(
                ft.Text(c)
            )
        self._view.update_page()


    def handleCercaStudente(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view.txtMatricola.value

        if matricola is None:
            (self._view.create_alert
             ("Attenzione, inserire una matricola"))
            self._view.update_page()
            return

        studente = self._model.getStudente(matricola)

        if not studente:
            self._view.txt_result.controls.append(
                ft.Text(f"Nessuno studente trovato con la matricola {matricola}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Studente con la matricola {matricola}:"))
        self._view.txt_result.controls.append(ft.Text(studente))
        self._view.txtNome.value = studente.nome
        self._view.txtCognome.value = studente.cognome
        self._view.update_page()


    def handleCercaCorsi(self, e):
        self._view.txt_result.controls.clear()
        matricola = self._view.txtMatricola.value

        if matricola is None:
            (self._view.create_alert
             ("Attenzione, inserire una matricola"))
            self._view.update_page()
            return

        corsi = self._model.getCorsi(matricola)

        if not len(corsi):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun corso trovato per la matricola {matricola}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i corsi frequentati dalla matricola {matricola}:"))
        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(c)
            )
        self._view.update_page()

