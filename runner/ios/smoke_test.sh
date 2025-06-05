export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
# FOR RUNNING TEST ON LOCAL SERVER
#python3 -m invoke test --env='preprod' --lang='en' --app='ios' --deviceOS='iPhone 15:17' --marker='sanity' --appiumServer='local'

# BROWSERSTACK CLOUD SERVER
python3 -m invoke test --env='preprod' --lang='en' --app='ios' --deviceOS='iPhone 15:17' --marker='smoke' --appiumServer='browserstack'
#browserstack-sdk pytest -s boh_login_test.py
