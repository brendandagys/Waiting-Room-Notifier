from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse

from django.core.mail import EmailMessage

from schedule.models import Schedule
from schedule.forms import ScheduleForm

from twilio.rest import Client
from django.conf import settings

import re
import datetime
date = datetime.date.today()
# current_hour = datetime.datetime.now().hour

slots = ['7:00 - 7:15', '7:15 - 7:30', '7:30 - 7:45', '7:45 - 8:00',
         '8:00 - 8:15', '8:15 - 8:30', '8:30 - 8:45', '8:45 - 9:00',
         '9:00 - 9:15', '9:15 - 9:30', '9:30 - 9:45', '9:45 - 10:00',
         '10:00 - 10:15', '10:15 - 10:30', '10:30 - 10:45', '10:45 - 11:00',
         '11:00 - 11:15', '11:15 - 11:30', '11:30 - 11:45', '11:45 - 12:00',
         '12:00 - 12:15', '12:15 - 12:30', '12:30 - 12:45', '12:45 - 13:00',
         '13:00 - 13:15', '13:15 - 13:30', '13:30 - 13:45', '13:45 - 14:00',
         '14:00 - 14:15', '14:15 - 14:30', '14:30 - 14:45', '14:45 - 15:00',
         '15:00 - 15:15', '15:15 - 15:30', '15:30 - 15:45', '15:45 - 16:00',
         '16:00 - 16:15', '16:15 - 16:30', '16:30 - 16:45', '16:45 - 17:00',
         '17:00 - 17:15', '17:15 - 17:30', '17:30 - 17:45', '17:45 - 18:00',
         '18:00 - 18:15', '18:15 - 18:30', '18:30 - 18:45', '18:45 - 19:00', ]

def get_default_json(slot_number):

    if slot_number == 1:
        slot = slots[0]
    elif slot_number == 2:
        slot = slots[1]
    elif slot_number == 3:
        slot = slots[2]
    elif slot_number == 4:
        slot = slots[3]
    elif slot_number == 5:
        slot = slots[4]
    elif slot_number == 6:
        slot = slots[5]
    elif slot_number == 7:
        slot = slots[6]
    elif slot_number == 8:
        slot = slots[7]
    elif slot_number == 9:
        slot = slots[8]
    elif slot_number == 10:
        slot = slots[9]
    elif slot_number == 11:
        slot = slots[10]
    elif slot_number == 12:
        slot = slots[11]
    elif slot_number == 13:
        slot = slots[12]
    elif slot_number == 14:
        slot = slots[13]
    elif slot_number == 15:
        slot = slots[14]
    elif slot_number == 16:
        slot = slots[15]
    elif slot_number == 17:
        slot = slots[16]
    elif slot_number == 18:
        slot = slots[17]
    elif slot_number == 19:
        slot = slots[18]
    elif slot_number == 20:
        slot = slots[19]
    elif slot_number == 21:
        slot = slots[20]
    elif slot_number == 22:
        slot = slots[21]
    elif slot_number == 23:
        slot = slots[22]
    elif slot_number == 24:
        slot = slots[23]
    elif slot_number == 25:
        slot = slots[24]
    elif slot_number == 26:
        slot = slots[25]
    elif slot_number == 27:
        slot = slots[26]
    elif slot_number == 28:
        slot = slots[27]
    elif slot_number == 29:
        slot = slots[28]
    elif slot_number == 30:
        slot = slots[29]
    elif slot_number == 31:
        slot = slots[30]
    elif slot_number == 32:
        slot = slots[31]
    elif slot_number == 33:
        slot = slots[32]
    elif slot_number == 34:
        slot = slots[33]
    elif slot_number == 35:
        slot = slots[34]
    elif slot_number == 36:
        slot = slots[35]
    elif slot_number == 37:
        slot = slots[36]
    elif slot_number == 38:
        slot = slots[37]
    elif slot_number == 39:
        slot = slots[38]
    elif slot_number == 40:
        slot = slots[39]
    elif slot_number == 41:
        slot = slots[40]
    elif slot_number == 42:
        slot = slots[41]
    elif slot_number == 43:
        slot = slots[42]
    elif slot_number == 44:
        slot = slots[43]
    elif slot_number == 45:
        slot = slots[44]
    elif slot_number == 46:
        slot = slots[45]
    elif slot_number == 47:
        slot = slots[46]
    elif slot_number == 48:
        slot = slots[47]

    return {
        'slot': slot,
        'name': '',
        'modality': 'Unspecified',
        'phone': '',
        'email': '',
        'status': 'Not Yet Sent', # Not Yet Sent, Sent, Confirmed
    }


