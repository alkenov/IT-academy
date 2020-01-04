#!python3
#-*-encoding:utf-8-*-


class Warrior:
    experience = 10
    level = 1
    achievements = []

    def battle(self, enemy_level):
        self.enemy_level = enemy_level
        if self.level < 1 or 100 < self.level:
            return 'Invalid Level'
        elif self.enemy_level < 1 or 100 < self.enemy_level:
            return 'Invalid battle'
        elif self.level == self.enemy_level:
            self.experience += 10
            return 'A good fight'
        elif self.level == self.enemy_level + 1:
            self.experience += 5
            return 'A good fight'
        elif self.level > self.enemy_level + 1:
            self.experience += 0
            return 'Easy fight'
        elif self.enemy_level - 4 <= self.level < self.enemy_level:
            diff = self.enemy_level - self.level
            self.experience += 20 * diff * diff
            return 'Inspiration in fight'
        else:
            self.experience += 0
            return "You've been defeated"


    def training(self, training):
        self.training = training
        if self.level < 1 or 100 < self.level:
            return "Invalid level"
        elif self.training[2] <= self.level:
            self.experience = self.experience + self.training[1]
            if self.experience > 100:
                self.experience = 100
            self.level = int(self.experience // 10)
            self.achievements.append(self.training[0])
            return  self.training[0]
        else:
            return "Not strong enough"


    @property
    def rank(self):
        if self.level <= 9:
            rank = 'Pushover'
        elif 10 <= self.level <= 19:
            rank = 'Novice'
        elif 20 <= self.level <= 29:
            rank = 'Fighter'
        elif 30 <= self.level <= 39:
            rank = 'Warrior'
        elif 40 <= self.level <= 49:
            rank = 'Veteran'
        elif 50 <= self.level <= 59:
            rank = 'Champion'
        elif 60 <= self.level <= 69:
            rank = 'Sage'
        elif 70 <= self.level <= 79:
            rank = 'Elite'
        elif 80 <= self.level <= 89:
            rank = 'Conqueror'
        elif 90 <= self.level <= 99:
            rank = 'Master'
        elif self.level == 100:
            rank = 'Greatest'
        else:
            rank = 'Invalid level'
        return rank



if __name__ == "__main__":
    Witcher = Warrior()
    print(Witcher.level)
    print(Witcher.experience)
    print(Witcher.rank)
    print(Witcher.achievements)
    print(Witcher.training(["Defeated Dragon", 90, 1]))
    print(Witcher.experience)
    print(Witcher.level)
    print(Witcher.rank)
    print(Witcher.battle(90))
    print(Witcher.experience)
    print(Witcher.achievements)
