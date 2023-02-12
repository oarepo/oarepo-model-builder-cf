from cf.records.api import CfRecord
from cf.services.records.permissions import CfPermissionPolicy
from cf.services.records.schema import CfSchema
from cf.services.records.search import CfSearchOptions
from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import RecordServiceConfig
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from invenio_records_resources.services.records.components import DataComponent


class CfServiceConfig(RecordServiceConfig):
    """CfRecord service config."""

    url_prefix = "/cf/"

    permission_policy_cls = CfPermissionPolicy
    schema = CfSchema

    search = CfSearchOptions

    record_cls = CfRecord
    # todo should i leave this here?
    service_id = "cf"

    components = [*RecordServiceConfig.components, DataComponent]

    model = "cf"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
