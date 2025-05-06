export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
##python3 -m invoke test --env='preprod' --lang='en' --app='ios' --deviceOS='iPhone 15:17' --marker='smoke' --appiumServer='local'
 browserstack-sdk pytest -s ./src/testcases/ios/sanity/boh_login_test.py
