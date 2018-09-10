#variables
kpi_path=$1

#sources
. $kpi_path/kpi.conf


#HTML Header
echo "<header style='font-size:16;'><b></b></header>" > $kpi_path/$Mail_Output

#Query with HTML/CSS
sqlplus -s $DB_Username/$DB_Password@//$DB_IP:$DB_Port/$DB_SID << !

SET MARKUP HTML ON SPOOL ON PREFORMAT OFF ENTMAP ON -
HEAD "<STYLE type='text/css'> -
<!-- table { background-color:#F2F2F5; border-width:1px 1px 0px 1px; border-color:#C9CBD3; border-style:solid; } td { color:#000000; font-family:Tahoma,Arial,Helvetica,Geneva,sans-serif; font-size:9pt; background-color:#EAEFF5;padding:8px;background-color:#F2F2F5;border-color:#ffffff #ffffff #cccccc #ffffff; border-style:solid solid solid solid; border-width:1px 0px 1px 0px; } th { font-family:Tahoma,Arial,Helvetica,Geneva,sans-serif;font-size:9pt;padding:8px;background-color:#CFE0F1;border-color:#ffffff #ffffff #cccccc #ffffff; border-style:solid solid solid none; border-width:1px 0px 1px 0px; white-space:nowrap; } --> -
</STYLE>" -
TABLE "WIDTH='10%'"

spool $kpi_path/$Mail_Output append 
`cat $kpi_path/query`

spool off;
quit;
!

