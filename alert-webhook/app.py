"""
Minimal webhook receiver for Prometheus Alertmanager (stdlib only, no pip).
Prints incoming alerts to stdout so you can see them in docker logs.
"""
import json
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler


def log(msg: str) -> None:
    print(f"[{datetime.utcnow().isoformat()}Z] {msg}", flush=True)


class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Alertmanager webhook receiver. Send POST with Alertmanager payload.\n")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path != "/" and self.path != "":
            self.send_response(404)
            self.end_headers()
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length) if length else b"{}"
            data = json.loads(body.decode("utf-8")) if body else {}
        except Exception as e:
            log(f"Error reading body: {e}")
            self.send_response(400)
            self.end_headers()
            return
        try:
            status = data.get("status", "?")
            alerts = data.get("alerts", [])
            log(f"Alertmanager webhook: status={status} alerts={len(alerts)}")
            for a in alerts:
                labels = a.get("labels", {})
                ann = a.get("annotations", {})
                log(f"  [{a.get('status')}] {labels.get('alertname', '?')} severity={labels.get('severity')} - {ann.get('summary', '')}")
        except Exception as e:
            log(f"Error: {e}")
        self.send_response(200)
        self.end_headers()

    def log_message(self, method, path, *args):
        pass  # suppress default request logging


if __name__ == "__main__":
    log("Alert webhook receiver listening on 0.0.0.0:5001")
    HTTPServer(("0.0.0.0", 5001), WebhookHandler).serve_forever()
