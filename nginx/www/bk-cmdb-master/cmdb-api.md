#������������ƽ̨�ӿ�˵��	

##����˵��
* �������������README.md��
##�������
* �ӿڶ�����post form-data�ķ�ʽ���ݲ���
##�������
* 1�������ʽͳһΪjson
* 2����ȷ����json����ʽһ���������ģ�
```json
{
    code: 0
}
```
* 3�����󷵻�json����ʽһ���������ģ�
```json
{
    "code": "0004",
    "msg": "ApplicationID Illegal",
    "extmsg": "�Ƿ���ҵ��Id"
}
```
##4���ӿ�˵��

###��ѯҵ���б�
* �ӿڵ�ַ��/api/App/getapplist
* ����ʽ��POST
* �����б�
 ��
* ����˵����
* �������ݸ�ʽ��
```json
{
  "code": 0, 
  "data": [
    {
      "ApplicationID": "996", 
      "ApplicationName": "��Դ��", 
      "Creator": "ʾ����˾", 
      "CreateTime": "2016-03-07 15:14:37", 
      "Default": "1", 
      "DeptName": "", 
      "Description": ""
      .....
    }
  ]
}
```



###IP��ѯ����
* �ӿڵ�ַ��/api/Host/gethostlistbyip
* ����ʽ��POST
* �����б�
 ApplicationID	ҵ��ID	��ѡ
 IP	����IP(����IP������IP)	��ѡ

* �������ݸ�ʽ��
```json
{
    "code": 0,
    "data": [
        {
            "ApplicationID": "997",
            "SetID": "1187",
            "ModuleID": "2105",
            "HostID": "1",
            "AssetID": "pc-8caade00023acfa122a5f36aee26ae98",
            "HostName": "a",
            "DeviceClass": "",
            "Operator": "",
            "BakOperator": "",
            "InnerIP": "10.126.84.10",
            "OuterIP": "10.126.84.10",
            "Status": "",
            "CreateTime": "1970-01-01 00:00:00",
            "HardMemo": "",
            "Region": "",
            "OSName": "",
            "IdcName": "",
            "ApplicationName": "bbb",
            "SetName": "",
            "ModuleName": "���л�"
        }
    ]
}
```
###�ֲ�ģ��ID��ѯ����
* �ӿڵ�ַ��/api/Host/getmodulehostlist
* ����ʽ��POST
* �����б�
 ApplicationID	ҵ��ID	��ѡ
 ModuleID	�ֲ�ģ��ID	��ѡ
* �������ݸ�ʽ��
```json
{
    "code": 0,
    "data": [
        {
            "ApplicationID": "997",
            "SetID": "1187",
            "ModuleID": "2105",
            "HostID": "2",
            "AssetID": "pc-e23675fcbe954635f8b860a172b423c3",
            "HostName": "b",
            "DeviceClass": "",
            "Operator": "",
            "BakOperator": "",
            "InnerIP": "10.126.84.11",
            "OuterIP": "10.126.84.11",
            "Status": "",
            "CreateTime": "1970-01-01 00:00:00",
            "Mem": "0",
            "HardMemo": "",
            "Source": "3",
            "OSName": "",
            "IdcName": "",
            "Region": "",
            "ApplicationName": "bbb",
            "SetName": "",
            "ModuleName": "���л�"
        }
    ]
}
```
###�ֲ�SetID��ѯ����
* �ӿڵ�ַ��/api/Host/getsethostlist
* ����ʽ��POST
* �����б�
 ApplicationID	ҵ��ID	��ѡ
 SetID	�ֲ�SetID	��ѡ
* �������ݸ�ʽ��
```json
{
    "code": 0,
    "data": [
        {
            "ApplicationID": "997",
            "SetID": "1187",
            "ModuleID": "2105",
            "HostID": "2",
            "AssetID": "pc-e23675fcbe954635f8b860a172b423c3",
            "HostName": "b",
            "DeviceClass": "",
            "Operator": "",
            "BakOperator": "",
            "InnerIP": "10.126.84.11",
            "OuterIP": "10.126.84.11",
            "Status": "",
            "CreateTime": "1970-01-01 00:00:00",
            "HardMemo": "",
            "Region": "",
            "OSName": "",
            "IdcName": "",
            "ApplicationName": "bbb",
            "SetName": "",
            "ModuleName": "���л�"
        }
    ]
}
```
###ҵ��ID��ѯ����
* �ӿڵ�ַ��/api/Host/getapphostlist
* ����ʽ��POST
* �����б�
ApplicationID	ҵ��ID	��ѡ

