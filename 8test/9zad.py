class main:

    def __init__(self):
        self.state = 'A'

    def cast(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'C'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise KeyError()

    def stash(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'D'
            return 8
        elif self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'D':
            self.state = 'D'
            return 6
        else:
            raise KeyError()

    def main(self):
        return main()