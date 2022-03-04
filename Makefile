.PHONY: install

install:
	-@asdf plugin add python
		asdf install python 3.9.10
	-@asdf plugin add nodejs
		asdf install nodejs 17.5.0
	@pip install pipenv
	@asdf reshim python
	@npm install -g serverless
