from abc import ABC, abstractmethod

class ILog(ABC):
    @abstractmethod
    def registrar(self, msg: str):
        pass

class LogArquivo(ILog):
    def registrar(self, msg: str):
        with open("log.txt", "a") as arquivo:
            arquivo.write(msg + "\n")
        print("Log registrado em arquivo")

class LogConsole(ILog):
    def registrar(self, msg: str):
        print("Log:", msg)


class LogBancoDeDados(ILog):
    def registrar(self, msg: str):
     
        print("Log registrado no banco de dados")


class FabricaLog:
    def criar_log(self, tipo: str) -> ILog:
        if tipo == "arquivo":
            return LogArquivo()
        elif tipo == "console":
            return LogConsole()
        elif tipo == "banco":
            return LogBancoDeDados()
        else:
            raise ValueError("Tipo de log inválido")


fabrica = FabricaLog()


log_arquivo = fabrica.criar_log("arquivo")
log_arquivo.registrar("Mensagem de log em arquivo")

log_console = fabrica.criar_log("console")
log_console.registrar("Mensagem de log no console")

log_banco = fabrica.criar_log("banco")
log_banco.registrar("Mensagem de log no banco de dados")
