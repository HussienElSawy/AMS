#import libraries
import os
import time
from flask import Flask, render_template, request

app = Flask(__name__)

ams_home = os.path.realpath(__file__)[:-18]


def get_mps_data():   
    #list of running processes
    mp_list = os.listdir(ams_home+"kpis")

    mp_table = []
    for mp in mp_list:
        temp = []
        temp.append(mp)
        if(os.popen('ps -ef | grep -v grep | grep -i ams | grep -wc '+mp).read().rstrip() >= '1' or os.popen('crontab -l | grep -w '+ams_home+'kpis/'+mp).read().rstrip()  >= '1'):
            temp.append('Running')
        else:
            temp.append('Stopped')
        mp_table.append(temp)
    return mp_table

def start_stop(name, status):
    if status == 'Stopped':
        os.popen('cd '+ams_home+'kpis/'+name+' ; nohup bash '+ams_home+'bin/timer '+name+' > /dev/null 2>&1 &')
    elif status == 'Running':
        pid=os.popen("ps -ef | grep -w '"+ams_home+"bin/timer "+name+"' | grep -v grep | awk {'print $2'}").read()
        if pid:
            os.popen('kill -9 '+pid)
        else:
            os.popen('crontab -l | grep -wv "'+ams_home+'kpis/'+name+'" > '+ams_home+'bin/crontab_tmp')
            os.popen('crontab '+ams_home+'bin/crontab_tmp') 
    

@app.route('/',  methods=['GET', 'POST'])
def main():
    table_headers=['','Name', 'Status', 'Action']
    if request.method=='POST':
        mp_number = request.form['start_stop_btn']
        mp_name = request.form['mp_name_'+mp_number]
        mp_status = request.form['mp_status_'+mp_number]
        start_stop(mp_name, mp_status)
        #time.sleep(2)
    mp_table = get_mps_data()
    return render_template('main.html', table_head=table_headers, table_data=enumerate(mp_table))

    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9889)
    app.run(debug=True)
