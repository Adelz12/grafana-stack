# 🚀 Next-Gen Unified Observability Platform (LGTM Stack)

A professional, enterprise-grade observability stack built on **Loki, Grafana, Tempo, and Mimir**, featuring a unified **OpenTelemetry (OTel) Collector** pipeline and **eBPF-powered** zero-code instrumentation.

## 🏗️ Architecture
This platform provides 360-degree visibility across four pillars:
*   **Metrics**: Prometheus & Mimir (Long-term, scalable storage)
*   **Logs**: Loki (Index-free, high-speed log aggregation)
*   **Traces**: Tempo (Distributed request tracing)
*   **Profiles**: Pyroscope (Code-level performance profiling)

## 💎 Key Features
*   **Unified Pipeline**: Powered by the **OpenTelemetry Collector** for standardized data routing.
*   **Zero-Code Instrumentation**: **Beyla** (eBPF) automatically captures metrics/traces at the kernel level.
*   **Performance Testing**: Integrated **k6** engine for load simulation.
*   **Standardized Deployment**: Unified `docker-compose.yml` with pinned stable versions.

## 🚀 Quick Start
1.  Clone the repository.
2.  Ensure you have Docker and Docker Compose installed.
3.  Run the stack:
    ```bash
    docker compose up -d
    ```
4.  Access Grafana at [http://localhost:3005](http://localhost:3005) (Anonymous Admin enabled).

## 🕵️‍♂️ Usage
*   **Explore Tab**: Navigate between `Loki`, `Tempo`, `Mimir`, and `Pyroscope`.
*   **Load Test**: Run `k6 run load-test.js` to see real-time performance spikes.
