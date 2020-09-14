from nonebot import on_command, CommandSession


@on_command('gameres', only_to_me=False, aliases=('help',))
async def gameres(session: CommandSession):
    res = '改进了上传图片的方式\n输入"上传图片"后，就可以依次发送单张图片，bot如果回复"继续"则说明上传成功，此时就可以继续上传\n想要结束上传，输入"结束"即可结束上传'
    await session.send(res)