@login_required
def check_for_status_update(request):

    if request.method == 'GET':

        if (Schedule.objects.last() is None) or (Schedule.objects.last().date != datetime.date.today()):
            schedule_object = Schedule()
        else:
            schedule_object = Schedule.objects.all().order_by('-date')[:1][0]

        return JsonResponse({ 'status_1' : schedule_object.slot_1['status'],
                              'status_2' : schedule_object.slot_2['status'],
                              'status_3' : schedule_object.slot_3['status'],
                              'status_4' : schedule_object.slot_4['status'],
                              'status_5' : schedule_object.slot_5['status'],
                              'status_6' : schedule_object.slot_6['status'],
                              'status_7' : schedule_object.slot_7['status'],
                              'status_8' : schedule_object.slot_8['status'],
                              'status_9' : schedule_object.slot_9['status'],
                              'status_10': schedule_object.slot_10['status'],
                              'status_11': schedule_object.slot_11['status'],
                              'status_12': schedule_object.slot_12['status'],
                              'status_13': schedule_object.slot_13['status'],
                              'status_14': schedule_object.slot_14['status'],
                              'status_15': schedule_object.slot_15['status'],
                              'status_16': schedule_object.slot_16['status'],
                              'status_17': schedule_object.slot_17['status'],
                              'status_18': schedule_object.slot_18['status'],
                              'status_19': schedule_object.slot_19['status'],
                              'status_20': schedule_object.slot_20['status'],
                              'status_21': schedule_object.slot_21['status'],
                              'status_22': schedule_object.slot_22['status'],
                              'status_23': schedule_object.slot_23['status'],
                              'status_24': schedule_object.slot_24['status'],
                              'status_25': schedule_object.slot_25['status'],
                              'status_26': schedule_object.slot_26['status'],
                              'status_27': schedule_object.slot_27['status'],
                              'status_28': schedule_object.slot_28['status'],
                              'status_29': schedule_object.slot_29['status'],
                              'status_30': schedule_object.slot_30['status'],
                              'status_31': schedule_object.slot_31['status'],
                              'status_32': schedule_object.slot_32['status'],
                              'status_33': schedule_object.slot_33['status'],
                              'status_34': schedule_object.slot_34['status'],
                              'status_35': schedule_object.slot_35['status'],
                              'status_36': schedule_object.slot_36['status'],
                              'status_37': schedule_object.slot_37['status'],
                              'status_38': schedule_object.slot_38['status'],
                              'status_39': schedule_object.slot_39['status'],
                              'status_40': schedule_object.slot_40['status'],
                              'status_41': schedule_object.slot_41['status'],
                              'status_42': schedule_object.slot_42['status'],
                              'status_43': schedule_object.slot_43['status'],
                              'status_44': schedule_object.slot_44['status'],
                              'status_45': schedule_object.slot_45['status'],
                              'status_46': schedule_object.slot_46['status'],
                              'status_47': schedule_object.slot_47['status'],
                              'status_48': schedule_object.slot_48['status'], })


