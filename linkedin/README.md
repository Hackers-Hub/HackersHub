# LinkedIn API

## Usage

### LinkedIn application
1. Create a LinkedIn application at https://www.linkedin.com/developers/apps/
2. Go to the application's *Auth* tab
  * Make sure that it has the *r_fullprofile* permission
  * Add a redirect url to `http://<yourdomain>/auth`
3. Create a *.env* file that sets up the following environment variables with the application's client id and secret:

```bash
export LINKEDIN_CLIENT_ID="..."
export LINKEDIN_CLIENT_SECRET="..."
```

### Flask application
1. Install the requirements: `make init`
2. Source the environment variables: `source .env`
3. Start the Flask application: `make dev`
4. With you web browser, go to http://localhost:8080 and click on the `auth_url` that is returned. This will redirect you to login with LinkedIn.
5. After logging in, you will be redirected back to the web page, and it will print the profile data that it could access.

