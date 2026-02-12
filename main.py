class Task:
    def __init__ (self, title, description, complete = False):
        self.title = title
        self.description = description
        self.complete = complete

class TaskManager:
    def __init__ (self):
        self.lista = []
    
    def add_task (self, title, description):
        task  = Task(title, description)
        self.lista.append(task)

t1 = Task("Pyhton", "lala", True)
print (t1.title)
print (t1.description)
print (t1.complete)