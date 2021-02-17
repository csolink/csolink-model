# All artifacts of the build should be preserved
.SECONDARY:

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- genrate uml images as inline url's
imgflags?=-i


# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: install tests build

# Build the csolink model python library
python: csolink/model.py
docs: docs/index.md
jekyll-docs: docs/Classes.md
shex: csolink-model.shex csolink-modeln.shex csolink-model.shexj csolink-modeln.shexj
json-schema: json-schema/csolink-model.json

build: python docs/index.md gen-golr-views csolink-model.graphql gen-graphviz java context.jsonld contextn.jsonld \
json-schema/csolink-model.json csolink-model.owl.ttl csolink-model.proto csolink-model.shex csolink-model.ttl

# TODO: Get this working
build_contrib: contrib_build_monarch contrib_build_translator contrib_build_go

install: env.lock



# ---------------------------------------
# Install package into build environment
# ---------------------------------------
env.lock:
	pipenv install --dev
	cp /dev/null env.lock


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
csolink/model.py: csolink-model.yaml env.lock
	pipenv run gen-py-classes $< > $@.tmp && pipenv run python $@.tmp &&  mv $@.tmp $@


# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: csolink-model.yaml env.lock
	pipenv run gen-markdown --dir docs $(imgflags) $<

# ~~~~~~~~~~~~~~~~~~~~
# JEKYLL DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/Classes.md: csolink-model.yaml env.lock
	pipenv run python script/jekyllmarkdowngen.py --dir jekyll_docs --yaml $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: csolink-model.yaml dir-golr-views env.lock
	pipenv run gen-golr-views -d golr-views $<


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
csolink-model.graphql: csolink-model.yaml env.lock
	pipenv run gen-graphql $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Graphviz
# ~~~~~~~~~~~~~~~~~~~~
gen-graphviz: csolink-model.yaml dir-graphviz env.lock
	pipenv run gen-graphviz  -d graphviz $< -f gv
	pipenv run gen-graphviz  -d graphviz $< -f svg


# ~~~~~~~~~~~~~~~~~~~~
# Java
# ~~~~~~~~~~~~~~~~~~~~
java: json-schema/csolink-model.json dir-java env.lock
	jsonschema2pojo --source $< -T JSONSCHEMA -t java


# ~~~~~~~~~~~~~~~~~~~~
# JSON-LD CONTEXT
# ~~~~~~~~~~~~~~~~~~~~
context.jsonld: csolink-model.yaml env.lock
	pipenv run gen-jsonld-context $< > tmp.jsonld && ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld

contextn.jsonld: csolink-model.yaml env.lock
	pipenv run gen-jsonld-context --metauris $< > tmp.jsonld && ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld


# ~~~~~~~~~~~~~~~~~~~~
# JSON-SCHEMA
# ~~~~~~~~~~~~~~~~~~~~
json-schema/csolink-model.json: csolink-model.yaml dir-json-schema env.lock
	pipenv run gen-json-schema $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
csolink-model.owl.ttl: csolink-model.yaml env.lock
	pipenv run gen-owl -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Proto
# ~~~~~~~~~~~~~~~~~~~~
csolink-model.proto: csolink-model.yaml env.lock
	pipenv run gen-proto $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
csolink-model.ttl: csolink-model.yaml env.lock
        pipenv run gen-rdf -f ttl --context https://w3id.org/csolink/csolinkml/context.jsonld $<  > $@

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
csolink-model.shex: csolink-model.yaml
	pipenv run gen-shex $< > $@
csolink-modeln.shex: csolink-model.yaml
	pipenv run gen-shex --metauris $< > $@
csolink-model.shexj: csolink-model.yaml
	pipenv run gen-shex --format json $< > $@
csolink-modeln.shexj: csolink-model.yaml
	pipenv run gen-shex --metauris --format json $< > $@


# ----------------------------------------
# Ontology conversion
# ----------------------------------------

# ontology/%.json: ontology/%.ttl
# 	owltools $< -o -f json $@

# ontology/%.obo: ontology/%.ttl
# 	owltools $< -o -f obo --no-check $@

# ontology/%.omn: ontology/%.ttl
# 	owltools $< -o -f omn --prefix '' http://w3id.org/csolink/vocab/ --prefix def http://purl.obolibrary.org/obo/IAO_0000115 $@

# ontology/%.tree: ontology/%.json
# 	ogr --showdefs -t tree -r $< % > $@

# ontology/%.png: ontology/%.json
# 	ogr-tree -t png -o $@ -r $< %


# ~~~~~~~~~~~~~~~~~~~~
# Contrib
# ~~~~~~~~~~~~~~~~~~~~
contrib_build_%: contrib-dir-% contrib/%/docs/index.md contrib/%/datamodel.py contrib-golr-% contrib/%/%.graphql \
contrib/%/%.owl contrib/%/schema.json contrib-java-% contrib/%/%.shex
	echo

contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml env.lock
	pipenv run gen-py-classes contrib/$*.yaml > tmp.py && (pipenv run comparefiles tmp.py $@ && cp tmp.py $@); rm tmp.py

contrib/%/docs/index.md: contrib/%.yaml
	pipenv run gen-markdown --dir contrib/$*/docs $<

contrib/%/datamodel.py: contrib/%.yaml
	pipenv run gen-py-classes contrib/$*.yaml > $@

contrib-golr-%: contrib-dir-% contrib/%.yaml
	pipenv run gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

contrib/%/%.graphql: contrib-dir-% contrib/%.yaml
	pipenv run gen-graphql contrib/$*.yaml > contrib/$*/$*.graphql

contrib-java-%: contrib-dir-% contrib/%/schema.json
	mkdir -p contrib/$*/java
	jsonschema2pojo --source contrib/$*/schema.json -T JSONSCHEMA -t contrib/$*/java

contrib/%/schema.json: contrib-dir-% contrib/%.yaml
	pipenv run gen-json-schema contrib/$*.yaml > $@

contrib/%/%.owl: contrib/%.yaml
	pipenv run gen-owl -o $@ contrib/$*.yaml

contrib/%/%.shex: contrib-dir-% contrib/%.yaml
	pipenv run gen-shex contrib/*.yaml > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: csolink-model.yaml env.lock pytest jsonschema_test
	pipenv run python -m unittest discover -p 'test_*.py'

pytest: csolink/model.py
	pipenv run python $<

jsonschema_test: json-schema/csolink-model.json
	jsonschema $<

# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf contrib/go contrib/monarch contrib/translator docs/images/* docs/*.md golr-views graphql graphviz java json json-schema ontology proto rdf shex
	rm -f env.lock
	pipenv --rm

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

contrib-dir-%:
	mkdir -p contrib/$*
