from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def clicar(self):
        pass

class Janela(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Cursor(ABC):
    @abstractmethod
    def mover(self):
        pass

class Select(ABC):
    @abstractmethod
    def selecionar(self):
        pass

class Input(ABC):
    @abstractmethod
    def inserir_texto(self):
        pass

# Fábrica abstrata
class FabricaUI(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

    @abstractmethod
    def criar_cursor(self) -> Cursor:
        pass

    @abstractmethod
    def criar_select(self) -> Select:
        pass

    @abstractmethod
    def criar_input(self) -> Input:
        pass


class FabricaWindows(FabricaUI):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

    def criar_cursor(self) -> Cursor:
        return CursorWindows()

    def criar_select(self) -> Select:
        return SelectWindows()

    def criar_input(self) -> Input:
        return InputWindows()

class FabricaMacOS(FabricaUI):
    def criar_botao(self) -> Botao:
        return BotaoMacOS()

    def criar_janela(self) -> Janela:
        return JanelaMacOS()

    def criar_cursor(self) -> Cursor:
        return CursorMacOS()

    def criar_select(self) -> Select:
        return SelectMacOS()

    def criar_input(self) -> Input:
        return InputMacOS()

class BotaoWindows(Botao):
    def clicar(self):
        print("Botão do Windows clicado")

class JanelaWindows(Janela):
    def mostrar(self):
        print("Janela do Windows mostrada")

class CursorWindows(Cursor):
    def mover(self):
        print("Cursor do Windows movido")

class SelectWindows(Select):
    def selecionar(self):
        print("Seleção no Windows realizada")

class InputWindows(Input):
    def inserir_texto(self):
        print("Texto inserido no Windows")


class BotaoMacOS(Botao):
    def clicar(self):
        print("Botão do macOS clicado")

class JanelaMacOS(Janela):
    def mostrar(self):
        print("Janela do macOS mostrada")

class CursorMacOS(Cursor):
    def mover(self):
        print("Cursor do macOS movido")

class SelectMacOS(Select):
    def selecionar(self):
        print("Seleção no macOS realizada")

class InputMacOS(Input):
    def inserir_texto(self):
        print("Texto inserido no macOS")


def criar_fabrica_ui(sistema_operacional: str) -> FabricaUI:
    if sistema_operacional.lower() == "windows":
        return FabricaWindows()
    elif sistema_operacional.lower() == "macos":
        return FabricaMacOS()
    else:
        raise ValueError("Sistema operacional não suportado")


sistema_operacional = "macos"  # Pode ser "windows" ou "macos"
fabrica_ui = criar_fabrica_ui(sistema_operacional)

botao = fabrica_ui.criar_botao()
janela = fabrica_ui.criar_janela()
cursor = fabrica_ui.criar_cursor()
select = fabrica_ui.criar_select()
input_ = fabrica_ui.criar_input()

botao.clicar()
janela.mostrar()
cursor.mover()
select.selecionar()
input_.inserir_texto()
