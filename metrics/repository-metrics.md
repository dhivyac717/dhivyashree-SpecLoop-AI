# Shopizer Repository Metrics

Status: static source inventory from the checked-out repository; not a production or quality score.

## Observed Baseline

- Root Maven project aggregates five modules: `sm-core-model`, `sm-core-modules`, `sm-core`, `sm-shop-model`, and `sm-shop`.
- Root POM declares Java 11 and Spring Boot 2.5.12.
- Reviewed capability areas: order checkout, cart operations, customer registration/authentication.
- Order integration test class is ignored and incomplete.
- Cart integration class contains ordered scenarios for create/update/missing code/multi-update/zero-quantity/delete.
- Customer registration test covers successful registration followed by login/token response.

## Reproducible Collection

Record commit SHA, count modules/source/test files using a pinned script, list selected test classes and annotations, and run the Maven wrapper. The analysis for these drafts did not run Maven tests, dependency scans, or coverage tools.

## Limitations

These observations are not test pass rates, code coverage, vulnerability counts, performance measurements, or operational metrics. Do not compare trends without using the same revision and method.