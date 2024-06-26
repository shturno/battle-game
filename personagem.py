class Personagem:
    def __init__(self, nome, vida, nivel, ataque, defesa):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        self.__ataque = ataque
        self.__defesa = defesa

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def get_ataque(self):
        return self.__ataque

    def get_defesa(self):
        return self.__defesa

    def set_nome(self, nome):
        self.__nome = nome

    def set_vida(self, vida):
        self.__vida = vida

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_ataque(self, ataque):
        self.__ataque = ataque

    def set_defesa(self, defesa):
        self.__defesa = defesa
