from cf.records.dumper import CfDumper
from cf.records.models import CfMetadata
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.dumpers import CustomFieldsDumperExt
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_runtime.cf import CustomFields, InlinedCustomFields


class CfRecord(Record):
    model_cls = CfMetadata

    schema = ConstantField("$schema", "local://cf-1.0.0.json")

    index = IndexField("cf-cf-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = [
        CustomFieldsDumperExt("TEST_CUSTOM_FIELDS"),
        CustomFieldsDumperExt("INLINE_CUSTOM_FIELDS"),
    ]
    dumper = CfDumper(extensions=dumper_extensions)

    custom_fields = CustomFields(
        "TEST_CUSTOM_FIELDS",
        "custom_fields",
        clear_none=True,
        create_if_missing=True,
    )

    inlined_custom_fields = InlinedCustomFields("INLINE_CUSTOM_FIELDS")
