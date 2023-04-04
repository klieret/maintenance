#!/usr/bin/env bash

# bash strict mode
set -euo pipefail
IFS=$'\n\t'

set -x

BRANCH_NAME="${1:-pre-commit-ci-update-config}"
echo "Branch name: ${BRANCH_NAME}"

multi-gitter merge -U klieret --branch "${BRANCH_NAME}" --merge-type squash
multi-gitter merge -O dieret --branch "${BRANCH_NAME}" --merge-type squash
multi-gitter merge -O hsf-training --branch "${BRANCH_NAME}" --merge-type squash
multi-gitter merge -O gnn-tracking --branch "${BRANCH_NAME}" --merge-type squash
multi-gitter merge -O clusterking --branch "${BRANCH_NAME}" --merge-type squash
