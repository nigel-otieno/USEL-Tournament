import random
import math
import copy

class Bracket:
    def __init__(self, teams, rounds=None, lineup=None):
        self.numTeams = len(teams)
        self.teams = list(teams)
        self.max = len(max(["Round "] + teams, key=len))
        self.numRounds = int(math.ceil(math.log(self.numTeams, 2)) + 1)
        self.totalNumTeams = int(2**math.ceil(math.log(self.numTeams, 2)))
        self.totalTeams = self.addTeams()
        self.lineup = lineup if lineup else ["bye" if "-" in str(x) else x for x in self.totalTeams]
        self.numToName()
        self.count = 0
        if rounds:
            self.rounds = rounds
        else:
            self.rounds = []
            for i in range(0, self.numRounds):
                self.rounds.append([])
                for _ in range(0, 2**(self.numRounds - i - 1)):
                    self.rounds[i].append("-" * self.max)
            self.rounds[0] = list(self.totalTeams)

    def numToName(self):
        for i in range(0, self.numTeams):
            self.totalTeams[self.totalTeams.index(i + 1)] = self.teams[i]

    def shuffle(self):
        random.shuffle(self.teams)
        self.totalTeams = self.addTeams()
        self.numToName()
        self.rounds[0] = list(self.totalTeams)

    def update(self, rounds, teams):
        lowercase = [team.lower() for team in self.rounds[rounds - 2]]
        for team in teams:
            try:
                index = lowercase.index(team.lower())
                self.rounds[rounds - 1][int(index / 2)] = self.rounds[rounds - 2][index]
            except:
                return False
        if "-" * self.max in self.rounds[rounds - 1]:
            return False
        return True

    def show(self):
        self.count = 0
        self.temp = copy.deepcopy(self.rounds)
        self.tempLineup = [lineup for lineup in self.lineup if lineup != "bye"]
        output = []
        for i in range(1, self.numRounds + 1):
            output.append(f"Round {i}".rjust(self.max + 3))
        output.append("\n")
        output.extend(self.recurse(self.numRounds - 1, 0))
        return ''.join(output)

    def recurse(self, num, tail):
        output = []
        if num == 0:
            self.count += 1
            if tail == -1:
                if self.tempLineup and self.temp[0]:
                    output.append(self.temp[0].pop(0).rjust(self.max + 3) + " \\\n")
            elif tail == 1:
                if self.tempLineup and self.temp[0]:
                    output.append(self.temp[0].pop(0).rjust(self.max + 3) + " /\n")
        else:
            output.extend(self.recurse(num - 1, -1))
            if tail == -1:
                if self.temp[num]:
                    output.append("".rjust((self.max + 3) * num) + self.temp[num].pop(0).rjust(self.max + 3) + " \\\n")
            elif tail == 1:
                if self.temp[num]:
                    output.append("".rjust((self.max + 3) * num) + self.temp[num].pop(0).rjust(self.max + 3) + " /\n")
            else:
                if self.temp[num]:
                    output.append("".rjust((self.max + 3) * num) + self.temp[num].pop(0).rjust(self.max + 3) + "\n")
            output.extend(self.recurse(num - 1, 1))
        return output

    def addTeams(self):
        x = self.numTeams
        teams = [1]
        temp = []
        count = 0
        for i in range(2, x + 1):
            temp.append(i)
        for i in range(0, int(2**math.ceil(math.log(x, 2)) - x)):
            temp.append("-" * self.max)
        for _ in range(0, int(math.ceil(math.log(x, 2)))):
            high = max(teams)
            for i in range(0, len(teams)):
                index = teams.index(high) + 1
                teams.insert(index, temp[count])
                high -= 1
                count += 1
        return teams
