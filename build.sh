set -x
set -e

p_beamer () {
  pdf=${1/.tex/.pdf}
  TMPDIR=. pandoc -f markdown $1 -t beamer --slide-level 2 -o $pdf
}


for f in *.tex ; do
  p_beamer $f;
done
