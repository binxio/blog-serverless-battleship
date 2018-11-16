# destroyer.big-gun
Contains a GCF that acts as a big-gun.

## Developing Cloud Functions
The Python runtime for Google Cloud Functions uses Flask to handle incoming requests. This helper invokes your function in response to an incoming request and takes care of other details, such as handling HTTP.

## Dependencies
When you deploy your function, Cloud Functions downloads and installs dependencies declared in the requirements.txt file using pip. You can also pre-package fully materialized dependencies alongside your function.

## Deploying
Cloud Functions can accept source code directly. The file should be called `main.py`. To deploy type `make deploy` and to remove type `make delete`.

## After deploying you see the following

```text
availableMemoryMb: 256
entryPoint: dnvriend_destroyer
httpsTrigger:
  url: https://us-central1-speeltuin-dennis-vriend.cloudfunctions.net/dnvriend_destroyer
labels:
  deployment-tool: cli-gcloud
name: projects/speeltuin-dennis-vriend/locations/us-central1/functions/dnvriend_destroyer
runtime: python37
serviceAccountEmail: speeltuin-dennis-vriend@appspot.gserviceaccount.com
sourceUploadUrl: https://storage.googleapis.com/gcf-upload-us-central1-42c4f8bc-8269-44c2-9ac0-0c81aef18837/1b2f3b86-e826-4417-91e5-29d856538d2c.zip?GoogleAccessId=service-423776850950@gcf-admin-robot.iam.gserviceaccount.com&Expires=1542363166&Signature=t0ip%2Fid4mMJqpjvmW%2B%2F8SldastN3Ukk3aXDh9EQntQDRx82uMpw7LsUc%2BlUM2jHw85hu9WBOAJNRTXHAkkRskSTiTFArzH2RUQRXtrw0wCsi60pqVFb1u%2FkUTO807A47zgLVDAPy6702X3qQ%2Bt%2FCD%2FjSDRbYy6b%2BF7t1ejxnv%2FHxcMzLVVHhYPcrbspmlDkbSdiDwbDBWId3NvRu%2F5x76iDU10JASYXPtJyiM412JVxbBqGh7Dqgr9LnvF%2FdHH%2BM5f5WsY792pDFwcnmjHvMfW5tXsIw%2BJRr%2B5vzURghiXiRfITALKBmPVXpAGtm0Yt3J8xelVF3Ls6r2i3x%2FTZotw%3D%3D
status: ACTIVE
timeout: 60s
updateTime: '2018-11-16T09:43:12Z'
versionId: '1'
```

## Resources
- [GCF - Binding to events](https://cloud.google.com/functions/docs/concepts/events-triggers)
- [GCF - HTTP Trigger](https://cloud.google.com/functions/docs/writing/http)
- [GCF - Scheduled Trigger](https://medium.com/@earlg3/google-cloud-functions-scheduled-trigger-915b5fb8310f)
- [Deploying Cloud Functions](https://cloud.google.com/functions/docs/deploying/filesystem)
- [Specifying Dependencies](https://cloud.google.com/functions/docs/concepts/python-runtime#specifying_dependencies)
- [How to Schedule (Cron) Jobs with Cloud Functions for Firebase](https://firebase.googleblog.com/2017/03/how-to-schedule-cron-jobs-with-cloud.html)