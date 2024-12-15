gcloud components update
gsutil -m -o GSUtil:parallel_process_count=1 -o GSUtil:parallel_thread_count=24 rsync -r . gs://www.physicsbootcamp.org
# gsutil -m -o GSUtil:parallel_process_count=1 -o GSUtil:parallel_thread_count=24 acl -r ch -u AllUsers:R gs://www.physicsbootcamp.org
