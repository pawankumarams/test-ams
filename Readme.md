# PART 2

For this section of the screener, we would like to gain insight into your ability to learn technical topics. Customers will frequently ask for assistance on projects. These requests will require you to learn new topics. This exercise will hopefully give us insight into your approach and aptitude in meeting these customers' needs.

GitHub API Challenge

GitHub has a powerful API that enables developers to easily access GitHub data. Companies often ask us to craft solutions to their specific problems. A common request we receive is for branches to be automatically protected upon creation.

Please create a simple web service that listens for organization events to know when a repository has been created. When the repository is created please automate the protection of the master branch. Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.


## Solution

## Usage
- Install the following:
  - [Python 3](https://www.python.org/downloads/)
  - Python3-pip (https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
    - `pip3 install -r requirements.txt`
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
  - [ngrok](https://dashboard.ngrok.com/get-started)

- export FLASK_APP=app.py
- Start the local web service via `flask run --host=0.0.0.0 &`
- Start the forwarding service via `./ngrok http 5000 &`
- Note the forwarding address (ie. `http://047b-18-136-126-168.ngrok.io/` in the output of the ngrok application)
- python3 main.py --name <reponame>

<!-- markdownlint-disable -->
- Set up a WebHook in the desired GitHub organization [example](https://github.com/organizations/pawankumarams1/settings/hooks)
  - Note that the Payload URL should match the forwarding address from [ngrok](https://abcdef.ngrok.io/apiGitHubWebHook)
  - Select the individual events radio button and check repositories
  - Content type should be application/json
  - Save the Webhook
  - Create a repository
  - See that branch protection and an issue was created for the repo!

 http://ec2-18-136-126-168.ap-southeast-1.compute.amazonaws.com:5000/
  
## Related Documentation
- [GitHub APIv3](https://developer.github.com/v3/)
- [Web Hooks](https://developer.github.com/webhooks/)
- [API Status](https://www.githubstatus.com/)
- [Flask Docs](https://flask.palletsprojects.com/en/2.0.x/)
- [ngrok](https://ngrok.com/docs)
