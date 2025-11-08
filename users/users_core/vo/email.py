class Email:
    value: str

    def __init__(self, value: str):
        if value.find('@') < 0:
            raise Exception

        self.value = value

