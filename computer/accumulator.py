from utils.logger import logger

class Accumulator:
    def __init__(self):
        self.value = 0  # The accumulator starts with a value of 0

    def load(self, value):
        # Loads a new value into the accumulator
        self.value = value

    def read(self):
        # Returns the current value of the accumulator
        return self.value

    def write(self, value):
        # Updates the accumulator with the given value
        self.load(value)  # Same as load in this case, can be different based on architecture

    def clear(self):
        # Resets the accumulator to 0
        self.value = 0

if __name__ == "__main__":
    acc = Accumulator()
    acc.load(10)  # Charge la valeur 10 dans l'accumulateur
    logger.info(acc.read())  # Affiche la valeur actuelle de l'accumulateur
    acc.clear()  # Réinitialise l'accumulateur
    logger.info(acc.read())  # Affiche la valeur réinitialisée de l'accumulateur
