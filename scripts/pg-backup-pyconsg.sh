#!/bin/bash
source $HOME/bin/script-settings-pyconsg.sh
BACKUPFOLDER='backups_'$PROJECTNAME'/postgres'

mkdir -p $HOME/$BACKUPFOLDER

KEEP=30
BACKUPS=`find $HOME/$BACKUPFOLDER -name "pgdump-*.gz" | wc -l | sed 's/\ //g'`

while [ $BACKUPS -ge $KEEP ]
do
    ls -tr1 $HOME/$BACKUPFOLDER/pgdump-*.gz | head -n 1 | xargs rm -f
    BACKUPS=`expr $BACKUPS - 1`
done

DATE=`date +%Y%m%d%H%M%S`
rm -f $HOME/$BACKUPFOLDER/.pgdump-${DATE}.gz_INPROGRESS
pg_dump -c -Fc -O -U $DBUSER -f $HOME/$BACKUPFOLDER/.pgdump-${DATE}._INPROGRESS
mv -f $HOME/$BACKUPFOLDER/.pgdump-${DATE}.gz_INPROGRESS $HOME/$BACKUPFOLDER/pgdump-${DATE}.gz
exit 0
