# LinkedIn API

There is a Python library for communicating with the LinkedIn API: https://github.com/ozgur/python-linkedin#profile-api
However, it is apparently very old and only supports version 1 of the API, which is deprecated. There is a fork https://github.com/advoninja/python-linkedin/tree/develop which has some updates on the branch`develop`which seems to be more current. However, it was not fully Python 3 compliant.

The only way to get the data we're interested in is to use the [*Full profile* permission](https://docs.microsoft.com/en-us/linkedin/shared/references/v2/profile/full-profile?context=linkedin/consumer/context). This is limited to only reviewed applications by the LinkedIn team.

Getting the profile picture can be done with a projection between the profilePicture to a digitalmediaAsset: `https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~digitalmediaAsset:playableStreams))&oauth2_access_token=` *etc*
