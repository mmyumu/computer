from utils.logger import logger

class ProgramCounter:
    def __init__(self):
        self.counter = 0

    def get(self):
        return self.counter

    def set(self, value):
        self.counter = value

    def increment(self):
        self.counter += 1

if __name__ == "__main__":
    # Exemple d'utilisation
    pc = ProgramCounter()
    logger.info(pc.get())  # Affiche 0
    pc.increment()
    logger.info(pc.get())  # Affiche 1
    pc.set(10)
    logger.info(pc.get())  # Affiche 10