# Csolink model file locations
import os

basedir = os.path.abspath(os.path.join(__file__, '..', '..'))
CSOLINK_MODEL_YAML = os.path.join(basedir, 'csolink-model.yaml')
CSOLINK_MODEL_JSONLD = os.path.join(basedir, 'context.jsonld')
CSOLINK_MODEL_SHEX = os.path.join(basedir, 'shex', 'csolink-model.shex')
CSOLINK_MODEL_RDF = os.path.join(basedir, 'rdf', 'csolink-model.ttl')
CSOLINK_MODEL_OWL = os.path.join(basedir, 'ontology', 'csolink-model.owl')
CSOLINK_MODEL_JSON = os.path.join(basedir, 'csolink-model.json')
CSOLINK_MODEL_JSON_SCHEMA = os.path.join(basedir, 'json-schema', 'csolink-model.json')
CSOLINK_MODEL_JAVA = os.path.join(basedir, 'java')
CSOLINK_MODEL_PYTHON = os.path.join(basedir, 'csolink', 'model.py')
