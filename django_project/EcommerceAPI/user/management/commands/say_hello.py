from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = "This is custom command test"

  def handle(self,*args, **kwargs):
    self.stdout.write("Hello this custom command")