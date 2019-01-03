#!/usr/bin/env python
from gomatic import *
import os, re

print "Updating PetClinic Pipeline..."
go_server_host = re.search('https?://([a-z0-9.\-._~%]+)', os.environ['GO_SERVER_URL']).group(1)
go_server_url = "%s:%s" % (go_server_host, "8153")
configurator = GoCdConfigurator(HostRestClient(go_server_url))
secret_variables = {'GCLOUD_SERVICE_KEY': 'AES:GT+IzogHKSnIkhQMyy2qTg==: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'}
pipeline = configurator\
	.ensure_pipeline_group("sample")\
	.ensure_replacement_of_pipeline("PetClinic")\
	.set_git_material(GitMaterial("https://github.com/MattBelcher/devops-in-practice-workshop.git", branch="master", ignore_patterns=set(['pipelines/*'])))
stage = pipeline.ensure_stage("commit")
job = stage\
    .ensure_job("build-and-publish")\
    .ensure_environment_variables({'MAVEN_OPTS': '-Xmx1024m', 'GCLOUD_PROJECT_ID': 'devops-workshop-mb'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('docker-jdk')
job.add_task(ExecTask(['./mvnw', 'clean', 'package']))
job.add_task(ExecTask(['bash', '-c', 'docker build --tag pet-app:$GO_PIPELINE_LABEL --build-arg JAR_FILE=target/spring-petclinic-2.0.0.BUILD-SNAPSHOT.jar .']))
job.add_task(ExecTask(['bash', '-c', 'docker login -u _json_key -p"$(echo $GCLOUD_SERVICE_KEY | base64 -d)" https://us.gcr.io']))
job.add_task(ExecTask(['bash', '-c', 'docker tag pet-app:$GO_PIPELINE_LABEL us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
job.add_task(ExecTask(['bash', '-c', 'docker push us.gcr.io/$GCLOUD_PROJECT_ID/pet-app:$GO_PIPELINE_LABEL']))
stage = pipeline.ensure_stage("deploy")
job = stage\
    .ensure_job("deploy")\
    .ensure_environment_variables({'GCLOUD_ZONE': 'us-central1-a', 'GCLOUD_PROJECT_ID': 'devops-workshop-mb', 'GCLOUD_CLUSTER': 'devops-workshop-gke'})\
    .ensure_encrypted_environment_variables(secret_variables)
job.set_elastic_profile_id('kubectl')
job.add_task(ExecTask(['bash', '-c', 'echo $GCLOUD_SERVICE_KEY | base64 -d > secret.json && chmod 600 secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud auth activate-service-account --key-file secret.json']))
job.add_task(ExecTask(['bash', '-c', 'gcloud container clusters get-credentials $GCLOUD_CLUSTER --zone $GCLOUD_ZONE --project $GCLOUD_PROJECT_ID']))
job.add_task(ExecTask(['bash', '-c', './deploy.sh']))
job.add_task(ExecTask(['bash', '-c', 'rm secret.json']))

configurator.save_updated_config()
