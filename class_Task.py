#Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

from datetime import datetime

class Task:
    def __init__(self, description, date):
        self.description = description
        self.date = date
        self.status = False
    def completed(self):
        self.status = True

class Tasks:
    def __init__(self):
        self.tasks = []
    def new(self, description, date):
        task = Task(description, date)
        self.tasks.append(task)
    def completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.completed()
                break
    def actual(self):
        return [task.description for task in self.tasks if not task.status]
    def view(self):
        return "\n".join(str(task.description) for task in self.tasks)


TaskManager = Tasks()
TaskManager.new("Разработка", "2025-01-31")
TaskManager.new("Презентация", "2025-02-25")
TaskManager.new("Компенсация", "2025-03-25")
TaskManager.completed("Разработка")

print("Все задачи:", "\n", TaskManager.view())
print("Актуальные задачи:", TaskManager.actual())



t1 = Task("Проснуться в 6", "26.01.2025")