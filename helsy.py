from .. import loader
from asyncio import sleep
@loader.tds
class HelsyMod(loader.Module):
	strings = {"name": "helsyfan"}
	@loader.owner
	async def helsycmd(self, message):
		for _ in range(10):
			for helsy in ['хелси пмт', '️хелси топ', 'хелси лучший', 'хелси топ', 'хелси моддир 228', '❤', '💙', '❤', '💙', '❤', '💙']:
				await message.edit(helsy)
				await sleep(0.4)
