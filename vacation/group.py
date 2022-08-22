
class Group():

    def __init__(self, group_id: int):
        self.id = str(group_id)
        self.produces = []

    def __str__(self):
        return f"Group {self.id}"
