# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m sphinx.cmd.build -qnNW docs docs/_build/html
python -m sphinx.cmd.build -qnNW -b doctest docs docs/_build/doctest
python -m pytest
tests_exit_code=$?
exit "$tests_exit_code"
