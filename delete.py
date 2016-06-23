#!/usr/bin/env python
import json,sys,re,urllib2

def http_post_gethostid(hostname):
        requrl="http://101.200.210.206/lisa/api_jsonrpc.php"
        values={
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output":"extend",
                "filter":{
                        "host":[hostname]
                }
            },
            "auth": "a0a261a8f2801d774df794a426cdc237",
            "id": 1
            #"auth": "null"
        }
        jdata = json.dumps(values)
        req = urllib2.Request(requrl,jdata)
        req.add_header('Content-Type','application/json-rpc')
        resq = urllib2.urlopen(req)
        content = resq.read()
        return content
response_hostid = http_post_gethostid(sys.argv[1])
decode = json.loads(response_hostid)
hostid = decode["result"][0]["hostid"]



def http_post_delete(idofhost):
        requrl="http://101.200.210.206/lisa/api_jsonrpc.php"
        values={
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": [idofhost],
	    "auth": "a0a261a8f2801d774df794a426cdc237",
            "id": 1
            #"auth": "null"
        }
        jdata = json.dumps(values)
        req = urllib2.Request(requrl,jdata)
        req.add_header('Content-Type','application/json-rpc')
        resq = urllib2.urlopen(req)
        content = resq.read()
        return content
response = http_post_delete(hostid)





filename = open('/etc/zabbix/alertscripts/data.txt','w')
filename.write("done")
filename.close()

