"""
Monkeypatching the Slot model to make handling the Presentaiton admin easier.

"""
from symposion.schedule.models import Slot


def slot_unicode(self):
    try:
        room = self.rooms[0]
    except IndexError:
        room = 'n/a'
    return "%s %s (%s - %s) [%s]" % (
        self.day, self.kind, self.start, self.end, room)


Slot.__unicode__ = slot_unicode
