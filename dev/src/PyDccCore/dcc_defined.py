#-*- coding:utf-8 -*-
'''
Created on 2010-9-4

@author: zdl

定义AVP的各种常量
'''

# 配置文件路径
ETC_PATH = "../src/etc"

# plus 路径
PLUS_PATH = "../src/plugins"

# 日期格式定义
COMPACTTIMEFORMAT = '%Y%m%d%H%M%S'       #例:20090313102835
ISOTIMEFORMAT = '%Y-%m-%d %X'            #例:2009-03-13 10:28:35

# 默认端口
DIAMETE_ADDRESS_PORT = 3868

# 编码进度
ENCODE_DCC_MSG_BEGIN = 'EM10'
ENCODE_DCC_MSG_BODY_BEGIN = 'EM20'
ENCODE_DCC_MSG_BODY_END = 'EM30'
ENCODE_DCC_MSG_HEAD_BEGIN = 'EM40'
ENCODE_DCC_MSG_HEAD_END = 'EM50'
ENCODE_DCC_MSG_END = 'EM60'

ENCODE_DCC_AVP_BEGIN = 'EA10'
ENCODE_DCC_AVP_BODY_BEGIN = 'EA20'
ENCODE_DCC_AVP_BODY_END = 'EA30'
ENCODE_DCC_AVP_HEAD_BEGIN = 'EA40'
ENCODE_DCC_AVP_HEAD_END = 'EA50'
ENCODE_DCC_AVP_END = 'EA60'

# 解码进度
DECODE_DCC_MSG_BEGIN = 'DM10'
DECODE_DCC_MSG_HEAD_BEGIN = 'DM20'
DECODE_DCC_MSG_HEAD_END = 'DM30'
DECODE_DCC_MSG_BODY_BEGIN = 'DM40'
DECODE_DCC_MSG_BODY_END = 'DM50'
DECODE_DCC_MSG_END = 'DM60'

DECODE_DCC_AVP_BEGIN = 'DA10'
DECODE_DCC_AVP_HEAD_BEGIN = 'DA20'
DECODE_DCC_AVP_HEAD_END = 'DA30'
DECODE_DCC_AVP_BODY_BEGIN = 'DA40'
DECODE_DCC_AVP_BODY_END = 'DA50'
DECODE_DCC_AVP_END = 'DA60'

# AVP_FLAGS中的定义
AVP_FLAG_VENDOR = 0x80
AVP_FLAG_MANDATORY = 0x40
AVP_FLAG_PRIVATE = 0x20

# 消息头信息
DMSG_VERSION = 0x01
DMSG_FLAGS_REQUEST = 0x80
DMSG_FLAGS_ANSWER = 0x00
DMSG_FLAGS_PROXIABLE = 0x40
DMSG_FLAGS_ERROR = 0x20
DMSG_FLAGS_TPOTENTIALLY = 0x10
DMSG_APPLICATION_ID = 0x40

# Command-Code定义
CREDIT_CONTROL_REQUEST = (272, 1)  #CCR
CREDIT_CONTROL_ANSWER = (272, 0)  #CCA
RE_AUTH_REQUEST = (258, 1)  #RAR
RE_AUTH_ANSWER = (258, 0)  #RAA
ABORT_SESSION_REQUEST = (274, 1)  #ASR
ABORT_SESSION_ANSWER = (274, 0)  #ASA
DEVICE_WATCHDOG_REQUEST = (280, 1)  #DWR
DEVICE_WATCHDOG_ANSWER = (280, 0)  #DWA
DISCONNECT_PEER_REQUEST = (282, 1)  #DPR
DISCONNECT_PEER_ANSWER = (282, 0)  #DPA
CAPABILITIES_EXCHANGE_REQUEST = (257, 1)  #CER
CAPABILITIES_EXCHANGE_ANSWER = (257, 0)  #CEA

# 返回码定义,需要支持多种协议RC=Result Code
#====================================================================
# 用于通知接入设备鉴权机制需要多轮往返，并且需要一个后续的请求来批准接入。
RC_DIAMETER_MULTI_ROUND_AUTH = 1001

# 请求被成功执行
RC_DIAMETER_SUCCESS = 2001

# 请求被成功执行，但是为了向用户提供服务，还需要额外的过程
RC_DIAMETER_LIMITED_SUCCESS = 2002

