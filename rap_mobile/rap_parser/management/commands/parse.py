from django.core.management.base import BaseCommand
from rap_parser.management.commands.parser.parser import WebParser


class Command(BaseCommand):
    help = "Site parsing"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of pages for parsing')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        parser = WebParser()
        parser.start_parse(count)
        parser.stop_parse()
