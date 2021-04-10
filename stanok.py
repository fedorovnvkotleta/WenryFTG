from .. import loader
from asyncio import sleep
@loader.tds
class StanokMod(loader.Module):
	strings = {"name": "stanok"}
	@loader.owner
	async def wenrycmd(self, message):
		for _ in range(10):
			for heart in ['венри', '️хелси', 'норка', 'боуз', 'молик', 'вейв', 'прокод', 'ачё', 'ладскер', 'фантик', 'заново ебать']:
				await message.edit(stanok)
				await sleep(0.2)
