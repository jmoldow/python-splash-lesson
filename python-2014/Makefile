all:
	rm -f *.aux *.ps *.bbl *.blg *.tmp *.log *~ *.out *.toc *.nav *.snm
	@echo pdflatex lesson.article.tex
	@pdflatex lesson.article.tex
	@pdflatex lesson.article.tex
	@echo pdflatex lesson.beamer.tex
	@pdflatex lesson.beamer.tex
	@pdflatex lesson.beamer.tex
	@if fgrep -e "Label(s) may have changed" $*.log > /dev/null; then \
  echo Latexing again because labels changed.; \
  echo pdflatex $*; \
  @pdflatex $*; \
fi
	rm -f *.aux *.ps *.bbl *.blg *.tmp *.log *~ *.out *.toc *.nav *.snm *.vrb