* �������ݸ�ʽ��
```json
{
    "code": 0,
    "data": [
        {
            "ApplicationID": "997",
            "SetID": "1187",
            "ModuleID": "2105",
            "HostID": "2",
            "AssetID": "pc-e23675fcbe954635f8b860a172b423c3",
            "HostName": "b",
            "DeviceClass": "",
            "Operator": "",
            "BakOperator": "",
            "InnerIP": "10.126.84.11",
            "OuterIP": "10.126.84.11",
            "Status": "",
            "CreateTime": "1970-01-01 00:00:00",
            "HardMemo": "",
            "Region": "",
            "OSName": "",
            "IdcName": "",
            "ApplicationName": "bbb",
            "SetName": "",
            "ModuleName": "���л�"
        }
    ]
}
```
###����appid��ѯҵ��ķֲ�������
* �����ַ��/api/TopSetModule/getappsetmoduletreebyappid 
* �������˵����
 ApplicationID	ҵ��ID	��ѡ
* ��Ӧ��Ϣ��
�ɹ���
```json
{
    "code": 0,
    "data": {
        "ApplicationID": "997",
        "ApplicationName": "bbb",
        "Creator": "admin",
        "CreateTime": "2016-03-07 15:43:28",
        "Default": "0",
        "DeptName": "ʾ����˾",
        "Description": "",
        "Display": "1",
        "GroupName": "",
        "LifeCycle": "����",
        "Maintainers": "owenlxu;admin",
        "LastTime": "2016-03-08 05:09:42",
        "Level": "2",
        "Owner": "ʾ����˾",
        "ProductPm": "admin",
        "Type": "0",
        "Source": "",
        "CompanyID": "0",
        "BusinessDeptName": "",
        "Children": [
            {
                "SetID": "1187",
                "ApplicationID": "997",
                "Default": "1",
                "Capacity": "0",
                "CreateTime": "1970-01-01 00:00:00",
                "ChnName": "",
                "Description": "",
                "EnviType": "",
                "LastTime": "2016-03-07 15:43:28",
                "ParentID": "0",
                "SetName": "���л���",
                "ServiceStatus": "",
                "Openstatus": "",
                "Children": [
                    {
                        "ModuleID": "2105",
                        "ApplicationID": "997",
                        "BakOperator": "",
                        "CreateTime": "1970-01-01 00:00:00",
                        "Default": "1",
                        "Description": "",
                        "LastTime": "2016-03-07 15:43:28",
                        "ModuleName": "���л�",
                        "Operator": "",
                        "SetID": "1187",
                        "HostNum": 0
                    },
                    {
                        "ModuleID": "2119",
                        "ApplicationID": "997",
                        "BakOperator": "admin",
                        "CreateTime": "2016-03-08 18:36:48",
                        "Default": "0",
                        "Description": "",
                        "LastTime": "2016-03-08 18:36:48",
                        "ModuleName": "aaaa",
                        "Operator": "admin",
                        "SetID": "1187",
                        "HostNum": 0
                    }
                ]
            }
        ]
    }
}
```
###��ѯҵ���µ�����ģ��
* �����ַ��/api/Module/getmodules
* �������˵����
* ApplicationID	ҵ��ID	��ѡ
* ��Ӧ��Ϣ��
�ɹ���
```json
{
    "code": 0,
    "data": [
        "���л�",
        "aaaa"
    ]
}
```
###�����set���Բ�ѯ����
* �����ַ��/api/set/gethostsbyproperty
* �������˵����
ApplicationID	ҵ��ID	��ѡ
SetID	����ID��ѡ�������ָ�	ѡ��
SetEnviType Set�������ͣ�ѡ������,�ָ�	ѡ��
SetServiceStatus Set����״̬��ѡ������,�ָ�	ѡ��
ModuleName	ģ������ѡ������,�ָ�	ѡ��
* ��Ӧ��Ϣ��
�ɹ���
```json
{
    "code": 0,
    "data": [
        {
            "InnerIP": "10.126.84.11",
            "OuterIP": "10.126.84.11",
            "Source": "3",
            "HostID": "2"
        }
    ]
}
```
###�����set���Բ�ѯģ��
* �����ַ��/api/Set/getmodulesbyproperty
* �������˵����
ApplicationID	ҵ��ID	��ѡ
SetID	����ID��ѡ����,�ָ�	ѡ��
SetEnviType Set�������ͣ�ѡ������,�ָ�	ѡ��
SetServiceStatus Set����״̬��ѡ������,�ָ�	ѡ��
* ��Ӧ��Ϣ��
�ɹ���
```json
{
    "code": 0,
    "data": [
        "���л�",
        "aaaa"
    ]
}
```
###��ȡ����set����
* �����ַ��/api/Set/getsetproperty
* �������˵����
��
* ��Ӧ��Ϣ��
```json
{
    "code": 0,
    "data": {
        "SetEnviType": [
            {
                "Property": "2",
                "value": "����4"
            },
            {
                "Property": "3",
                "value": "����4"
            }
        ],
        "SetServiceStatus": [
            {
                "Property": "0",
                "value": "����4"
            },
            {
                "Property": "1",
                "value": "����5"
            },
            {
                "Property": "5",
                "value": "����67"
            },
            {
                "Property": "6",
                "value": "����779"
            }
        ]
    }
}
```

