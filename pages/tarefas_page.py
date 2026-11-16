from playwright.sync_api import Page


class TarefasPage:
    def __init__(self, page: Page):
        self.page = page
        self.campo = page.get_by_role("textbox", name="Nova tarefa")
        self.adicionar = page.get_by_role("button", name="Adicionar")
        self.itens = page.get_by_role("list", name="Tarefas").get_by_role("listitem")

    def abrir(self, url: str):
        self.page.goto(url)

    def criar_tarefa(self, texto: str):
        self.campo.fill(texto)
        self.adicionar.click()
