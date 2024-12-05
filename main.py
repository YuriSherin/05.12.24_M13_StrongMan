import asyncio


async def start_strongman(name, power):
    """Асинхронная функция, в которой в цикле силач поднимает шары,
    где name - имя силача, power - его подъёмная мощность"""

    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1 / power)  # асинхронный сон. Время сна обратно пропорционально power
        print(f'Силач {name} поднял {str(i + 1)} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    """Основная функция, которая создает задачи и ожидает результат выполнения этих задач"""
    # создаем трех участников соревнования
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await task_1  # ожидание результата
    await task_2  # ожидание результата
    await task_3  # ожидание результата



asyncio.run(start_tournament())  # запуск асинхронной программы на выполнение
