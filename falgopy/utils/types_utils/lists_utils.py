class ListUtils:

    @staticmethod
    def swap_items(lst: list, i: int, j: int):
        lst[i], lst[j] = lst[j], lst[i]
