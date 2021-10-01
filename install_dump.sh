#!/usr/bin/env bash

docker cp dump.sql db:dump.sql
docker exec -it db psql -d caserepo -U caseapi_test -a -f dump.sql -v ON_ERROR_STOP=1