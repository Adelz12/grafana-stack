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
*   **Alerting**: **Prometheus** + **Alertmanager** with configurable alert rules for service health, resource usage, and application performance.
*   **Standardized Deployment**: Unified `docker-compose.yml` with pinned stable versions.

## 🚀 Quick Start
1.  Clone the repository.
2.  Ensure you have Docker and Docker Compose installed.
3.  Run the stack:
    ```bash
    docker compose up -d --build
    ```
    > **Note**: Use `--build` flag on first run to build custom services (e.g., `alert-webhook`, `my-python-app`).
4.  Access Grafana at [http://localhost:3005](http://localhost:3005) (Anonymous Admin enabled).

## 🕵️‍♂️ Usage
*   **Explore Tab**: Navigate between `Loki`, `Tempo`, `Mimir`, and `Pyroscope`.
*   **Load Test**: Run `k6 run load-test.js` to see real-time performance spikes.
*   **Alerting**: Monitor alerts via [Alertmanager UI](http://localhost:9093) or check webhook logs with `docker logs -f alert-webhook`.

## 📢 Alerting

The stack includes a complete alerting pipeline:
*   **Prometheus** evaluates alert rules from `prometheus/alert_rules.yml` (service health, resource usage, application performance).
*   **Alertmanager** routes alerts to configured receivers (webhook, Slack, email, etc.) using `alertmanager/alertmanager-config.yml`.
*   **alert-webhook** service receives and logs alerts for testing and debugging.

**Quick Links:**
*   Alertmanager UI: [http://localhost:9093](http://localhost:9093)
*   Prometheus Alerts: [http://localhost:9090/alerts](http://localhost:9090/alerts)
*   View webhook logs: `docker logs -f alert-webhook`

For detailed alerting configuration, see [ALERTING.md](./ALERTING.md).
