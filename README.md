# Battle Game between Heroes and Villains
This is a simple battle game where heroes face villains in epic combats. The game is developed in Python and uses object-oriented programming concepts to model characters and their interactions.

## Features
- Add Characters: Allows creation of heroes and villains with different attributes such as name, health, level, attack, defense, and special abilities.
- Battle: Characters can attack, defend, use special abilities, and even flee from battle depending on player choices.
- Score Keeping: The game keeps track of characters' scores as they participate in battles.

## How to Play
1. Choose Your Hero: At the start, the player can choose which hero to control during battles.
2. Battle: The game presents available options for each round of battle, such as attack, use special attack, defend, or flee.
3. Victory or Defeat: The battle continues until one character runs out of health. The player wins if the hero defeats all villains, and vice versa.

## System Requirements
- Python 3.x installed
- personagem.py module that defines the Personagem class and its subclasses Heroi and Vilao.
- How to Run
- Clone the repository to your local machine: ```git clone https://github.com/your-username/repository-name.git```

## Creating characters
```hero = Heroi('Aragorn', 100, 1, 10, 5, 'Double Attack')```
```villain = Vilao('Orc', 100, 1, 10, 5, 'Warrior', 'Double Attack')```

## Starting the game
```game = Jogo(hero, villain)```
```game.start_battle()```

## Contributions
Contributions are welcome! Feel free to submit pull requests with improvements or fixes.

## Author
Gabriela Alvarenga
gabrielasalvarenga2@gmail.com
