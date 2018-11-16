.PHONY: help create update delete
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

deploy: ## deploys the application
	gcloud functions deploy dnvriend-destroyer --runtime python37 --trigger-http

browse: ## open browser
	gcloud app browse

logs: ## show logs
	gcloud app logs tail -s default

describe: ## displays data about the app
	gcloud app describe

list: ## list app engine instances
	gcloud app instances list

