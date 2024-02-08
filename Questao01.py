class Configuracao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tema = "claro"
            cls._instance.idioma = "português"
            cls._instance.tamanho_fonte = 12
        return cls._instance

    def alterar_configuracao(self, tema=None, idioma=None, tamanho_fonte=None):
        if tema:
            self.tema = tema
        if idioma:
            self.idioma = idioma
        if tamanho_fonte:
            self.tamanho_fonte = tamanho_fonte

    def acessar_configuracao(self):
        return {
            "tema": self.tema,
            "idioma": self.idioma,
            "tamanho_fonte": self.tamanho_fonte
        }


config = Configuracao()
print(config.acessar_configuracao())  

config.alterar_configuracao(tema="escuro", tamanho_fonte=14)
print(config.acessar_configuracao())  


config2 = Configuracao()
print(config2.acessar_configuracao())  
print(config is config2) 
