from abc import ABC, abstractmethod

class RenderizadorTextura(ABC):
    @abstractmethod
    def renderizar_textura(self, textura):
        pass

class RenderizadorSombra(ABC):
    @abstractmethod
    def renderizar_sombra(self, sombra):
        pass

class RenderizadorModelo(ABC):
    @abstractmethod
    def renderizar_modelo(self, modelo):
        pass


class FabricaRenderizacao(ABC):
    @abstractmethod
    def criar_renderizador_textura(self) -> RenderizadorTextura:
        pass

    @abstractmethod
    def criar_renderizador_sombra(self) -> RenderizadorSombra:
        pass

    @abstractmethod
    def criar_renderizador_modelo(self) -> RenderizadorModelo:
        pass


class FabricaOpenGL(FabricaRenderizacao):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def criar_renderizador_textura(self) -> RenderizadorTextura:
        return RenderizadorTexturaOpenGL()

    def criar_renderizador_sombra(self) -> RenderizadorSombra:
        return RenderizadorSombraOpenGL()

    def criar_renderizador_modelo(self) -> RenderizadorModelo:
        return RenderizadorModeloOpenGL()


class FabricaDirectX(FabricaRenderizacao):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def criar_renderizador_textura(self) -> RenderizadorTextura:
        return RenderizadorTexturaDirectX()

    def criar_renderizador_sombra(self) -> RenderizadorSombra:
        return RenderizadorSombraDirectX()

    def criar_renderizador_modelo(self) -> RenderizadorModelo:
        return RenderizadorModeloDirectX()


class RenderizadorTexturaOpenGL(RenderizadorTextura):
    def renderizar_textura(self, textura):
        print("Renderizando textura com OpenGL")

class RenderizadorSombraOpenGL(RenderizadorSombra):
    def renderizar_sombra(self, sombra):
        print("Renderizando sombra com OpenGL")

class RenderizadorModeloOpenGL(RenderizadorModelo):
    def renderizar_modelo(self, modelo):
        print("Renderizando modelo com OpenGL")

class RenderizadorTexturaDirectX(RenderizadorTextura):
    def renderizar_textura(self, textura):
        print("Renderizando textura com DirectX")

class RenderizadorSombraDirectX(RenderizadorSombra):
    def renderizar_sombra(self, sombra):
        print("Renderizando sombra com DirectX")

class RenderizadorModeloDirectX(RenderizadorModelo):
    def renderizar_modelo(self, modelo):
        print("Renderizando modelo com DirectX")


def criar_fabrica_renderizacao(biblioteca_grafica: str) -> FabricaRenderizacao:
    if biblioteca_grafica.lower() == "opengl":
        return FabricaOpenGL()
    elif biblioteca_grafica.lower() == "directx":
        return FabricaDirectX()
    else:
        raise ValueError("Biblioteca gráfica não suportada")


biblioteca_grafica = "opengl"  #
fabrica_renderizacao = criar_fabrica_renderizacao(biblioteca_grafica)


renderizador_textura = fabrica_renderizacao.criar_renderizador_textura()
renderizador_textura.renderizar_textura("textura.png")

renderizador_sombra = fabrica_renderizacao.criar_renderizador_sombra()
renderizador_sombra.renderizar_sombra("sombra.png")

renderizador_modelo = fabrica_renderizacao.criar_renderizador_modelo()
renderizador_modelo.renderizar_modelo("modelo.obj")
