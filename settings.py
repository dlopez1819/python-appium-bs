import os
import yaml

if os.path.exists(os.path.dirname(__file__) + "/src/config/desired_caps.yaml"):
    #try:
    with open(os.path.dirname(__file__) + "/src/config/desired_caps.yaml") as f:
        CONFIG = yaml.safe_load(f)
    if os.environ.get('browserstack_user') is not None:
        CONFIG['browserstack_user'] = os.environ.get('browserstack_user')
        CONFIG['browserstack_accesskey'] = os.environ.get('browserstack_accesskey')
        CONFIG['browserstack']['appiumserverlocation'] = 'https://' + os.environ.get('browserstack_user') + ':' + \
                                                        os.environ.get('browserstack_accesskey') + \
                                                        '@hub-cloud.browserstack.com/wd/hub'
    else:
        tempUserInfo = CONFIG['browserstack']['appiumserverlocation'].split('@')[0]
        CONFIG['browserstack_user'] = tempUserInfo.split(':')[1].replace('//', '')
        CONFIG['browserstack_accesskey'] = tempUserInfo.split(':')[2]
    #except:
        #raise Exception("Open capbility file fail")
else:
    raise Exception("Capability file not exists")

if os.path.exists(os.path.dirname(__file__) + "/browserstack.yml"):
    with open(os.path.dirname(__file__) + "/browserstack.yml") as f:
        CONFIG_BS = yaml.safe_load(f)

