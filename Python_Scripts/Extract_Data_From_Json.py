import sys
import json
import os


def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)

def get_campaign_name_and_ids(path):
    # open json file
    # for simplicity I will consider that the test file already downloaded in specific path.
    with open(path, 'r',encoding='utf-8') as test_file:
      data = test_file.read()
    # load json file
    content = json.loads(data)
    set_output('value1',content["name"])
    set_output('value2',content["executionList"])
    
    return content["name"],content["executionList"]
    
    
   
if __name__ == "__main__":
  if len(sys.argv)==1:
    print("Test file must be provided")
  else:
    returned=get_campaign_name_and_ids(sys.argv[1])
    print(f'Compaign_Name= {returned[0]}')
    print(f'test_set_ids= {returned[1][0]} {returned[1][1]}')
