from os.path import join
from bountydns.core.utils import db_dir, load_env
from bountydns.db.session import session, db_register
from bountydns.db.utils import make_db_url
from bountydns.db.migrate.migrate import migrate
from .base import BaseCommand


class AlembicMigrate(BaseCommand):
    name = "alembic-migrate"
    aliases = []
    description = "run alembic migrate"

    @classmethod
    def parser(cls, parser):
        return parser

    def run(self):
        load_env("db")
        db_register("api", make_db_url("api"))
        migrate(join(db_dir("api"), "alembic"))
