#!/bin/sh
#
# Shell script to extract notes for single lecture.
# First argument specifies which lecture number to compile.
# If no argument is given, all notes will be compiled.

PDFLATEX=`which pdflatex`
BIBTEX=`which bibtex`

if [ $# -eq 0 ]
then
    echo "No lecture number specified."
    echo "Compiling all lectures."
    echo 'Compiling sources.'
    $PDFLATEX main.tex > /dev/null
    $BIBTEX main > /dev/null
    echo 'Compiling sources again.'
    $PDFLATEX main.tex > /dev/null
    $PDFLATEX main.tex > /dev/null
    mv main.pdf ee227c-notes.pdf
    echo "Cleaning up."
    rm *.aux *.log *.toc *.out *.bbl *.blg
    exit 0
fi

if [ -f "lecture$1.tex" ]
then
    LATEX_OFFSET=`expr $1 - 1`
    echo "lecture$1.tex exists."
    cat header.tex > tmp-lecture.tex
    echo '\\setcounter{section}{'$LATEX_OFFSET'}' >> tmp-lecture.tex
    cat "lecture$1.tex" >> tmp-lecture.tex
    cat footer.tex >> tmp-lecture.tex
    echo 'Compiling sources.'
    $PDFLATEX tmp-lecture.tex > /dev/null
    $BIBTEX tmp-lecture > /dev/null
    echo 'Compiling sources again.'
    $PDFLATEX tmp-lecture.tex > /dev/null
    $PDFLATEX tmp-lecture.tex > /dev/null
    mv tmp-lecture.pdf ee227c-lecture$1.pdf
    echo "Created ee227c-lecture$1.pdf"
    echo "Cleaning up."
    rm tmp-lecture.*
else
    echo "lecture$1.tex does not exist."
fi
