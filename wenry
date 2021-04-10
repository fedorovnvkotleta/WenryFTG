from .. import loader
from asyncio import sleep
@loader.tds
class WenryMod(loader.Module):
	strings = {"name": "wenry"}
	@loader.owner
	async def wenrycmd(self, message):
		for _ in range(10):
			for heart in ['начинается самоотсос', '️венри делает самоотсос онлайн', 'венри лучший', 'венри топ', 'самоотсос кончился', 'венри гандон']:
				await message.edit(heart)
				await sleep(0.4)
