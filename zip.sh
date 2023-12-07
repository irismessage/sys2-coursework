#!/bin/bash
set -eux

git_ref='HEAD'
bundle_file='git.bundle'
zip_file="${1:-exam.zip}"

git bundle create "${bundle_file}" "${git_ref}"
git archive --output="${zip_file}" --add-file="${bundle_file}" "${git_ref}"

ls -lh "${zip_file}"
md5sum "${zip_file}"
