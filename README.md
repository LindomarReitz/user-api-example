# user-api-example

![Main workflow](https://github.com/LindomarReitz/user-api-example/workflows/Main%20workflow/badge.svg) [![Maintainability](https://api.codeclimate.com/v1/badges/b6ef4417631603bfc8de/maintainability)](https://codeclimate.com/github/LindomarReitz/user-api-example/maintainability)

Change the env `PACT_BROKER_URL`. If you want to use [PactFlow](https://pactflow.io/) change the env `PACT_BROKER_TOKEN`.

Run using docker-compose:

```
docker-compose up -d
docker-compose exec user_api bash
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the API:

```
python user_api.py
```

Now is it possible to access the endpoints (e.g. http://localhost:8081/users)

## Validate consumer contract

To use the env `PACT_BROKER_TOKEN` add the option `--pact-broker-token $PACT_BROKER_TOKEN`.

Run pact-verifier for the latest version:

```
pact-verifier --provider-base-url http://<user_endpoint> \
--pact-url $PACT_BROKER_URL/pacts/provider/User/consumer/Checkout/latest
```

Run pact-provider for a specific version:

```
pact-verifier --provider-base-url http://<user_endpoint> \
--pact-url $PACT_BROKER_URL/pacts/provider/User/consumer/Checkout/version/<version>
```

Publish provider results:

```
pact-verifier --provider-base-url http://<user_endpoint> \
--pact-url $PACT_BROKER_URL/pacts/provider/User/consumer/Checkout/latest \
--provider-app-version <provider-version> \
--publish-verification-results
```