###����set���Ի�ȡset
* �����ַ��/api/Set/getsetsbyproperty
* �������˵����
	ApplicationID	ҵ��ID	��ѡ
	SetEnviType	Set����	�Ǳ�ѡ
	SetServiceStatus	Set����״̬	�Ǳ�ѡ
* ��Ӧ��Ϣ��
```json
{
    "code": 0,
    "data": [
        {
            "SetID": "1187",
            "SetName": "���л���"
        }
    ]
}
```

###��ȡuserName��Ȩ�޵�ҵ��
* �����ַ��/api/App/getappbyuin
* �������˵����
	userName	API�˺�	��ѡ
* ��Ӧ��Ϣ��
 �������ݳɹ���
```json
{
    "code": 0,
    "data": [
        {
            "ApplicationID": "996",
            "ApplicationName": "��Դ��",
            "Creator": "ʾ����˾",
            "CreateTime": "2016-03-07 15:14:37",
            "Default": "1",
            "DeptName": "",
            "Description": "",
            "Display": "1",
            "GroupName": "",
            "LifeCycle": "",
            "Maintainers": "ʾ����˾",
            "LastTime": "2016-03-07 15:14:37",
            "Level": "2",
            "Owner": "ʾ����˾",
            "ProductPm": "",
            "Type": "0",
            "Source": "0",
            "CompanyID": "0",
            "BusinessDeptName": ""
        }
    ]
}
```
###����������
* �����ַ��/api/Host/addHost
* �������˵����
	InnerIP	����IP	��ѡ
	OuterIP	����IP	ѡ��
	HostName	������	ѡ��
	Operator	������	ѡ��
	BakOperator	���ݲ�����	ѡ��
* ��Ӧ��Ϣ��

�������ݳɹ���
```json
 {
  "code": 0, 
  "data": [ ]
 }
```
###ɾ������
* �����ַ��/api/Host/delHost
* �������˵����
InnerIP	����IP	��ѡ
* ��Ӧ��Ϣ��

 �������ݳɹ���
```json
 {
  "code": 0, 
  "data": [ ]
 }
```

###�༭����
* �����ַ��/api/Host/editHost
* �������˵����
InnerIP	����IP	��ѡ
OuterIP	����IP	ѡ��
HostName	������	ѡ��
Operator	������	ѡ��
BakOperator	���ݲ�����	ѡ��
* ��Ӧ��Ϣ��

 �������ݳɹ���
 
```json
 {
  "code": 0, 
  "data": [ ]
 }
```
###������ģ��
* �����ַ��/api/Module/addModule
* �������˵����
AppName	ҵ����	��ѡ
SetName	��Ⱥ��	��ѡ
ModuleName	ģ����	��ѡ
Operator	������	��ѡ
BakOperator	���ݲ�����	��ѡ
* ��Ӧ��Ϣ��

 �������ݳɹ���
```json
 {
  "code": 0, 
  "data": [ ]
 }
```
###ɾ��ģ��
* �����ַ��/api/Module/delModule
* �������˵����
AppName	ҵ����	��ѡ
SetName	��Ⱥ��	��ѡ
ModuleName	ģ����	��ѡ
* ��Ӧ��Ϣ��

 �������ݳɹ���
```json
 {
  "code": 0, 
  "data": [ ]
 }
```
###�༭ģ��
* �����ַ��/api/Module/delModule
* �������˵����
AppName	ҵ����	��ѡ
SetName	��Ⱥ��	��ѡ
ModuleName	��ģ����	��ѡ
newModuleName	�µ�ģ����	ѡ��
Operator	ά����	ѡ��
BakOperator	����ά����	ѡ��
* ��Ӧ��Ϣ��

 �������ݳɹ���
  ```json
 {
  "code": 0, 
  "data": [ ]
}
```


�塢������Ϣ�б�

code	msg	extMsg
* 0001
ApplicationID Illegal
�Ƿ���ҵ��id

* 0002
no app
û��ҵ��

* 0004
user name illegal
�û�id�Ƿ�

* 0005
only default app exsit
ֻ��Ĭ��ҵ��

* 0006
only right to app
ûȨ������ҵ��

* 0011
no host
û������

* 0016
invalid input ApplicationID
ҵ��id������Ч


