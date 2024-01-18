#!/bin/bash
set -eux

# requires these:
#pacman -S pandoc-cli texlive-latex texlive-latexrecommended texlive-fontsrecommended
pandoc answers.md -o answers.pdf
