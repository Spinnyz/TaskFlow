class Task:
    def __init__ (self, title, description, completed = False):
        self.title = title
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__ (self):
        self.lista = []
    
    def add_task (self, title, description):
        task  = Task(title, description)
        self.lista.append(task)
        return task
    
    def list_tasks(self):
        for indice, tarefa  in enumerate(self.lista):
            status = "Concluida" if tarefa.completed else "Pendente"
            print (f"{indice} - {tarefa.title} - {tarefa.description} - {status}")


