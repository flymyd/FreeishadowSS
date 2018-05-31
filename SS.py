import io,sys,re,base64,urllib.request,json,collections
code_list=[];h4_result=[];info=[];count=-1;server=collections.OrderedDict();configs_dict=[]
all_configs=[{},{},{},{},{},{},{},{},{},{},{},{}]
data="True";a=data==str(True);b=data==str(False)
useless_word_dict={"\n":"","\t\t ":"","</h4>":""," data-lightbox-gallery=\"gallery1\">Click to view QR Code</a>":""," ":"","\"":"","=":":"}
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url='https://my.ishadowx.net/'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
request=urllib.request.Request(url,headers=header)
source_code=urllib.request.urlopen(request).read()
code_list=str(source_code,encoding="utf-8").split('\n')
useless_word_dict={"\n":"","\t\t ":"","</h4>":""," data-lightbox-gallery=\"gallery1\">Click to view QR Code</a>":"","\"":"","=":":"}
for analyze_h4 in code_list:
    if "<h4>" in analyze_h4:
        if "href" in analyze_h4:
            continue
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', analyze_h4)
        h4_result.append(dd)
    if "title=" in analyze_h4:
        h4_result.append(analyze_h4)
useless_word_dict = dict((re.escape(k), v) for k, v in useless_word_dict.items())
pattern = re.compile("|".join(useless_word_dict.keys()))
for iter_str in h4_result:
    iter_str = pattern.sub(lambda m: useless_word_dict[re.escape(m.group(0))], iter_str)
    if ':' in iter_str:
        iter_str=re.sub("\s","",iter_str)
    info.append(iter_str)
for i in range(60):
    if 'IP' in info[i]:
        info[i]=re.sub("IPAddress:","",info[i])
        configs_dict.append({'server':info[i]})
    elif 'Port' in info[i]:
        info[i]=re.sub("Port:", "", info[i])
        configs_dict.append({'server_port':int(info[i])})
    elif 'Password' in info[i]:
        info[i]=re.sub("Password:", "",info[i])
        configs_dict.append({'password':info[i]})
    elif 'Method' in info[i]:
        info[i]=re.sub("Method:", "", info[i])
        configs_dict.append({'method':info[i]})
    elif 'title' in info[i]:
        info[i] = re.sub("title:", "", info[i])
        encodestr=base64.b64encode(info[i].encode('utf-8'))
        strbase64=str(encodestr,'utf-8')
        strbase64=strbase64.replace('==','')
        configs_dict.append({'remarks':info[i],'remarks_base64':strbase64})
    elif 'auth' in info[i]:
        proto=info[i].split(' ')[16]
        obfs=info[i].split(' ')[17]
        configs_dict.append({'protocol':proto,'obfs':obfs})
for i in range(60):
    if i%5==0:
        count+=1
    all_configs[count].update(configs_dict[i])
server['configs']=all_configs
params={"index" : 1,"random" : b,"sysProxyMode" : 2,"shareOverLan" : b,"bypassWhiteList" : b,"localPort" : 1080,"localAuthPassword" : "PxfvWZceF2O90omVOIZC","dns_server" : "1.2.4.8 53,8.8.8.8 53","reconnectTimes" : 2,"randomAlgorithm" : 0,"randomInGroup" : b,"TTL" : 0,"connect_timeout" : 5,"proxyRuleMode" : 0,"proxyEnable" : b,"pacDirectGoProxy" : b,"proxyType" : 0,"proxyHost" : "","proxyPort" : 0,"proxyAuthUser" : "","proxyAuthPass" : "","proxyUserAgent" : "","authUser" : "","authPass" : "","autoBan" : b,"sameHostForSameTarget" : b,"keepVisitTime" : 180,"isHideTips" : b}
server.update(params)
try:
    config_json = open('D:\gui-config.json', 'w')
    config_json.write(json.dumps(server, sort_keys=True, indent=4, separators=(',', ': ')))
except IOError:
    print("Error, cannot write file")
    print("失败，无法写文件")
else:
    print("Success!")
    print("成功！")