#!/bin/bash
set -eux

# requires these:
#pacman -S pandoc-cli texlive-latex texlive-latexrecommeneded texlive-fontsrecommened
pandoc answers.md -o answers.pdf
