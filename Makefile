.DEFAULT_GOAL := help
create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	mkdir -p ${PRACTICE}
	@echo "Creating practice"

# 	mkdir demo-practice
# 	mkdir demo-practice/src
# 	mkdir demo-practice/tests
# 	mkdir demo-practice/docs
# 	mkdir demo-practice/README.md


remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rmdir /s /q ${PRACTICE}
	@echo "Removing practice"


