#!/bin/sh
#
# Shell script to extract notes for single lecture
# First argument specifies which lecture number to compile

# PDFLATEX=/usr/bin/pdflatex
PDFLATEX=/Library/TeX/texbin/pdflatex

if [ $# -eq 0 ]
then
    echo "No lecture number specified."
    echo "Compiling all lectures."
    echo 'Compiling sources.'
    $PDFLATEX main.tex > /dev/null
    echo 'Compiling sources again.'
    $PDFLATEX main.tex > /dev/null
    mv main.pdf ee227c-notes.pdf
    echo "Cleaning up."
    rm *.aux *.log *.toc *.out
    exit 0
fi

if [ -f "lecture$1.tex" ]
then
    LATEX_OFFSET=`expr $1 - 1`
    echo "lecture$1.tex exists."
    echo '\\documentclass[12pt]{article}' > tmp-lecture.tex
    echo '\\usepackage{macros}' >> tmp-lecture.tex
    echo '\\begin{document}' >> tmp-lecture.tex
    echo '\\input{title}' >> tmp-lecture.tex
    echo '\\maketitle' >> tmp-lecture.tex
    echo '\\setcounter{section}{'$LATEX_OFFSET'}' >> tmp-lecture.tex
    cat "lecture$1.tex" >> tmp-lecture.tex
    echo '\\end{document}' >> tmp-lecture.tex
    echo 'Compiling sources.'
    $PDFLATEX tmp-lecture.tex > /dev/null
    echo 'Compiling sources again.'
    $PDFLATEX tmp-lecture.tex > /dev/null
    mv tmp-lecture.pdf ee227c-lecture$1.pdf
    echo "Created lecture$1.pdf"
    echo "Cleaning up."
    rm tmp-lecture.*
else
    echo "lecture$1.tex does not exist."  
fi
