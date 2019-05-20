from bountydns.core.entities.base.repos import BaseRepo
from bountydns.db.models.dns_record import DnsRecord
from bountydns.core.entities.dns_record.data import DnsRecordData


class DnsRecordRepo(BaseRepo):
    default_model = DnsRecord
    default_data_model = DnsRecordData
    default_loads = []
