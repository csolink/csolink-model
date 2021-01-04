import unittest

from biolinkml.utils.schemaloader import SchemaLoader

from csolink import CSOLINK_MODEL_YAML


class CsolinkModelTestCase(unittest.TestCase):
    def test_csolink_model(self):
        """ Make sure the csolink model is valid """
        schema = SchemaLoader(CSOLINK_MODEL_YAML)
        errors = []
        try:
            schema.resolve()
        except ValueError as e:
            errors.append(str(e))
        if not errors:
            errors = schema.synopsis.errors()
        self.assertEqual([], errors, "csolink-model.yaml - errors detected")


if __name__ == '__main__':
    unittest.main()