def handle_patient_responses(request):

    if request.method == 'GET':

        decoder = { 217: 1,
                    94: 2,
                    33: 3,
                    65: 4,
                    210: 5,
                    38: 6,
                    51: 7,
                    176: 8,
                    154: 9,
                    77: 10,
                    66: 11,
                    114: 12,
                    177: 13,
                    111: 14,
                    86: 15,
                    74: 16,
                    104: 17,
                    186: 18,
                    78: 19,
                    37: 20,
                    222: 21,
                    12: 22,
                    75: 23,
                    55: 24,
                    46: 25,
                    57: 26,
                    95: 27,
                    60: 28,
                    59: 29,
                    63: 30,
                    99: 31,
                    170: 32,
                    44: 33,
                    32: 34,
                    61: 35,
                    151: 36,
                    189: 37,
                    147: 38,
                    80: 39,
                    234: 40,
                    85: 41,
                    35: 42,
                    43: 43,
                    202: 44,
                    81: 45,
                    93: 46,
                    228: 47,
                    24: 48 }

        # Get the full URL
        url = request.build_absolute_uri()

        # Split the URL string on '/' and take the number at the end
        form_indicator = int(int(url.split('/')[-2]) / (date.month * date.day))
        form_indicator = decoder[form_indicator]

        schedule_object = Schedule.objects.all().order_by('-date')[:1][0]

        objects = [schedule_object.slot_1, schedule_object.slot_2, schedule_object.slot_3, schedule_object.slot_4,
                   schedule_object.slot_5, schedule_object.slot_6, schedule_object.slot_7, schedule_object.slot_8,
                   schedule_object.slot_9, schedule_object.slot_10, schedule_object.slot_11, schedule_object.slot_12,
                   schedule_object.slot_13, schedule_object.slot_14, schedule_object.slot_15, schedule_object.slot_16,
                   schedule_object.slot_17, schedule_object.slot_18, schedule_object.slot_19, schedule_object.slot_20,
                   schedule_object.slot_21, schedule_object.slot_22, schedule_object.slot_23, schedule_object.slot_24,
                   schedule_object.slot_25, schedule_object.slot_26, schedule_object.slot_27, schedule_object.slot_28,
                   schedule_object.slot_29, schedule_object.slot_30, schedule_object.slot_31, schedule_object.slot_32,
                   schedule_object.slot_33, schedule_object.slot_34, schedule_object.slot_35, schedule_object.slot_36,
                   schedule_object.slot_37, schedule_object.slot_38, schedule_object.slot_39, schedule_object.slot_40,
                   schedule_object.slot_41, schedule_object.slot_42, schedule_object.slot_43, schedule_object.slot_44,
                   schedule_object.slot_45, schedule_object.slot_46, schedule_object.slot_47, schedule_object.slot_48, ]

        objects[form_indicator - 1]['status'] = 'CONFIRMED'

        schedule_object.save()

        return render(request, 'thankyou.html')

