# Shopizer Case Study Deployment Architecture

Status: no SpecLoop-AI deployment target has been selected or implemented.

## Shopizer Runtime Evidence

The repository contains a Spring Boot `sm-shop` application and a `sm-shop/Dockerfile`. This static case study did not inspect or verify a live deployment, cloud account, production topology, or operational configuration.

## Proposed SpecLoop-AI Environments

For the scaffold, run the Streamlit shell locally. A shared deployment would require approved repository access, identity/authentication, isolated processing, network egress policy, and artifact storage; none is configured yet.

## Configuration and Secrets

Use environment or managed-secret configuration for future provider credentials. Never check credentials into the repository or sample data. No AI-provider credentials are required by the current stub application.

## Operations and Recovery

Before shared use, define source revision pinning, artifact backups/deletion, job timeouts, retry behavior, audit logging, monitoring, and recovery. Do not assume Shopizer's runtime deployment practices apply to this separate tool.