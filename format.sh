black oarepo_model_builder_cf tests --target-version py310
autoflake --in-place --remove-all-unused-imports --recursive oarepo_model_builder_cf tests
isort oarepo_model_builder_cf tests
