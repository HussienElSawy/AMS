#variables
kpi_path=$1

#sources
. $kpi_path/kpi.conf

sqlplus -s $DB_Username/$DB_Password@//$DB_IP:$DB_Port/$DB_SID << !

spool $kpi_path/file.csv
set linesize 1000
set termout off
set trim on
set colsep ' | '
set tab off
set heading off

`cat $kpi_path/query`

spool off;
quit;
!
