OUTPUTS = $(sort $(wildcard outputs/*.txt))
QUESTIONS = $(patsubst outputs/%.txt,%,$(OUTPUTS))
MAKEFILE_PATH = /Users/DanialYunus/Dev/cse412project/cse-412-class-project/phase2
ROOT = $(MAKEFILE_PATH)

all: path $(QUESTIONS)
	rm -rf tmp

%: queries/%.sql
	@echo "checking $@; correct if nothing below ----"
	@psql -A -t -d $(USER) -q -f $< 1> tmp/$@.txt
	@diff outputs/$@.txt tmp/$@.txt || echo "$@ is wrong"; exit 0
	@echo ""

path:
	@mkdir -p tmp

setup_postgres:
	@echo "creating tables"
	psql -d $(USER) -q -f setup_postgres/create_tables.sql


insert_postgres:
	@echo "inserting into tables"
	psql -d $(USER) -q -f setup_postgres/insert_tables.sql

clean_postgres:
	@echo "dropping tables"
	psql -d $(USER) -q -f setup_postgres/drop_tables.sql


.PHONY: setup_postgres

