import random


class Building:

    def random_selection_from_list(value):
        """Функция выбирает из списка рандомное значение

        Args:
            value ([list]): [список из которого будут рандомиться значения]
        """
        return random.choice(value)
