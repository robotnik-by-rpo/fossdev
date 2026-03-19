.DEFAULT_GOAL := help
create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	mkdir -p ${PRACTICE}
	@echo "Creating practice"
	cp PracticeMakefile ${PRACTICE}/Makefile
# 	mkdir demo-practice
# 	mkdir demo-practice/src
# 	mkdir demo-practice/tests
# 	mkdir demo-practice/docs
# 	mkdir demo-practice/README.md

# Монорепозиторий

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf ${PRACTICE}
	@echo "Removing practice"



