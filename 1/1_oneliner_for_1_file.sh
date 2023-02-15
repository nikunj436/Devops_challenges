#!/usr/bin/bash
sed -E -e 's|([[:alnum:]]+)\s+\1|\1|g' inputs/1_input.txt > outputs_single_file/1_output.txt