# 第一次作主叫（激活储值卡）
RC_FIRST_TIME_CALLING = 2201

# 主叫余额小于最小提醒额。如果同时满足用户快到有效期的通知条件，
# 不使用该返回码，该情况使用2208的返回代码。
RC_BALANCE_HAVE_LITTLE_MONEY = 2202

# 您拨的电话号码需要个人付费，本次呼叫费用将计入您的个人帐户。
RC_INDIVIDUAL_PAYMENT = 2203

# 您的成员帐户被冻结，本次呼叫费用将计入您的个人帐户。
RC_MEMBER_ACCOUNT_FROZEN_CHARGED_TO_INDIVIDUAL_ACCOUNT = 2204

# 您的成员帐户月限额已到达，本次呼叫费用将计入您的个人帐户，
# 但可以享受虚拟专网的优惠费率。
RC_MEMBERACCOUNT_REACHED_MONTHLY_LIMIT_CHARGED_TO_INDIVIDUAL_ACCOUNT = 2205

# 优惠小区标志, 给SCP返回优惠小区标志，SCP可放音通知用户。
RC_FAV_CELLID_FLAG = 2206

# 【C网】在用户的有效期到期前n天（n可以配置），
# OCS通过此结果代码通知SCP报音：您的手机快到有效期了。
# 如果同时满足最小余额提醒的提醒通知条件，不使用该返回码，
# 该情况使用2208的返回代码。
RC_USER_EXPIRING = 2207

# 【C网】在用户的有效期到期前n天，同时用户余额小于最小提醒额，
# OCS通过此结果代码通知SCP报音：您的手机快到有效期了，
# 您的余额已不多，请充值。
RC_USER_EXPIRING_LITTLE_MONEY = 2208

# 无法识别或者不支持此命令码
RC_DIAMETER_COMMAND_UNSUPPORTED = 3001

# 消息无法发送到目的地，可能因为在域(realm)中找不到主机，
# 或者是没有给出目的域(Destination-Realm)
RC_DIAMETER_UNABLE_TO_DELIVER = 3002

# 请求的域(realm)无法识别
RC_DIAMETER_REALM_NOT_SERVED = 3003

# 指定的服务器无法提供指定的服务，Diameter节点应该试图向备选端发送消息
RC_DIAMETER_TOO_BUSY = 3004

# 代理检测到环路
RC_DIAMETER_LOOP_DETECTED = 3005

# 发起者应该将请求直接发送到Redirect-Host中指定的服务器
RC_DIAMETER_REDIRECT_INDICATION = 3006

# 无法支持所要求的应用
RC_DIAMETER_APPLICATION_UNSUPPORTED = 3007

# 消息头中的比特位组合无效，或者其值与命令码中的定义不一致
RC_DIAMETER_INVALID_HDR_BITS = 3008

# 无法识别AVP标志位，或者定义不一致
RC_DIAMETER_INVALID_AVP_BITS = 3009

# 从一个未知端收到CER请求
RC_DIAMETER_UNKNOWN_PEER = 3010

# 鉴权失败，极有可能由于无效密码
RC_DIAMETER_AUTHENTICATION_REJECTED = 4001

# 由于暂时没有空间，无法确保稳定的存储
RC_DIAMETER_OUT_OF_SPACE = 4002

# 该端在选择过程中失败，因此断开了传输连接
RC_ELECTION_LOST = 4003

# OCF根据业务相关限制或约束条件拒绝了业务请求，
# 比如：终端用户帐户余额无法支付业务费用
RC_DIAMETER_END_USER_SERVICE_DENIED = 4010

# 业务被允许但是无需进一步的信用控制（比如：免费业务）
RC_DIAMETER_CREDIT_CONTROL_NOT_APPLICABLE = 4011

# 由于终端用户的账户无法支付业务费用，其请求的业务被拒绝
RC_DIAMETER_CREDIT_LIMIT_REACHED = 4012

# 标有M比特位标记的AVP无法被识别或支持，
# 同时必须在Failed-AVP中携带导致失败的AVP
RC_DIAMETER_AVP_UNSUPPORTED = 5001

# 未知的会话标识(Session-Id)
RC_DIAMETER_UNKNOWN_SESSION_ID = 5002

# 用户未授权，或者业务不允许给用户使用
RC_DIAMETER_AUTHORIZATION_REJECTED = 5003

