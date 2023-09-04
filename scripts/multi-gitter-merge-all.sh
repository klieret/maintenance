#!/usr/bin/env bash

# bash strict mode
set -euo pipefail
IFS=$'\n\t'

set -x

BRANCH_NAME="${1:-pre-commit-ci-update-config}"
echo "Branch name: ${BRANCH_NAME}"

multi-gitter merge -U klieret --branch "${BRANCH_NAME}" --merge-type squash,merge

for org in dieret hsf-training gnn-tracking clusterking cidakima HSF; do
    multi-gitter merge -O "${org}" --branch "${BRANCH_NAME}" --merge-type squash,merge
done
