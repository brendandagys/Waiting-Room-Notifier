from django.shortcuts import render

from schedule.models import Schedule
# from schedule.forms import ScheduleForm

# Create your views here.
def schedule(request):

    if request.method == 'GET':

        if Schedule.objects.last() is None:
            schedule_object = Schedule()

        elif Schedule.objects.last().date == datetime.date.today():
            schedule_object = Schedule.objects.all().order_by('-date')[:1][0]

        else:
            schedule_object = Schedule()

        date = schedule_object.date

    # 'slot': '',
    # 'name': '',
    # 'modality': '',
    # 'phone': '',
    # 'email': '',
    # 'status': '',

        print(schedule_object.slot_1['slot'])
        # slot_2
        # slot_3
        # slot_4
        # slot_5
        # slot_6
        # slot_7
        # slot_8
        # slot_9
        # slot_10
        # slot_11
        # slot_12
        # slot_13
        # slot_14
        # slot_15
        # slot_16
        # slot_17
        # slot_18
        # slot_19
        # slot_20
        # slot_21
        # slot_22
        # slot_23
        # slot_24
        # slot_25
        # slot_26
        # slot_27
        # slot_28
        # slot_29
        # slot_30
        # slot_31
        # slot_32
        # slot_33
        # slot_34
        # slot_35
        # slot_36
        # slot_37
        # slot_38
        # slot_39
        # slot_40
        # slot_41
        # slot_42
        # slot_43
        # slot_44
        # slot_45
        # slot_46
        # slot_47
        # slot_48
        # slot_49
        # slot_50


        # form = ScheduleForm(request)
