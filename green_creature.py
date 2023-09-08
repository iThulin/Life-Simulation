class GreenCreature(Creature):

    def __init__(self, x_boundary, y_boundary) -> None:
        Creature.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__ (self, other_creature):
        if other_creature.color == (255, 0, 0):
            self.size -= other_creature.size
            other_creature.size -= self.size

        elif other_creature.color == (0, 255, 0):
            self.size += other_creature.size
            other_creature.size = 0

        