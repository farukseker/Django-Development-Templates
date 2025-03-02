#!/bin/sh
set -e

echo "MinIO bucket oluşturuluyor..."
sleep 5  # MinIO'nun başlatılması için bekleme süresi

mc alias set local http://minio:9000 admin supersecret
mc mb local/my-bucket || true
mc policy set public local/my-bucket

echo "MinIO bucket oluşturuldu."
exec "$@"
