from django.core.management.base import BaseCommand, CommandError

from symposion.schedule.models import Room, Slot, SlotRoom

class Command(BaseCommand):
    help = 'Adds all rooms to all schedule slots.'

    def handle(self, *args, **options):
        for slot in Slot.objects.all():
            for room in Room.objects.all():
                SlotRoom.objects.get_or_create(slot=slot, room=room)
