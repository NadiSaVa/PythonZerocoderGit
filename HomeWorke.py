from datetime import date


class Task:
    def __init__(self, description, deadline):
        """
        Инициализация задачи.

        :param description: Описание задачи
        :param deadline: Срок выполнения задачи (datetime.date)
        """
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        """Отмечаем задачу выполненной."""
        self.completed = True

    def is_overdue(self):
        """Проверяем, просрочена ли задача."""
        today = date.today()
        if not self.completed and today > self.deadline:
            return True
        return False


class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач."""
        self.tasks = []

    def add_task(self, task):
        """Добавляем новую задачу."""
        self.tasks.append(task)

    def list_current_tasks(self):
        """Возвращаем список невыполненных задач."""
        current_tasks = [task for task in self.tasks if not task.completed]
        return current_tasks

    def complete_task_by_description(self, description):
        """Отмечаем задачу выполненной по её описанию."""
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break


def main():
    # Пример использования
    manager = TaskManager()

    # Добавление задач
    task1 = Task("Написать отчет", date(2025, 10, 1))
    task2 = Task("Подготовка презентации", date(2025, 10, 15))
    task3 = Task("Встреча с клиентом", date(2025, 10, 10))

    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)

    # Отметка одной задачи как выполненной
    manager.complete_task_by_description("Написать отчет")

    # Получение текущего списка задач
    current_tasks = manager.list_current_tasks()

    print("\nСписок текущих задач:")
    for idx, task in enumerate(current_tasks, start=1):
        overdue_status = "(Просрочена)" if task.is_overdue() else ""
        print(f"{idx}. {task.description} ({task.deadline.strftime('%d-%m-%Y')}) {overdue_status}")


if __name__ == "__main__":
    main()