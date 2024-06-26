import random
from personagem import Personagem


def exibir_detalhes(personagem):
    return f"Nome: {personagem.get_nome()}\nVida: {personagem.get_vida()}\nNivel: {personagem.get_nivel()}\nAtaque: {personagem.get_ataque()}\nDefesa: {personagem.get_defesa()}\nTem a habilidade especial: {personagem.get_habilidade_especial()}"


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, ataque, defesa):
        super().__init__(nome, vida, nivel, ataque, defesa)
        self.__habilidade_especial = None
        self.pontos = 0

    def set_habilidade_especial(self, habilidade_especial):
        self.__habilidade_especial = habilidade_especial

    def get_habilidade_especial(self):
        return self.__habilidade_especial
    
    def atacar(self, inimigo):
        inimigo.set_vida(inimigo.get_vida() - self.get_ataque())
        print(f'{self.get_nome()} atacou {inimigo.get_nome()} com {self.get_ataque()} de ataque.')
        print(f'{inimigo.get_nome()} agora tem {inimigo.get_vida()} de vida.')
        self.pontos += 1
        print(f'{self.get_nome()} agora tem {self.pontos} pontos.')

    def defender(self, inimigo):
        dano = max(0, inimigo.get_ataque() - self.get_defesa())
        self.set_vida(self.get_vida() - dano)
        print(f'{self.get_nome()} defendeu o ataque de {inimigo.get_nome()}.')
        print(f'{self.get_nome()} agora tem {self.get_vida()} de vida.')

    def fugir(self):
        print(f'{self.get_nome()} fugiu da batalha.')
        print(f'{self.get_nome()} agora tem {self.get_vida()} de vida.')

    def __str__(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nAtaque: {self.get_ataque()}\nDefesa: {self.get_defesa()}\nPontos: {self.pontos}'


class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, ataque, defesa, tipo, habilidade_especial):
        super().__init__(nome, vida, nivel, ataque, defesa)
        self.__habilidade_especial = habilidade_especial
        self.__tipo = tipo
        self.pontos = 0

    def get_habilidade_especial(self):
        return self.__habilidade_especial

    def get_tipo(self):
        return self.__tipo

    def atacar(self, inimigo):
        inimigo.set_vida(inimigo.get_vida() - self.get_ataque())
        print(f'{self.get_nome()} atacou {inimigo.get_nome()} com {self.get_ataque()} de ataque.')
        print(f'{inimigo.get_nome()} agora tem {inimigo.get_vida()} de vida.')

    def defender(self, inimigo):
        dano = max(0, inimigo.get_ataque() - self.get_defesa())
        self.set_vida(self.get_vida() - dano)
        print(f'{self.get_nome()} defendeu o ataque de {inimigo.get_nome()}.')
        print(f'{self.get_nome()} agora tem {self.get_vida()} de vida.')
    

class Jogo:

    def __init__(self):
        self.herois = [
            Heroi('Aragorn', 100, 1, 10, 5),
            Heroi('Legolas', 80, 2, 8, 3),
            Heroi('Gandalf', 120, 3, 12, 6),
        ]
        
        self.viloes = [
            Vilao('Orc', 100, 1, 10, 5, 'Guerreiro', 'Ataque Duplo'),
            Vilao('Troll', 150, 2, 15, 8, 'Brutamontes', 'Impacto Poderoso'),
            Vilao('Goblin', 80, 1, 8, 3, 'Ladrão', 'Agilidade Sinistra'),
        ]

    def iniciar_batalha(self):
        heroi = random.choice(self.herois)
        vilao = random.choice(self.viloes)
        
        print("A batalha começou!")
        print(f'{heroi.get_nome()} vs {vilao.get_nome()}')
        
        while heroi.get_vida() > 0 and vilao.get_vida() > 0:
            print("\nDetalhes dos personagens")
            print(exibir_detalhes(heroi))
            print(exibir_detalhes(vilao))

            input('Pressione Enter para continuar...')
            escolha = input('Escolha a ação:\n1 - Atacar\n2 - Ataque Especial \n3 - Defender\n4 - Fugir\n')
            if escolha == '1':
                heroi.atacar(vilao)
                vilao.defender(heroi)
                if vilao.get_vida() <= 0:
                    print(f'{heroi.get_nome()} venceu a batalha!')
                    break
                vilao.atacar(heroi)
                heroi.defender(vilao)
                if heroi.get_vida() <= 0:
                    print(f'{vilao.get_nome()} venceu a batalha!')
                    break
            elif escolha == '2':
                heroi.atacar(vilao)
                vilao.defender(heroi)
                if vilao.get_vida() <= 0:
                    print(f'{heroi.get_nome()} venceu a batalha!')
                    break
                vilao.atacar(heroi)
                heroi.defender(vilao)
                if heroi.get_vida() <= 0:
                    print(f'{vilao.get_nome()} venceu a batalha!')
                    break
            elif escolha == '3':
                heroi.defender(vilao)
                vilao.atacar(heroi)
                heroi.defender(vilao)
                if heroi.get_vida() <= 0:
                    print(f'{vilao.get_nome()} venceu a batalha!')
                    break
            elif escolha == '4':
                heroi.fugir()
                break
            else:
                print('Opção inválida!')
            heroi.atacar(vilao)
            vilao.defender(heroi)
            if vilao.get_vida() <= 0:
                print(f'Você({heroi.get_nome()}) venceu a batalha!')
                break
            vilao.atacar(heroi)
            heroi.defender(vilao)
            if heroi.get_vida() <= 0:
                print(f'{vilao.get_nome()} venceu a batalha!')
                break

jogo = Jogo()
jogo.iniciar_batalha()
