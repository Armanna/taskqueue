import pytest
from taskqueue import TaskQueue, Task, Resources

@pytest.fixture
def task_queue():
    return TaskQueue()

def test_add_task(task_queue):
    task = Task(id=1, priority=2, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task content", result="")
    task_queue.add_task(task)
    assert len(task_queue.tasks) == 1

def test_get_task(task_queue):
    task1 = Task(id=1, priority=2, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task 1 content", result="")
    task2 = Task(id=2, priority=1, resources=Resources(ram=2, cpu_cores=1, gpu_count=1), content="Task 2 content", result="")
    
    task_queue.add_task(task1)
    task_queue.add_task(task2)

    available_resources = Resources(ram=3, cpu_cores=1, gpu_count=1)
    selected_task = task_queue.get_task(available_resources)

    # Your assertions based on the logic in your get_task method
    # For example:
    assert selected_task.id == 2
