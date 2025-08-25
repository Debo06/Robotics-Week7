# emits synthetic JSON logs
import argparse, json, os, time, random, datetime as dt, pathlib
p=argparse.ArgumentParser(); p.add_argument('--out',default='logs/monitor.log'); p.add_argument('--n',type=int,default=200); a=p.parse_args()
pathlib.Path(os.path.dirname(a.out)).mkdir(parents=True, exist_ok=True)
with open(a.out,'w') as f:
    rid=int(time.time()); 
    f.write(json.dumps({'time':dt.datetime.utcnow().isoformat()+'Z','level':'INFO','event':'job_start','run_id':rid})+'\n')
    for i in range(a.n):
        if random.random()<0.02:
            f.write(json.dumps({'time':dt.datetime.utcnow().isoformat()+'Z','level':'ERROR','event':'api_timeout','retry':1,'run_id':rid})+'\n')
        time.sleep(0.001)
    f.write(json.dumps({'time':dt.datetime.utcnow().isoformat()+'Z','level':'INFO','event':'job_complete','rows':a.n,'run_id':rid})+'\n')
print('✅ wrote', a.out)
