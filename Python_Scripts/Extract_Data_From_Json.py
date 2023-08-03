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
    set_output('campaign_name',content["name"])
    set_output('id_list',content["executionList"])
    set_output('test_set_id',content["id"])
    #set_output('trace_file_path',content["executionList"])
    #set_output('test_set_file_path',content["executionList"])
    
    
    return content["name"],content["executionList"]
    
    
   
if __name__ == "__main__":
  if len(sys.argv)==1:
    print("Test file must be provided")
  else:
    returned=get_campaign_name_and_ids(sys.argv[1])
    print(f'Compaign_Name= {returned[0]}')
    print(f'test_set_ids= {returned[1][0]} {returned[1][1]}')
