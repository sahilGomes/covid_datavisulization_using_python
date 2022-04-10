from Home_Window import CreateHome_Window

class mainClass(CreateHome_Window):
    def __init__(self) -> None:
        self.home_obj = CreateHome_Window()

mainClass_obj = mainClass()