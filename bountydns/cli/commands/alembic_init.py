from os.path import join
from bountydns.core.utils import db_dir, load_env
from bountydns.db.session import session, db_register
from bountydns.db.utils import make_db_url
from bountydns.db.migrate.initialize import initialize
from .base import BaseCommand


class AlembicInit(BaseCommand):
    name = "alembic-init"
    aliases = []
    description = "run alembic init"

    @classmethod
    def parser(cls, parser):
        return parser

    def run(self):
        load_env("db")
        db_register("api", make_db_url("api"))
        initialize(join(db_dir("api"), "alembic"))
