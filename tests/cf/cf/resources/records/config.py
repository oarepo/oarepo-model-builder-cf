import importlib_metadata
from invenio_records_resources.resources import RecordResourceConfig


class CfResourceConfig(RecordResourceConfig):
    """CfRecord resource config."""

    blueprint_name = "Cf"
    url_prefix = "/cf/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(group="invenio.cf.response_handlers"):
            entrypoint_response_handlers.update(x.load())
        return {**super().response_handlers, **entrypoint_response_handlers}
