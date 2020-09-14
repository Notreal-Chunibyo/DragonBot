from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .mottodata import get_lon
import random


@on_command('motto', only_to_me=False, aliases=('语录','名言警句',))
async def motto(session: CommandSession):
    file1 = 'motto\\'
    long_path = 'C:\\Code\\CQP-xiaoi\\酷Q Pro\\data\\image\\'+file1
    things = await get_content(long_path)
    times = random.randint(0, len(things)-1)
    print('[CQ:image,file=motto\\'+things[times][42:]+']')
    await session.send('[CQ:image,file=motto\\'+things[times][42:]+']')


@on_command('moremotto', only_to_me=False, aliases=('语录十连',))
async def moremotto(session: CommandSession):
    file1 = 'motto\\\\'
    long_path = 'C:\\Code\\CQP-xiaoi\\酷Q Pro\\data\\' + 'image\\\\'+file1
    things = await get_content(long_path)
    time1 = [ random.randint(0, len(things)-1) for i in range(10)]
    for times in time1:
        await session.send('[CQ:image,file=motto\\'+things[times][42:]+']')


async def get_content(path):
    lists = get_lon(path, [])
    return lists


@on_natural_language(only_to_me=False,keywords={'治国理政','批话'})
async def _(session: NLPSession):
    return IntentCommand(100.0, 'motto')



