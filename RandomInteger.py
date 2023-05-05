from .. import loader, utils
import random as rd
__version__ = (1, 1, 0)
@loader.tds
class RandomInteger(loader.Module):
    strings = {
        "name": "RandomInteger",
    }
    def rdint_core(self, message):
        Random = message.message.split(" ")
        Integers = rd.randint(int(Random[1]), int(Random[2]))
        return (
            f'<i>Рандомное число:</i> <b>{Integers}</b>'
        )
    @loader.command()
    async def rdint(self, message):
        """- Выводит рандомное число (параметры)"""
        await utils.answer(message, self.rdint_core(message))