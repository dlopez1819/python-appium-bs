export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
# FOR RUNNING TEST ON LOCAL SERVER
#python3 -m invoke test --env='preprod' --lang='en' --app='ios' --deviceOS='iPhone 15:17' --marker='sanity' --appiumServer='local'

# BROWSERSTACK CLOUD SERVER
python3 -m invoke test --env='preprod' --lang='en' --app='android' --deviceOS='Samsung Galaxy S22:12.0' --marker='functional22' --appiumServer='browserstack'

