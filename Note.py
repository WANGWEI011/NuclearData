import function as f
# note_card()函数的功能是建立存档文件card，备份NJOY输入卡
def note_card(production_path,note_path,nuclide,temp):
    card = production_path + 'Card.njoy'
    card_name = 'card_' + nuclide + '_' + temp + 'K'
    card_i = note_path + 'Card/' + card_name
    f.copyfile(card, card_i)

# note_message()函数的功能是建立存档文件message，备份输入卡和加工过程中的报错信息
def note_message(production_path,note_path,nuclide,temp):
    global message
    card = production_path + 'Card.njoy'
    message_name = 'message_' + nuclide + '_' + temp + 'K'
    message_i = note_path + 'Message/' + message_name
    f.copyfile(card, message_i)
    message = open(message_i, 'a')
    message.write('\n')

def note_message_total():
    return 0;
def xsdir():
    return 0;