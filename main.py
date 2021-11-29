import requests
from pprint import pprint
from secret import GITHUB_TOKEN
import argparse

API_URL= "https://api.github.com"
API_PAYLOAD = '{"name":"anotherrepo"}'
ORG_NAME = 'pawankumarams1'
REPO_NAME = 'test'
API_BP_ENDPOINT = "https://api.github.com/repos/pawankumarams1"

BRANCH_PROTECT = '{"required_status_checks":{"strict":true,"contexts":["contexts"]},"enforce_admins":true,"required_pull_request_reviews":{"dismissal_restrictions":{"users":["users"],"teams":["teams"]},"dismiss_stale_reviews":true,"require_code_owner_reviews":true,"required_approving_review_count":2},"restrictions":{"users":["users"],"teams":["teams"],"apps":["apps"]}}'


headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept":"application/vnd.github.v3+json"
}

putheaders ={
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept":"application/vnd.github.luke-cage-preview+json"
}


parser = argparse.ArgumentParser()
parser.add_argument("--name","-n",type=str,dest="name",required=True)
parser.add_argument("--private","-p",dest="is_private",action="store_true")
parser.add_argument("--auto_init","-a",dest='auto_init',action="store_true")

args = parser.parse_args()
print(args)
repo_name = args.name
is_private = args.is_private
auto_init = args.auto_init

if is_private & auto_init:
    payload = '{"name": "' +repo_name + '", "private": true, "auto_init": "true"}'
else:
    payload = '{"name": "' + repo_name + '", "private": false, "auto_init": "true"}'
print(payload)


try:
    #reponse = requests.post(API_URL+"/user/repos",data=payload,headers = headers)
    print(API_URL+"/orgs/"+ORG_NAME+"/"+"repos")
    print(API_BP_ENDPOINT+"/"+repo_name+"/branches/main/protection")
    reponse = requests.post(API_URL+"/orgs/"+ORG_NAME+"/"+"repos",data=payload,headers = headers)
    if(reponse.status_code==201):
        putresponse = requests.put(API_BP_ENDPOINT+"/"+repo_name+"/branches/main/protection",data=BRANCH_PROTECT,headers=putheaders)

    else:
        reponse.raise_for_status()

except requests.exceptions.RequestException as err:
    raise SystemExit(err)


#pprint(response.json())
