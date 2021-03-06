all:
	make WCDB1.zip

clean:
	rm -f WCDB1.log
	rm -f WCDB1.zip
    rm -f *.html
	rm -f *.pyc

turnin-list:
	turnin --list acoomans cs373pj3

turnin-submit: WCDB1.zip
	turnin --submit acoomans cs373pj3 WCDB1.zip

turnin-verify:
	turnin --verify acoomans cs373pj3

Models.html: Models.py
	pydoc -w Models

WCDB1.log:
	git log > WCDB1.log

WCDB1.zip: makefile apiary.apib  \
           Models.html Models.py \
           WCDB1.log WCDB1.pdf
	zip -r WCDB1.zip             \
	       makefile apiary.apib  \
	       Models.html Models.py \
	       WCDB1.log WCDB1.pdf
