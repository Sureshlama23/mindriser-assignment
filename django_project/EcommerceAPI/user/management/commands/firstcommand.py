from typing import Any
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):

  # def add_arguments(self, parser):
  #   parser.add_argument('count',type=int,help="How much loop will run") # Positional argument
  #   parser.add_argument('-c','--count',type=int,help="How much loop will run") # Optional arument

  # def handle(self, *args, **kwargs):
  #   count = kwargs['count']
  #   for i in range(count):
  #     self.stdout.write("This is first command")


  # def add_arguments(self, parser):
  #     # parser.add_argument('count',type=int,help="How much loop will run") # Positional argument
  #     # parser.add_argument('-c','--count',type=int,help="How much loop will run") # Optional arument
  #     parser.add_argument('-f','--flag',action='store_true') #flag argument

  # def handle(self, *args, **kwargs):
  #     count = kwargs['count']
  #     flag = kwargs['flag']
  #     if flag:
  #       for i in range(count):
  #         self.stdout.write("This is first command")
  #     else:
  #        self.stdout.write('Flag value is false.')

  
  def add_arguments(self,parser):
    parser.add_argument('count',nargs='+',type=int)

  def handle(self, *args,**options):
    count = options['count']
    print(count)
