# -*- coding: utf-8 -*-
import _winreg
import sys

def read_config_file():
    with open('proxy.ini', 'r') as proxy_conf:
        config = proxy_conf.readlines()
    proxy_conf.close()
    return config


def get_proxy_status():
    ie_setting_reg = _winreg.OpenKey(
        _winreg.HKEY_CURRENT_USER,
        "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        )
    proxy_status_key = _winreg.QueryValueEx(ie_setting_reg ,"ProxyEnable")
    _winreg.CloseKey(ie_setting_reg)
    assert type(proxy_status_key[0]) == int
    return proxy_status_key[0]


def toggle_proxy_status(proxy_status, proxy_conf):
    ie_setting_reg = _winreg.OpenKey(
        _winreg.HKEY_CURRENT_USER,
        "Software\Microsoft\Windows\CurrentVersion\Internet Settings",
        0, 
        _winreg.KEY_WRITE 
        ) 
    if proxy_status == 0:
        print u'proxy is disabled'
        proxy_url = 'ftp=' +  proxy_conf + ';http=' + proxy_conf + ';https=' + proxy_conf
        _winreg.SetValueEx(ie_setting_reg, 'ProxyEnable', 0, _winreg.REG_DWORD, 1)
        _winreg.SetValueEx(ie_setting_reg, 'ProxyServer', 0, _winreg.REG_SZ, proxy_url)
        _winreg.SetValueEx(ie_setting_reg, 'ProxyOverride', 0, _winreg.REG_SZ, '<local>')
        print u'proxy enable now!'

    else:
        print u'proxy is enabled'
        _winreg.SetValueEx(ie_setting_reg, 'ProxyEnable', 0, _winreg.REG_DWORD, 0)
        print u'proxy disable now!'

    _winreg.CloseKey(ie_setting_reg)

if __name__ == '__main__':
    proxy = read_config_file()[0].split()[1]
    assert isinstance(proxy, str)
    toggle_proxy_status(get_proxy_status(), proxy)
    print 
    print "Bye"
    print
    raw_input('Press Enter to quit')
    sys.exit()