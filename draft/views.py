from django.shortcuts import render
from draft.models import Player, Owner, DraftOrder


def home(request):
    return render(request, 'home.html')


def draft(request):
    rookie_qb = Player.objects.filter(year='Rookie', position='QB')
    rookie_rb = Player.objects.filter(year='Rookie', position='RB')
    rookie_wr = Player.objects.filter(year='Rookie', position='WR')
    rookie_te = Player.objects.filter(year='Rookie', position='TE')
    fa_qb = Player.objects.filter(year='FA', position='QB')
    fa_rb = Player.objects.filter(year='FA', position='RB')
    fa_wr = Player.objects.filter(year='FA', position='WR')
    fa_te = Player.objects.filter(year='FA', position='TE')
    draft_order = DraftOrder.objects.all()

    return render(request, 'draft.html', locals())

