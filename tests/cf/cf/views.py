from flask import Blueprint


def create_blueprint_from_app_cf(app):
    """Create  blueprint."""
    if app.config.get("CF_REGISTER_BLUEPRINT", True):
        blueprint = app.extensions["cf"].resource.as_blueprint()
    else:
        blueprint = Blueprint("cf", __name__, url_prefix="/empty/cf")
    blueprint.record_once(init_create_blueprint_from_app_cf)

    # calls record_once for all other functions starting with "init_addons_"
    # https://stackoverflow.com/questions/58785162/how-can-i-call-function-with-string-value-that-equals-to-function-name
    funcs = globals()
    funcs = [
        v for k, v in funcs.items() if k.startswith("init_addons_cf") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint


def init_create_blueprint_from_app_cf(state):
    """Init app."""
    app = state.app
    ext = app.extensions["cf"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(ext.service, service_id="cf")

    # Register indexer
    if hasattr(ext.service, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(ext.service.indexer, indexer_id="cf")
