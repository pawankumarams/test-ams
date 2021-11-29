# PART 1

# Company: Acme computers

*Version control platform(s):* Many GitHub Enterprise instances installed throughout the company by different teams. Acme Computers is trying to standardize on GitHub Enterprise and consolidate their GitHub usage onto a single instance. The company has many instances of other Git hosting solutions installed as well. Some are fully supported applications. Other instances are on machines under people's desks.

## Customer request

* Shrink large repository: Acme wants GitHub to help them shrink the large repository to a more manageable size that is performant for common Git operations. The large repo is a project that is high visibility with an aggressive roadmap. They request that we help them within the month. It's a large, monolithic repository.

## Approach
*Github has helped many customers to shrink the large repository to a more manageable size, to give you a best possible solution, we need to analyse your repos to identify which strategies will be most effective and minimize disruption to the team, The general recommendation is to not have Git repositories larger than 1GB to preserve performance.

Please find below some best practices which helped our customers to achieve their business outcome.

* Separate repositories for large binary files
* Separate build units for consideration to move to separate repositories
* Slow changing sections of the repository for consideration to move to separate repositories
* Large files to move to Git Large File Storage (Git LFS) 


> *References*
> * Reduce Repository Size: https://docs.gitlab.com/ee/user/project/repository/reducing_the_repo_size_using_git.html
> * Removing Large File: https://help.github.com/en/github/managing-large-files/removing-files-from-a-repositorys-history
> * Git Large File Storage (Git LFS): https://docs.gitlab.com/ee/topics/git/lfs/
> * Splitting sub folders into new Repo: https://help.github.com/en/github/using-git/splitting-a-subfolder-out-into-a-new-repository


## Customer request
* Consolidate instances: Acme wants you to tell them the best way to move all the other teams, using GitHub Enterprise or other Git solutions, onto their consolidated GitHub Enterprise instance. They have asked you to give them five or six bullet points about how you would approach that initiative, both technically and culturally.

## Approach
* Assess & Discovery: Conduct team interviews/workshops to understand their current process, branching strategy and concerns
* Planning: Based on team feedback develop a road map that address concerns
* Validate: Setup mirror repositories that are keep in sync in the background
* Backup: Retain your old version control system for a set time after migration.
* Deployment: Move teams in waves to new repositories on an agreed schedule

> *References*
> * Migrating data to and from your enterprise: https://docs.github.com/en/enterprise-server@2.21/admin/user-management/migrating-data-to-and-from-your-enterprise

## Customer request
* Migrate an SVN repo: The customer has one SVN repository that hasn't migrated over to a Git solution. They would like help moving this one large repository over. The team has a trunk based development pattern with this repository and is unfamiliar with Git.


## Approach
* Phase 1 - Setup and maintain a git repo in parallel with the SVN
* Phase 2 - Train the team and move them to git but continue the trunk pattern on master.
* Phase 3 - Additional training and phased migrate the team to a Pull-Request pattern
* Phase 4 - Evaluate options/benefits in dividing up the repo
Note: Order of phase 3/4 can be switched based on company needs

> *References*
> * SVN to Git conversion: https://git-scm.com/docs/git-svn
> * Github Training: https://lab.github.com

***

# Prompt two

# Company: Dunder Mifflin Technologies

*Version control platform(s):* They currently use Gerrit, out-of-the-box Git, Subversion, and Team Foundation Server.

## Customer requests

## Modernize our practices
###  Challenge
* Dunder Mifflin is worried they are falling behind their industry. They have lots of legacy software and development patterns that were created 20 years ago. They have found it incredibly difficult to change any aspect of their SDLC because of their infrastructure, processes, and long-tenured team members who are resistant to change.

### Discussion Points
> * Create a map of current tools & process
> * Identify what is working well and what is not
> * Review what changes have been tried and lessons learned
> * Create an evolutionary plan to move to modern Devops practice

## Release More Often
###  Challenge
* Dunder Mifflin releases software four times a year. They are shipping largely web-based applications. They want to increase more frequently, but they are unsure of the best first steps. What areas would you explore with the customer to help them move this goal forward?

### Discussion Points
> * Identify monolithic repositories/processes that can be divided to improve agility
> * Identify bottlenecks in current process
> * Review State of Continuous Build, Integration Test, look for areas to incorporate

## Commit/merge/deploy permissions
###  Challenge
* Dunder Mifflin has expressed concern about moving away from Gerrit. They have asked how they can control repository access, merging, and deployment permissions within GitHub, and what aspects of their desired security setup can be enforced programmatically.

### Discussion Points
> * Review current rules in place in Gerrit
> * Github features that can be used to address company requirements and evolution
>   * Branch Permissions
>   * Webhooks  
>   * Integrations

> *References*
> * Github Marketplace(Integrations): https://github.com/marketplace
> * Github Webhooks: https://help.github.com/en/github/extending-github/about-webhooks
> * Branch Permissions: https://help.github.com/en/github/administering-a-repository/about-branch-restrictions

***

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

## Related Documentation
- [GitHub APIv3](https://developer.github.com/v3/)
- [Web Hooks](https://developer.github.com/webhooks/)
- [API Status](https://www.githubstatus.com/)
- [Flask Docs](https://flask.palletsprojects.com/en/2.0.x/)
- [ngrok](https://ngrok.com/docs)
