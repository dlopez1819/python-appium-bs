import os
from invoke import task
import threading

@task
def test(c, env='preprod', lang='en', app='android', deviceOS='emulator', marker='smoke', appiumServer='local'):
    """
    Enable and modify this to add local storage
    """
    deviceList = deviceOS.split(",")
    markerList = marker.split(",")
    jobs = []
    for d in deviceList:
        device = d.split(":")[0]
        os = d.split(":")[1]
        for m in markerList:
            thread = threading.Thread(target=run_automation_test, args=(c, m, app, env, appiumServer, device, os))
            jobs.append(thread)
            thread.start()

    for thread in jobs:
        thread.join()


def run_automation_test(c, m, app, env, appiumServer, device, operatingsystem):
    #runningCommand = f"python3 -m pytest -m {m} ./src/testcases/{app}/* --env ={env} --app={app} --appiumServer={appiumServer} --device='{device}' --os='{operatingsystem}' --reruns 1 --junitxml='./report/xml/{m}_{device}_{operatingsystem}.xml' --html-report='./report/{m}_{device}_{operatingsystem}.html'&"
    runningCommand = f"python3 -m pytest -m {m} ./src/testcases/{app}/* --env ={env} --app={app} --appiumServer={appiumServer} --device='{device}' --os='{os}' --reruns 0  --html-report='./report/{m}_{device}_{os}.html'&"
    if appiumServer == "browserstack": #For browserstack enable parallel running to 5
        #if os.environ.get('browserstack_build_id') is not None:
        #runningCommand = f"python3 -m pytest -m {m} ./src/testcases/{app}/* -workers 5 --tests-per-worker 3 --env ={env} --app={app} --appiumServer={appiumServer} --device='{device}' --os='{operatingsystem}'  --reruns 0  --html-report='./report/{m}_{device}_{operatingsystem}.html'&"
        runningCommand = f"python3 -m pytest -m {m} ./src/testcases/{app}/* --workers 3 --tests-per-worker 1 --env ={env} --app={app} --appiumServer={appiumServer} --device='{device}' --os='{operatingsystem}' --reruns 0 --junitxml='./report/xml/{m}_{device}_{operatingsystem}.xml' --html-report='./report/html/{m}_{device}_{operatingsystem}.html'" 
    c.run(runningCommand)
