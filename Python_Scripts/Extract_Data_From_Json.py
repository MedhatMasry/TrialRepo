import sys
import json
import os
import argparse


def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)

def get_test_set_campaign_name_and_ids(test_set_path:str):
    # open json file
    # for simplicity I will consider that the test file already downloaded in specific path.
    with open(test_set_path, 'r',encoding='utf-8') as test_file:
      data = test_file.read()
    # load json file
    content = json.loads(data)
    set_output('campaign_name',content["name"])
    set_output('id_list',' '.join(content["executionList"]))
    set_output('test_set_id',content["id"])
    #set_output('trace_file_path',content["executionList"])
    #set_output('test_set_file_path',content["executionList"])
    
    
    return content["name"], content["executionList"], content["id"]

def main(test_set_path:str):
   get_test_set_campaign_name_and_ids(test_set_path)    
   name=os.getenv("FILE_NAME","") 
   if name:
      print(f'{name}={name}')
   else:
      print('Name not given')              

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="The script helps to set the prerequisites for the Offline TraceAnalyzer tool."
    )
    parser.add_argument(
        "--test_set_path",
        "-t1",
        help="a path to the test file.",
    )
    args = parser.parse_args()
    # pass the input arguments to main script.
    main(args.test_set_path)


