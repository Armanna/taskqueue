import unittest
from dataclasses import dataclass

@dataclass
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int

@dataclass
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_task(self, available_resources: Resources) -> Task:
        # Your implementation to get the highest priority task that satisfies available resources
        pass

class TestTaskQueue(unittest.TestCase):
    def test_add_task(self):
        task_queue = TaskQueue()
        task = Task(id=1, priority=2, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task content", result="")
        task_queue.add_task(task)
        self.assertEqual(len(task_queue.tasks), 1)

    def test_get_task(self):
        task_queue = TaskQueue()
        task1 = Task(id=1, priority=2, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task 1 content", result="")
        task2 = Task(id=2, priority=1, resources=Resources(ram=2, cpu_cores=1, gpu_count=1), content="Task 2 content", result="")
        
        task_queue.add_task(task1)
        task_queue.add_task(task2)

        available_resources = Resources(ram=3, cpu_cores=1, gpu_count=1)
        selected_task = task_queue.get_task(available_resources)

        # Your assertions based on the logic in your get_task method
        # For example:
        self.assertEqual(selected_task.id, 2)

if __name__ == '__main__':
    unittest.main()
