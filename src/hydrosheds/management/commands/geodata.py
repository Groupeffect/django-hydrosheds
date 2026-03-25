from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os
from django.contrib.gis.utils import LayerMapping
from hydrosheds.db import models, core
from django.utils.text import get_valid_filename

default_name = "ChangeMeModel"


def name_validator(name):
    """Ensure name has no space"""
    try:
        _name = get_valid_filename(name)
        if name != _name:
            raise ValidationError(f"name contains invalid characters, try {_name}")
    except Exception as e:
        raise e


def write_ogrinspect_model(options):
    """ogrinspect wrapper"""
    name = options["name"]
    name_validator(name)
    return call_command(
        "ogrinspect",
        f"{options["file"]}",
        name,
        "--mapping",
        f"--srid={options["srid"]}",
        f"--geom-name",
        f"{options["geom"]}",
    )


def import_dataset_from_shape_file(options):
    name = options["name"]
    file = options["file"]
    if not file or not os.path.exists(file):
        raise CommandError("Set existing --file path.")
    if not name or options["name"] in [default_name]:
        raise CommandError("Set --name model.")
    model = getattr(models, name)
    if not model:
        raise CommandError(f"Model {name} in ontology not found.")
    lm = LayerMapping(model, file, getattr(core, f"{name}_mapping"), transform=False)
    lm.save(strict=True, verbose=True)
    return [options, lm]


class Command(BaseCommand):
    help = """
    Write Model with ogrinspect. Example:
    >>> python manage.py geodata -f data-sets/HydroRIVERS/HydroRIVERS_v10_af_shp/HydroRIVERS_v10_af.shp -n HydroRiver
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "-l",
            "--load",
            action="store_true",
            help="load file data to database model",
        )
        parser.add_argument(
            "-f",
            "--file",
            required=False,
            type=str,
            default=None,
            help="set file path [*.shp] ",
        )
        parser.add_argument(
            "-n",
            "--name",
            default=default_name,
            required=False,
            type=str,
            help="model name",
        )
        parser.add_argument("-s", "--srid", default=4326, required=False, type=str)
        parser.add_argument(
            "-g",
            "--geom",
            required=False,
            default="geom",
            type=str,
            help="geometry field of input file",
        )

    def handle(self, *args, **options):
        if options["load"] is not False:
            r = import_dataset_from_shape_file(options)
            self.stdout.write(self.style.SUCCESS(f"{r}"))

        elif options["file"]:
            write_ogrinspect_model(options)

        else:
            call_command("geodata", "--help")
