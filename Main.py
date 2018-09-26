from ipwhois import IPWhois
import subprocess
import re


def tracert(name):
    try:
        return subprocess.check_output(r'tracert ' + name, shell=True)
    except subprocess.CalledProcessError:
        print('ошибка tracert')


def who_is(ip):
    try:
        data = IPWhois(ip).lookup_whois()
        return 'ip : ' + ip + '\n' + \
               'ASN : ' + data['asn'] + '\n' + \
               'country : ' + data['asn_country_code'] + '\n' + \
               'provider : ' + data['nets'][0]['description'] + '\n' + \
               'provider address : ' + data['nets'][0]['address'] + '\n'
    except:
        return ip + ' : ASN - None'


def main():
    pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    while True:
        print(r'введите ip/имя сервера')
        s = input()
        if s == 'exit':
            break
        else:
            raw_data = tracert(s).decode('cp866')
            if raw_data:
                res = [who_is(ip) for ip in pattern.findall(raw_data)[1:]]
                for i in range(1, len(res) + 1):
                    print('number :', i)
                    print(res[i - 1])


if __name__ == '__main__':
    main()
