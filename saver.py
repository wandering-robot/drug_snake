
class Saver:

    def __init__(self,list_len=10):
        self.data = []
        self.get_highscores()
        
        self.i = None   #for inserting new score
        self.list_len = list_len

    @staticmethod
    def get_path(file_name):            #might not need this part
        abs_path = pathlib.Path(__file__).parent.absolute()
        complete_name = os.path.join(abs_path,'leaderboard',file_name+'.txt')
        return complete_name

    def get_highscores(self):
        with open('leaderboard') as names:
            for line in names:
                name,score = line.strip().split(':')
                self.data.append((name,int(score)))

    def check_if_highscore(self,results):
        for i in range(len(self.data)):
            if results > self.data[i][1]:
                self.i = i
                return i
        return None
            
    def update_highscores(self,results):
        for score in self.data:
            if results > score[1]:
                print("\n***\tHigh Score!\t***\n")
                name = self.get_player_name()
                self.data.insert(self.i,(name,results))
                self.display()
                break
            self.data = self.data[:9]

    def get_player_name(self):
        name = input("NAME: ")
        invalid = True
        while invalid:
            if type(name) != str:
                print('Invalid Name\n')
            elif len(name) != 3:
                print('3 Characters\n')
            else:
                break
            name = input("NAME: ")
        return name.upper()

    def write_2_file(self):
        with open('leaderboard','w') as saved:
            for result in self.data:
                name,score = result
                saved.write(f'{name}:{score}\n')

    def display(self):
        for line in self.data:
            name,score = line
            print(f'{name}...{score}')

    def reset_scores(self):
        with open('leaderboard','w') as saved:
            for i in range(self.list_len):
                saved.write('AAA:000\n')

    def end_game(self,result):
        highscore = False
        self.check_if_highscore(result)
        if self.i != None:
            self.update_highscores(result)
            highscore = True
        self.write_2_file()
        if not highscore:
            self.display()

if __name__ == "__main__":

    saver = Saver()

    saver.reset_scores()
