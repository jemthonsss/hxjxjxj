#pylint:disable=E0602
#pylint:disable=E0401
#pylint:disable=W0622
#pylint:disable=W0401
from config import *
from telethon import events
from help import *


@youthon.on(events.NewMessage(outgoing=True))
async def _(event):
    id = str(event.sender_id)
    idas = await youthon.get_messages("youthon", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay[0] == 'yes':
        ispay.clear('yes')
        ispay.append("yes")
    elif id not in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("yes")
    else:
        pass

    id = str(event.sender_id)
    idas = await youthon.get_messages("youthoon1", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay2[0] == 'yes':
        ispay2.clear("yes")
        ispay2.append("yes")
    elif id not in msg and ispay2[0] == 'yes':
        ispay2.clear('yes')
        ispay2.append("yes")
    else:
        pass
