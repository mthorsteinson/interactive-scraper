#!/bin/bash

source .venv/bin/activate
OTEL_RESOURCE_ATTRIBUTES="service.name=interactive-token-app,service.namespace=interactive-token-group,deployment.environment=production" \
OTEL_EXPORTER_OTLP_ENDPOINT="https://otlp-gateway-prod-us-west-0.grafana.net/otlp" \
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Basic%20MTE1NjE0NDpnbGNfZXlKdklqb2lNVEUwTVRVNE55SXNJbTRpT2lKemRHRmpheTB4TVRVMk1UUTBMVzkwWld3dGIyNWliMkZ5WkdsdVp5MXBiblJsY21GamRHbDJaUzF6WTNKaGNHVnlMV0Z3Y0MxMGIydGxiaUlzSW1zaU9pSjNXRm96TmtKaU5HUXpOREJPTXpWemJHYzNNMmhCUW1vaUxDSnRJanA3SW5JaU9pSndjbTlrTFhWekxYZGxjM1F0TUNKOWZRPT0=" \
OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf" \
opentelemetry-instrument flask run -p 5000