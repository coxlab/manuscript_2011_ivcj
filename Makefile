.PHONY: pdf

SHORT_NAME=ivcj_lfw
PDFVIEW?=open

fg2011_lfw.pdf: clean
	pdflatex ${SHORT_NAME}.tex && bibtex ${SHORT_NAME} && pdflatex ${SHORT_NAME}.tex && pdflatex ${SHORT_NAME}.tex

view: ${SHORT_NAME}.pdf
	${PDFVIEW} ${SHORT_NAME}.pdf

clean:
	rm -vf $$(ls ${SHORT_NAME}.??? | grep -v tex | grep -v bib)


# Figures & Tables

screening_histograms:
	cd figures; python histogram_figure.py

data_table:
	cd tables; python generate_performance_table.py

roc_curves:
	cd figures; python generate_roc_curves.py

figures: screening_histograms data_table roc_curves
    
