class Task:
    def __init__ (self, title, description, complete = False):
        self.title = title
        self.description = description
        self.complete = complete

class TaskManager:
    def __init__ (self):
        self.lista = []
    
    def add_task (self, title, description):
        lista  = Task(title, description)
        self.append(lista)