# AVP包含无效数据，必须在Failed-AVP中携带违规的AVP
RC_DIAMETER_INVALID_AVP_VALUE = 5004

# 没有包含命令码定义中需要的AVP，
# 应该在Failed-AVP中携带缺失的AVP和Vendor-ID
RC_DIAMETER_MISSING_AVP = 5005

# 由于用户占用资源达到限制而无法为请求授权，
# 比如：用户被限制最多使用一个拨号PPP端口，而用户却试图建立第二个PPP连接
RC_DIAMETER_RESOURCES_EXCEEDED = 5006

# AVP相互矛盾，必须在Failed-AVP中携带相互矛盾的AVP
RC_DIAMETER_CONTRADICTING_AVPS = 5007

# 消息中包含不可出现的AVP，必须在Failed-AVP中携带不被允许的AVP
RC_DIAMETER_AVP_NOT_ALLOWED = 5008

# 在消息中AVP重复的次数超过消息所定义的最大次数，
# 必须在Failed-AVP中携带第一个超过允许次数的AVP
RC_DIAMETER_AVP_OCCURS_TOO_MANY_TIMES = 5009

# 当CER消息被接收到时，对等端之间没有支持的公共应用
RC_DIAMETER_NO_COMMON_APPLICATION = 5010

# 版本号不被支持
RC_DIAMETER_UNSUPPORTED_VERSION = 5011

# 请求由于无法表示的原因被拒绝
RC_DIAMETER_UNABLE_TO_COMPLY = 5012

# 在消息头中无法识别的比特位被置1
RC_DIAMETER_INVALID_BIT_IN_HEADER = 5013

# AVP长度无效，必须在Failed-AVP中携带违规的AVP
RC_DIAMETER_INVALID_AVP_LENGTH = 5014

# 消息长度无效
RC_DIAMETER_INVALID_MESSAGE_LENGTH = 5015

# 给出的AVP标志值不被允许，必须在Failed-AVP中携带违规的AVP
RC_DIAMETER_INVALID_AVP_BIT_COMBO = 5016

# 当CER消息被接收到时，对等端之间没有公共的安全机制
RC_DIAMETER_NO_COMMON_SECURITY = 5017

# 指定的用户无法在OCF中找到
RC_DIAMETER_USER_UNKNOWN = 5030

# 由于输入的批价信息不足、错误的AVP组合、AVP的值无法识别或支持，
# 请求的业务无法批价(rating)，必须在Failed-AVP中携带无法成功处
# 理的AVP或者包含供应商标识(Vender-Id)的缺失AVP
RC_DIAMETER_RATING_FAILED = 5031

# 运营商内部定义
#--------------------------------------------------------------------
# 用户未启用
RC_USER_NEVER_OPEN = 4201

# 储值卡未头次使用
RC_NEVER_USED = 4202

# 储值卡进入冷冻期
RC_USER_FROZEN = 4203

# 储值卡已挂失
RC_USER_MISSING_CLAIM = 4204

# 储值卡被封锁
RC_USER_LOCKED = 4205

# 单停呼出
RC_USER_STOPPED_OUT = 4206

# 储值卡超过有效期，进入保留期。双停。
RC_USER_EXPIRED = 4207

# 语音业务已经停止
RC_VOICE_SERVICE_STOPED = 4208

# 无效（号码资源已经回收）
RC_USER_INVALID = 4209

# 黑名单
RC_BLACK_LIST = 4210

# 用户使用的是非预付费电话
RC_NOT_PPS = 4211

# 主叫余额为零或小于零
RC_BALANCE_IS_ZERO = 4212

# 对不起，您拨的电话号码需要个人付费，请查询。
RC_NO_INDIVIDUAL_PAYMENT = 4214

# 对不起，您的成员帐户被冻结。
RC_MEMBER_ACCOUNT_FROZEN = 4216

# 对不起，您的成员帐户月限额已到达。
RC_MEMBERACCOUNT_REACHED_MONTHLY_LIMIT = 4217

# 对不起，您所拨的用户成员帐户被冻结，无法接听您的电话。
RC_CALLED_MEMBER_ACCOUNT_FROZEN = 4220

# 对不起，您所拨的用户成员帐户月限额到达，无法接听您的电话。
RC_CALLED_MEMBER_ACCOUNT_REACHED_MONTHLY_LIMIT = 4221
#====================================================================
