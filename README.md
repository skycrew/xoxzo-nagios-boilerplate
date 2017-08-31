XOXZO Nagios Boilerplate
========================
The repository contains boilerplate to write nagios plugin in python. Once the check failed or critical, emergency operations center (EOC) will get notification through their phone using XOXZO telephony API.

**How to use**

    # Clone this repo
    git clone https://github.com/skycrew/xoxzo-nagios-boilerplate.git
    
    # Go into the repository
    cd xoxzo-nagios-boilerplate
    
    # Install requirements
    pip install -r requirements.txt
    
    # Sign up xoxzo account
    https://www.xoxzo.com/en/accounts/signup/
    
    # Create API user
    https://www.xoxzo.com/en/you/createapiuser/
    
    # Setting up xoxzo/config.yml
    api_url: https://api.xoxzo.com
    api_sid: [REPLACE_WITH_XOXZO_API_SID]
    auth_token: [REPLACE_WITH_XOXZO_AUTH_TOKEN]
    
    # Start writing your nagios check plugins
**Dont have time to write nagios plugin?**

    # Just clone this repo, fire up your python and try the xoxzo api :D
    
    from xoxzo.api import XoxzoApi
    api = XoxzoApi()
    status = api.call(caller="+60199999999", recipient="+60123456789", message="Hello world!")

**License**

The xoxzo-nagios-boilerplate is licensed under the terms of the GPL Open Source license and is available for free.