@login_required
def schedule(request):

    if request.method == 'GET':

        if (Schedule.objects.last() is None) or (Schedule.objects.last().date != datetime.date.today()):

            form_1  = ScheduleForm(initial=get_default_json(1))
            form_2  = ScheduleForm(initial=get_default_json(2))
            form_3  = ScheduleForm(initial=get_default_json(3))
            form_4  = ScheduleForm(initial=get_default_json(4))
            form_5  = ScheduleForm(initial=get_default_json(5))
            form_6  = ScheduleForm(initial=get_default_json(6))
            form_7  = ScheduleForm(initial=get_default_json(7))
            form_8  = ScheduleForm(initial=get_default_json(8))
            form_9  = ScheduleForm(initial=get_default_json(9))
            form_10 = ScheduleForm(initial=get_default_json(10))
            form_11 = ScheduleForm(initial=get_default_json(11))
            form_12 = ScheduleForm(initial=get_default_json(12))
            form_13 = ScheduleForm(initial=get_default_json(13))
            form_14 = ScheduleForm(initial=get_default_json(14))
            form_15 = ScheduleForm(initial=get_default_json(15))
            form_16 = ScheduleForm(initial=get_default_json(16))
            form_17 = ScheduleForm(initial=get_default_json(17))
            form_18 = ScheduleForm(initial=get_default_json(18))
            form_19 = ScheduleForm(initial=get_default_json(19))
            form_20 = ScheduleForm(initial=get_default_json(20))
            form_21 = ScheduleForm(initial=get_default_json(21))
            form_22 = ScheduleForm(initial=get_default_json(22))
            form_23 = ScheduleForm(initial=get_default_json(23))
            form_24 = ScheduleForm(initial=get_default_json(24))
            form_25 = ScheduleForm(initial=get_default_json(25))
            form_26 = ScheduleForm(initial=get_default_json(26))
            form_27 = ScheduleForm(initial=get_default_json(27))
            form_28 = ScheduleForm(initial=get_default_json(28))
            form_29 = ScheduleForm(initial=get_default_json(29))
            form_30 = ScheduleForm(initial=get_default_json(30))
            form_31 = ScheduleForm(initial=get_default_json(31))
            form_32 = ScheduleForm(initial=get_default_json(32))
            form_33 = ScheduleForm(initial=get_default_json(33))
            form_34 = ScheduleForm(initial=get_default_json(34))
            form_35 = ScheduleForm(initial=get_default_json(35))
            form_36 = ScheduleForm(initial=get_default_json(36))
            form_37 = ScheduleForm(initial=get_default_json(37))
            form_38 = ScheduleForm(initial=get_default_json(38))
            form_39 = ScheduleForm(initial=get_default_json(39))
            form_40 = ScheduleForm(initial=get_default_json(40))
            form_41 = ScheduleForm(initial=get_default_json(41))
            form_42 = ScheduleForm(initial=get_default_json(42))
            form_43 = ScheduleForm(initial=get_default_json(43))
            form_44 = ScheduleForm(initial=get_default_json(44))
            form_45 = ScheduleForm(initial=get_default_json(45))
            form_46 = ScheduleForm(initial=get_default_json(46))
            form_47 = ScheduleForm(initial=get_default_json(47))
            form_48 = ScheduleForm(initial=get_default_json(48))

        else:
            schedule_object = Schedule.objects.all().order_by('-date')[:1][0]

            objects = [schedule_object.slot_1, schedule_object.slot_2, schedule_object.slot_3, schedule_object.slot_4,
                       schedule_object.slot_5, schedule_object.slot_6, schedule_object.slot_7, schedule_object.slot_8,
                       schedule_object.slot_9, schedule_object.slot_10, schedule_object.slot_11, schedule_object.slot_12,
                       schedule_object.slot_13, schedule_object.slot_14, schedule_object.slot_15, schedule_object.slot_16,
                       schedule_object.slot_17, schedule_object.slot_18, schedule_object.slot_19, schedule_object.slot_20,
                       schedule_object.slot_21, schedule_object.slot_22, schedule_object.slot_23, schedule_object.slot_24,
                       schedule_object.slot_25, schedule_object.slot_26, schedule_object.slot_27, schedule_object.slot_28,
                       schedule_object.slot_29, schedule_object.slot_30, schedule_object.slot_31, schedule_object.slot_32,
                       schedule_object.slot_33, schedule_object.slot_34, schedule_object.slot_35, schedule_object.slot_36,
                       schedule_object.slot_37, schedule_object.slot_38, schedule_object.slot_39, schedule_object.slot_40,
                       schedule_object.slot_41, schedule_object.slot_42, schedule_object.slot_43, schedule_object.slot_44,
                       schedule_object.slot_45, schedule_object.slot_46, schedule_object.slot_47, schedule_object.slot_48, ]

            form_1  = ScheduleForm(initial=objects[0])
            form_2  = ScheduleForm(initial=objects[1])
            form_3  = ScheduleForm(initial=objects[2])
            form_4  = ScheduleForm(initial=objects[3])
            form_5  = ScheduleForm(initial=objects[4])
            form_6  = ScheduleForm(initial=objects[5])
            form_7  = ScheduleForm(initial=objects[6])
            form_8  = ScheduleForm(initial=objects[7])
            form_9  = ScheduleForm(initial=objects[8])
            form_10 = ScheduleForm(initial=objects[9])
            form_11 = ScheduleForm(initial=objects[10])
            form_12 = ScheduleForm(initial=objects[11])
            form_13 = ScheduleForm(initial=objects[12])
            form_14 = ScheduleForm(initial=objects[13])
            form_15 = ScheduleForm(initial=objects[14])
            form_16 = ScheduleForm(initial=objects[15])
            form_17 = ScheduleForm(initial=objects[16])
            form_18 = ScheduleForm(initial=objects[17])
            form_19 = ScheduleForm(initial=objects[18])
            form_20 = ScheduleForm(initial=objects[19])
            form_21 = ScheduleForm(initial=objects[20])
            form_22 = ScheduleForm(initial=objects[21])
            form_23 = ScheduleForm(initial=objects[22])
            form_24 = ScheduleForm(initial=objects[23])
            form_25 = ScheduleForm(initial=objects[24])
            form_26 = ScheduleForm(initial=objects[25])
            form_27 = ScheduleForm(initial=objects[26])
            form_28 = ScheduleForm(initial=objects[27])
            form_29 = ScheduleForm(initial=objects[28])
            form_30 = ScheduleForm(initial=objects[29])
            form_31 = ScheduleForm(initial=objects[30])
            form_32 = ScheduleForm(initial=objects[31])
            form_33 = ScheduleForm(initial=objects[32])
            form_34 = ScheduleForm(initial=objects[33])
            form_35 = ScheduleForm(initial=objects[34])
            form_36 = ScheduleForm(initial=objects[35])
            form_37 = ScheduleForm(initial=objects[36])
            form_38 = ScheduleForm(initial=objects[37])
            form_39 = ScheduleForm(initial=objects[38])
            form_40 = ScheduleForm(initial=objects[39])
            form_41 = ScheduleForm(initial=objects[40])
            form_42 = ScheduleForm(initial=objects[41])
            form_43 = ScheduleForm(initial=objects[42])
            form_44 = ScheduleForm(initial=objects[43])
            form_45 = ScheduleForm(initial=objects[44])
            form_46 = ScheduleForm(initial=objects[45])
            form_47 = ScheduleForm(initial=objects[46])
            form_48 = ScheduleForm(initial=objects[47])

        context = { 'date': datetime.date.today(),
                    'form_dict': {'form_1' : form_1,
                                  'form_2' : form_2,
                                  'form_3' : form_3,
                                  'form_4' : form_4,
                                  'form_5' : form_5,
                                  'form_6' : form_6,
                                  'form_7' : form_7,
                                  'form_8' : form_8,
                                  'form_9' : form_9,
                                  'form_10': form_10,
                                  'form_11': form_11,
                                  'form_12': form_12,
                                  'form_13': form_13,
                                  'form_14': form_14,
                                  'form_15': form_15,
                                  'form_16': form_16,
                                  'form_17': form_17,
                                  'form_18': form_18,
                                  'form_19': form_19,
                                  'form_20': form_20,
                                  'form_21': form_21,
                                  'form_22': form_22,
                                  'form_23': form_23,
                                  'form_24': form_24,
                                  'form_25': form_25,
                                  'form_26': form_26,
                                  'form_27': form_27,
                                  'form_28': form_28,
                                  'form_29': form_29,
                                  'form_30': form_30,
                                  'form_31': form_31,
                                  'form_32': form_32,
                                  'form_33': form_33,
                                  'form_34': form_34,
                                  'form_35': form_35,
                                  'form_36': form_36,
                                  'form_37': form_37,
                                  'form_38': form_38,
                                  'form_39': form_39,
                                  'form_40': form_40,
                                  'form_41': form_41,
                                  'form_42': form_42,
                                  'form_43': form_43,
                                  'form_44': form_44,
                                  'form_45': form_45,
                                  'form_46': form_46,
                                  'form_47': form_47,
                                  'form_48': form_48, }}

        return render(request, 'schedule.html', context=context)

    elif request.method == 'POST':

        if 'notify' in request.POST:

            encoder = { 1: date.month * date.day * 217,
                        2: date.month * date.day * 94,
                        3: date.month * date.day * 33,
                        4: date.month * date.day * 65,
                        5: date.month * date.day * 210,
                        6: date.month * date.day * 38,
                        7: date.month * date.day * 51,
                        8: date.month * date.day * 176,
                        9: date.month * date.day * 154,
                        10: date.month * date.day * 77,
                        11: date.month * date.day * 66,
                        12: date.month * date.day * 114,
                        13: date.month * date.day * 177,
                        14: date.month * date.day * 111,
                        15: date.month * date.day * 86,
                        16: date.month * date.day * 74,
                        17: date.month * date.day * 104,
                        18: date.month * date.day * 186,
                        19: date.month * date.day * 78,
                        20: date.month * date.day * 37,
                        21: date.month * date.day * 222,
                        22: date.month * date.day * 12,
                        23: date.month * date.day * 75,
                        24: date.month * date.day * 55,
                        25: date.month * date.day * 46,
                        26: date.month * date.day * 57,
                        27: date.month * date.day * 95,
                        28: date.month * date.day * 60,
                        29: date.month * date.day * 59,
                        30: date.month * date.day * 63,
                        31: date.month * date.day * 99,
                        32: date.month * date.day * 170,
                        33: date.month * date.day * 44,
                        34: date.month * date.day * 32,
                        35: date.month * date.day * 61,
                        36: date.month * date.day * 151,
                        37: date.month * date.day * 189,
                        38: date.month * date.day * 147,
                        39: date.month * date.day * 80,
                        40: date.month * date.day * 234,
                        41: date.month * date.day * 85,
                        42: date.month * date.day * 35,
                        43: date.month * date.day * 43,
                        44: date.month * date.day * 202,
                        45: date.month * date.day * 81,
                        46: date.month * date.day * 93,
                        47: date.month * date.day * 228,
                        48: date.month * date.day * 24, }

            schedule_object = Schedule.objects.all().order_by('-date')[:1][0]

            json_dicts = [schedule_object.slot_1, schedule_object.slot_2, schedule_object.slot_3, schedule_object.slot_4,
                       schedule_object.slot_5, schedule_object.slot_6, schedule_object.slot_7, schedule_object.slot_8,
                       schedule_object.slot_9, schedule_object.slot_10, schedule_object.slot_11, schedule_object.slot_12,
                       schedule_object.slot_13, schedule_object.slot_14, schedule_object.slot_15, schedule_object.slot_16,
                       schedule_object.slot_17, schedule_object.slot_18, schedule_object.slot_19, schedule_object.slot_20,
                       schedule_object.slot_21, schedule_object.slot_22, schedule_object.slot_23, schedule_object.slot_24,
                       schedule_object.slot_25, schedule_object.slot_26, schedule_object.slot_27, schedule_object.slot_28,
                       schedule_object.slot_29, schedule_object.slot_30, schedule_object.slot_31, schedule_object.slot_32,
                       schedule_object.slot_33, schedule_object.slot_34, schedule_object.slot_35, schedule_object.slot_36,
                       schedule_object.slot_37, schedule_object.slot_38, schedule_object.slot_39, schedule_object.slot_40,
                       schedule_object.slot_41, schedule_object.slot_42, schedule_object.slot_43, schedule_object.slot_44,
                       schedule_object.slot_45, schedule_object.slot_46, schedule_object.slot_47, schedule_object.slot_48, ]

            slot     = int(request.POST['form_indicator'][1:]) # Slice it because it begins with '_'
            name     = request.POST['name']
            modality = request.POST['modality']
            phone    = request.POST['phone']
            email    = request.POST['email']

            # Change the indicator to a semi-random number, the 48-set of which change every day, so that no one can meddle
            slot_encoded = encoder[slot]

            # Keep 'there' lower-case when no name is provided in the form.
            if name == 'There':
                name = 'there'

            # Use regex to limit spaces to 1, split the resulting string on whitespaces, then capitalize each segment
            name = ' '.join([x.capitalize() for x in re.sub('\s{2,}', ' ', name).split(' ')])

            slot_json = json_dicts[slot - 1]

            slot_json['status'] = 'Sent'

            schedule_object.save()


            def send_email():

                email_body = """\
    <html>
      <head></head>
      <body style="border-radius: 20px; padding: 1rem; color: black; font-size: 1.1rem; background-color: #d5e9fb">
        <h2>Hello {0},</h2>
        <h3>We are now ready for you!</h3> </br>
        <p>Please use the button below to indicate that you are on your way. Thank you!</p> </br>
        <a href="NBRHCalert.herokuapp.com/{1}/confirm"><input type="button" style="border-radius: 9px; padding: 1rem; margin: 1rem 0; color: white; background-color: #1F45FC;" value="Confirm Appointment"></a>
      </body>
    </html>
    """.format(name, slot_encoded)
                email_message = EmailMessage('Ready for your appointment!', email_body, to=[email])
                email_message.content_subtype = "html" # this is the crucial part
                email_message.send()


            def send_text():
                to = '+1' + phone
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                response = client.messages.create(
                    body='\nHello {0},\n\nWe are now ready for you!\n\nPlease use the link below to indicate that you are on your way.\n\nNBRHCalert.herokuapp.com/{1}/confirm\n\nThank you!'.format(name, slot_encoded),
                    to=to,
                    from_=settings.TWILIO_PHONE_NUMBER)

            if modality == 'Email':
                send_email()
            elif modality == 'Phone':
                send_text()
            elif modality == 'Phone & Email':
                send_email()
                send_text()

        else:

            if Schedule.objects.last() is None:
                schedule_object = Schedule()
                set_default_slots = True

            elif Schedule.objects.last().date == datetime.date.today():
                schedule_object = Schedule.objects.all().order_by('-date')[:1][0]
                set_default_slots = False

            else:
                schedule_object = Schedule()
                set_default_slots = True

            json_dicts = [schedule_object.slot_1, schedule_object.slot_2, schedule_object.slot_3, schedule_object.slot_4,
                       schedule_object.slot_5, schedule_object.slot_6, schedule_object.slot_7, schedule_object.slot_8,
                       schedule_object.slot_9, schedule_object.slot_10, schedule_object.slot_11, schedule_object.slot_12,
                       schedule_object.slot_13, schedule_object.slot_14, schedule_object.slot_15, schedule_object.slot_16,
                       schedule_object.slot_17, schedule_object.slot_18, schedule_object.slot_19, schedule_object.slot_20,
                       schedule_object.slot_21, schedule_object.slot_22, schedule_object.slot_23, schedule_object.slot_24,
                       schedule_object.slot_25, schedule_object.slot_26, schedule_object.slot_27, schedule_object.slot_28,
                       schedule_object.slot_29, schedule_object.slot_30, schedule_object.slot_31, schedule_object.slot_32,
                       schedule_object.slot_33, schedule_object.slot_34, schedule_object.slot_35, schedule_object.slot_36,
                       schedule_object.slot_37, schedule_object.slot_38, schedule_object.slot_39, schedule_object.slot_40,
                       schedule_object.slot_41, schedule_object.slot_42, schedule_object.slot_43, schedule_object.slot_44,
                       schedule_object.slot_45, schedule_object.slot_46, schedule_object.slot_47, schedule_object.slot_48, ]

            # Run this code if a new object has been created
            if set_default_slots == True:

                slot_counter = 0

                for slot_json in json_dicts:
                    slot_json['slot'] = slots[slot_counter]
                    slot_counter+=1

            # Get the specific slot to update based on the POST request
            slot_json = json_dicts[int(request.POST['form_indicator'][1:]) - 1]

            slot_json['slot'] = request.POST['slot']
            slot_json['name'] = request.POST['name'].capitalize()
            slot_json['modality'] = request.POST['modality']
            slot_json['phone'] = request.POST['phone']
            slot_json['email'] = request.POST['email']
            slot_json['status'] = request.POST['status']

            schedule_object.save()

        return HttpResponse()
