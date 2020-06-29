from locatable import Locatable


class Teacher(Locatable):

    def __init__(self, id, pos, allocated=False):
        super(Teacher, self).__init__(id, pos)
        self.allocated = allocated
        

    def print_t(self):
        print(f"i am a teacher:{self.id} my location {self.pos}")
