.PHONY: help create update delete
.DEFAULT_GOAL := help
region := europe-west1

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

deploy: ## deploys the application
	gcloud functions deploy dnvriend_destroyer --entry-point dnvriend_destroyer --runtime python37 --trigger-http --region $(region)

delete: ## delete the application
	gcloud functions delete dnvriend_destroyer --region $(region)

list-event-types: ## list the event types
	gcloud functions event-types list

logs: ## show logs
#	gcloud functions logs read dnvriend_destroyer --region $(region) > dnvriend_battleship.log
#	gcloud alpha functions logs read dnvriend_destroyer --region $(region)
	gcloud functions logs read --region europe-west1

describe: ## displays data about the app
	gcloud functions describe dnvriend_destroyer --region $(region)

list: ## list app engine instances
	gcloud functions list --region $(region)

regions-list: ## show list of regions
	gcloud functions regions list
