import requests
import traceback

def main():
    url_endpoint = 'http://54.236.25.78:4000/api/blueprints/3'

    try:
        raw_response = requests.get(url=url_endpoint)
        response_json = raw_response.json()

        if response_json:
            # project_name = response_json['plan'][0][0]['options']['projectMappings'][0]['projectName']
            # print(project_name)

            project_name = response_json["plan"][1][1]["options"]["name"]
            repo_id = response_json["plan"][1][1]["options"]["repoId"]
            print(project_name)
            print(repo_id)
    except:
        traceback.print_exc()


if __name__ == '__main__':

    try:
        main()
    except (Exception) as e:
        print(e)
