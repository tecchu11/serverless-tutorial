.PHONY: install

install:
	-@asdf plugin add python
	-@asdf plugin add nodejs
	@asdf install
	@npm ci
	@pip install pipenv
	@asdf reshim python
	@pipenv sync -d
	@pre-commit install
