#code-by-mohamed-salah
#@M77SALAH
try:
	import requests,telebot,time
except:import os;os.system('pip install requests');os.system('pip install telenot');os.system('pip install time')
token=('6397566392:AAEfui9r_owAdx7FHXSN_BcyC7Z2P1TP3B4')
bot = telebot.TeleBot(token)
def check_captcha(url):
    response = requests.get(url).text
    if 'https://www.google.com/recaptcha/api' in response or 'captcha' in response or 'verifyRecaptchaToken' in response or 'grecaptcha' in response or 'www.google.com/recaptcha' in response:
        return True
    else:
        return False
def check_credit_card_payment(url):
    response = requests.get(url)
    if 'stripe' in response.text:
    	return ' Stripe'
    elif 'Cybersource' in response.text:
    	return ' Cybersource'
    elif 'paypal' in response.text:
    	return 'Paypal' 
    elif 'authorize.net' in response.text:
    	return ' authorize'
    elif 'Bluepay' in response.text:
    	return '  Bluepay'
    elif 'Magento' in response.text:
    	return '  Magento'
    elif 'woo' in response.text:
    	return ' Woo'
    elif 'Shopify' in response.text:
    	return '  Shopify'
    elif 'adyan' in response.text or 'Adyen' in response.text:
    	return ' adyan'
    elif 'braintree' in response.text:
    	return '  Barintree'
    elif 'suqare' in response.text:
    	return ' suqare'
    elif 'payflow' in response.text:
    	return ' payflow'
    elif  'payment by' in response.text:
    	return True
    elif "credit card" in response.text:
        return True
    else:
        return False     
def check_cloud_in_website(url):
    response = requests.get(url)
    if 'cloud' in response.text.lower():
        return True
    else:
        return False
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,'<strong>Hello Pro Bot Check Gate\nSend Only Link Gate 🥵</strong>',parse_mode="HTML")
@bot.message_handler(func= lambda m: True)
def mess(message):
	url=message.text
	try:
		c=check_captcha(url)
	except:
		c= 'False'
	co=check_cloud_in_website(url)
	py=check_credit_card_payment(url)
	kg=bot.reply_to(message,f'<strong>[~]-Lodaing.... 🥸</strong>',parse_mode="HTML")
	time.sleep(1)
	msg=[f"[~]- Captcha = {c}",f"[~]- Captcha = {c}\n\n[~]- Cloud = {co}",f"[~]- Captcha = {c}\n\n[~]- Cloud = {co}\n\n[~]- Payment = {py}",f"[~]- Captcha = {c}\n\n[~]- Cloud = {co}\n\n[~]- Payment = {py}\n\n[~]- Bot By = <a href='tg://openmessage?user_id=6689099522'>Hare</a>"]
	time_sleep=0
	for _ in msg:
		bot.edit_message_text(_,message.chat.id, kg.message_id,parse_mode='html')
		time_sleep+=1
		time.sleep(time_sleep)
		

bot.polling(True)