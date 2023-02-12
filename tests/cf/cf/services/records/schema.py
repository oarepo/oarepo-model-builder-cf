from functools import partial

import marshmallow as ma
from invenio_records_resources.services.custom_fields import CustomFieldsSchema
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import ValidationError
from marshmallow import fields as ma_fields
from marshmallow import validates as ma_validates
from marshmallow_utils import fields as mu_fields
from marshmallow_utils import schemas as mu_schemas
from marshmallow_utils.fields import NestedAttribute
from oarepo_runtime.cf import InlinedCustomFieldsSchemaMixin
from oarepo_runtime.validation import validate_date


class CfMetadataSchema(ma.Schema):
    """CfMetadataSchema schema."""

    title = ma_fields.String()


class CfSchema(InlinedCustomFieldsSchemaMixin, InvenioBaseRecordSchema):
    """CfSchema schema."""

    CUSTOM_FIELDS_VAR = "INLINE_CUSTOM_FIELDS"
    metadata = ma_fields.Nested(lambda: CfMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y:%m:%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y:%m:%d")], dump_only=True)
    custom_fields = NestedAttribute(
        partial(CustomFieldsSchema, fields_var="TEST_CUSTOM_FIELDS")
    )
