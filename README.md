# AMS - Automated Monitoring System

## SYNOPSIS

     ams [options] [name...]

## DESCRIPTION**

     ams is a tool to monitor any database  logs  using queries,
     it can also send notifications via several  channels  like:
     SLACK , SMS , MAIL (Text) , MAIL (HTML), MAIL (Attachement)
     it have its own timer, so it can be used instead of crontab
     
## OPTIONS
     Options start with one or two dashes. Many  of  the  options
     require an additional value next to them.

     The short "single-dash" form :     	   -d for example
     The long "double-dash" form  :          --delete for example
     both short and long version require space between  them  and
     the value

    * **-a, --about**
          This  option  show the about file ,  and it doesnt take 
	  any extra values
		  
   * **-c, --create <name>**
          This will allow the user to create new KPI that will be
	  edited with the edit option to configure it 
		  
          See also --edit.
		  
   *  **-d, --delete <name>**
          This will  allow  the user  to delete  any KPI that was
	  created before , this action can't be rolled back! 
		  		  
   *  **-e, --edit [option] <name>**
	  This will allow the user to start configuring/editing the
	  configuration of the mentioned KPI
		  
	  Used together with conf, sms_list, mail_list, query

	  Added in 3.1

   * **-h, --help [options]**
          Usage help. This lists all current command line options
          with a short description.
		  
	  Used together with create, delete, edit, stop, start, test
		  
    * **-M, --manual**
          Manual. Display the huge help text.

          Added in 3.1

    * **-s, --start <name>**
          Starts specific KPI 	
	  Can be used with "all" instead of "name" to start all KPIs
					
		  
    * **-p, --stop <name>**
          Starts specific KPI	
  	  Can be used with "all" instead of "name" to stop all KPIs


## REQUIRMENTS
     The ams system requires some packages to be availble , so it
     can functionate as supposed
	 
     the following packages MUST be installed for all features to
     function as required
	 * **- CURL		(to send notifications to SLACK)**
	 * **- SQLPLUS	(to connect to database)**
	 * **- MAILX	(to send notifications to mail)**


## EXIT CODES
     There are  a  bunch  of  different  error  codes  and  their
     corresponding error messages that may appear during bad con-
     ditions. At the time of this writing, the exit codes are:

     * 1    Unsupported option.

     * 2    Failed to start KPI.

     * 3    Failed to stop KPI.
	 
     *	X    More will be added in the future releases


## AUTHORS / CONTRIBUTORS
     Hussien El-Saw is the main author, but the  whole  list  of
     contributors is found in the separate THANKS file.

## WWW
     https://github.com/hussienelsawy/ams


## LATEST VERSION

  You always find news about what's going on as well as the latest versions
  from the ams web pages, located at:

        https://github.com/hussienelsawy/ams

## SIMPLE USAGE

  **Create/Delete new KPI:**

        ams -c | -d new_kpi
		ams --create | --delete new_kpi

  **Start/Stop all KPIs:**

        ams -s | -p all
		ams --start | --stop all
		
  **Start/Stop specific KPIs:**

        ams -s | -p new_kpi
		ams --start | --stop new_kpi
 
  **Edit Configurations for a KPI:**
		
		ams -e --conf new_kpi

  **Add Mail list to a specific KPI:**
  
		ams -e --mail_list new_kpi

  **Add SMS list to a specific KPI:**
  
		ams -e --sms_list new_kpi
		


  Please direct ams questions, feature requests and trouble reports to the mail
  mentioned below with the one of the following subjects
  
	**Mail: Hussien.ElSawy@outlook.com**
	Subjects:
		* **- AMS Request :** to request new function
		* **- AMS Issue  :** to report an issue
		* **- AMS General :** for any other topic