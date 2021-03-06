#!/bin/bash
patch -p0 < internationalization.patch
patch -p0 < lang-template.patch

sudo supervisorctl restart bbx
. /srv/bbx/envs/bbx/bin/activate
python /srv/bbx/baobaxia/app/django-bbx/manage.py update_templates
