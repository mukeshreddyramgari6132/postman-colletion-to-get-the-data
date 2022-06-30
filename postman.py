import datetime,os,requests,logging,json,time

logging.basicConfig(filename='postman collection44.log', filemode='w', format='%(asctime)s  -  %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
path=input('Enter your folder path: ')
os.chdir(path)
start_time=datetime.datetime.now()
logging.info(start_time)
lst=os.listdir()
count=[]
for j in lst:
    file=open(rf'{path}/{j}')
    data=json.load(file)
    if len(data['item'])>1:
        items=data['item']
    else:
        items=data['item'][0]['item']
    count.append(len(items))

    print(f"Urls count in {j} :{len(items)} \nstarting attack for this file: {j}")
    for i in range(len(items)):

        try:
            print(i,'/',len(items))
            if items[i]['request']['method']=="POST":
                items[i].pop('response')
                header=items[i]['request']['header']
                items[i]['request']['header']={header[i]['key']:header[i]['value'] for i in range(len(header))}
                by=items[i]['request']["body"][items[i]['request']["body"]['mode']]
                items[i]['request']["body"][items[i]['request']["body"]['mode']]={by[i]['key']:by[i]['value'] for i in range(len(by))}
                if 'raw' in items[i]['request']['url']:
                    items[i]['request']['url']=items[i]['request']['url']['raw']
                post_url=items[i]['request']['url']
                post_header=items[i]['request']['header']
                post_body=items[i]['request']["body"][items[i]['request']["body"]['mode']]
                
                # print(f'{post_url} {post_header} {post_body}')
                responses=requests.post(url=post_url,headers=post_header,data=post_body)
                logging.info(f" response: {responses}, url: {post_url}, header: {post_header}, body: {post_body}")
                # logging.info(f"url: {post_url}, header: {post_header}, body: {post_body}")
            if items[i]['request']['method']=="GET":
                items[i].pop('response')
                header=items[i]['request']['header']
                items[i]['request']['header']={header[i]['key']:header[i]['value'] for i in range(len(header))}
                if 'raw' in items[i]['request']['url']:
                    items[i]['request']['url']=items[i]['request']['url']['raw']
                get_url=items[i]['request']['url']
                get_header=items[i]['request']['header']
                
                reponses=requests.get(url=get_url,headers=get_header)
                logging.info(f" response: {reponses}, url: {get_url}, header: {get_header}")
                # logging.info(f"url: {get_url}, header: {get_header}")

        except Exception as err:
            print(err)
print(f'all url counts {sum(count)}')


endtime=datetime.datetime.now()
logging.info(endtime)
logging.info(f'total duration {endtime-start_time}')
logging.info(f'all url counts {sum(count)}')