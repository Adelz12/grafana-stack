# Alerting في الـ Stack

## ما الموجود

- **Prometheus**: يقيّم قواعد التنبيه من `alert_rules.yml` ويرسل التنبيهات إلى Alertmanager على `localhost:9093`.
- **Alertmanager**: يستقبل التنبيهات ويوجّهها إلى المستقبلات (حالياً webhook على المنفذ 5001).
- **alert-webhook**: خدمة صغيرة تستقبل تنبيهات Alertmanager وتطبعها في الـ logs.

## القواعد الحالية (`alert_rules.yml`)

| المجموعة | التنبيه | الشرط |
|----------|---------|--------|
| service_health | ServiceDown | الـ target غير متاح لأكثر من دقيقة |
| resource_usage | HighCPUUsage | استهلاك CPU > 80% لمدة 2 دقيقة |
| resource_usage | HighMemoryUsage | استهلاك ذاكرة > 85% لمدة 2 دقيقة |
| resource_usage | DiskSpaceLow | استخدام القرص > 80% لمدة 5 دقائق |
| application_performance | PythonAppSlowResponse | p95 لوقت الاستجابة لـ my-python-app > 2 ثانية |
| application_performance | HighErrorRate | نسبة أخطاء 5xx > 5% |

## تشغيل الـ Stack مع الـ Alerting

```bash
docker compose up -d --build
```

لمشاهدة تنبيهات الـ webhook في الـ logs:

```bash
docker logs -f alert-webhook
```

## واجهات مفيدة

- **Alertmanager**: http://localhost:9093 (عرض التنبيهات النشطة والمُحلّة)
- **Prometheus Alerts**: http://localhost:9090/alerts (عرض حالة القواعد والتنبيهات)

## إضافة Slack أو البريد

عدّل `alertmanager-config.yml`: أزل التعليق عن مستقبل `slack` أو أضف مستقبل `email` وضبط الـ URL أو إعدادات البريد، ثم أضف الـ route المناسب في `route.routes`.
