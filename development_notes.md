# LinkedIn API

There is a well used Python library for communicating with the LinkedIn API: https://github.com/ozgur/python-linkedin#profile-api
However, it is apparently very old and only supports version 1 of the API, which seems deprecated. There is a fork https://github.com/advoninja/python-linkedin/tree/develop which has some updates on the branch `develop` which seems to be current.

The only way to get the data we're interested in is to use the [*Full profile* permission](https://docs.microsoft.com/en-us/linkedin/shared/references/v2/profile/full-profile?context=linkedin/consumer/context). This is limited to only reviewed applications by the LinkedIn team.

