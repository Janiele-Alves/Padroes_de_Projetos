class Configuracao:
    _instance = None

    def __new__(clas):
        if clas._instance is None:
            clas._instance = super().__new__(clas)
            clas._instance.tema = "claro"
            clas._instance.idioma = "português"
            clas._instance.fonte = 12
        return clas._instance

    def alterar_configuracao(self, tema=None, idioma=None, fonte=None):
        if tema:
            self.tema = tema
        if idioma:
            self.idioma = idioma
        if fonte:
            self.fonte = fonte

    def acessar_configuracao(self):
        return {
            "tema": self.tema,
            "idioma": self.idioma,
            "fonte": self.fonte
        }


config = Configuracao()
print(config.acessar_configuracao())  

config.alterar_configuracao(tema="escuro", fonte=14)
print(config.acessar_configuracao())  


conf = Configuracao()
print(conf.acessar_configuracao())  
print(config is conf) 
