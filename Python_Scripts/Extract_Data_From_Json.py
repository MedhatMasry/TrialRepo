import sys
import json
import requests


def main(path):
    # open json file
    # for simplicity I will consider that the test file already downloaded in specific path.
    with open(path, 'r',encoding='utf-8') as test_file:
      data = test_file.read()
    # data=requests.get(' url of "test_set.json" ').json()

    # load json file
    content = json.loads(data)

    # create a list of dictionaries that contains only the test_sets
    # test_set_list = content["testCaseSet"]

    # #create empty list to hold the test 
    # test_id_list=list()

    # # iterate through the list and only look at test_ids
    # for test_set in test_set_list:
       # test_id_list.append(test_set["id"])

    #for testing, print the test case ids         
    #print(f'Test-Case-Set-List of "{path}"= {[int(i) for i in content["executionList"]]}')
     #for testing, print the test case ids         
    #print(f'Campaign_Name= {content["name"]}')
    
    return content["name"],content["executionList"]
    
    
   
if __name__ == "__main__":
  if len(sys.argv)==1:
    print("Test file must be provided")
  else:
    returned=main(sys.argv[1])
    print(f'Compaign_Name= {returned[0]}')
    print(f'test_set_ids= {returned[1][0]} {returned[1][1]}')
