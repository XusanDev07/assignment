from django.shortcuts import render, redirect
from app.models import Doktor, Xona, Klient, Xamshira
from app.tgbot import send_messege


def get_doktor(requests):
    dok = Doktor.objects.all().order_by('status')
    return render(requests, 'get_format/doktor_list.html', {'all': dok})


def get_xona(requests):
    xona = Xona.objects.all().order_by('odam_soni')
    return render(requests, 'get_format/doktor_list.html', {'all': xona})


def get_klient(requests, pk=None):
    kl = Klient.objects.all().order_by('status')
    dok = Doktor.objects.all()
    xona = Xona.objects.all()
    xamshira = Xamshira.objects.all()
    ctx = {
        'all': kl,
        "xona": xona,
        "doktor": dok,
        "xamshira": xamshira
    }
    if requests.POST:
        data = requests.POST

        # print(data)
        # nott = 'ism' if 'ism' not in data else 'familiya' if "familiya" not in data else "phone" if "phone" not in data else "doktor" if "doktor" not in data else "xona" if "xona" not in data else ""
        # print(nott)
        # if nott:
        #     print(data, " Xato ")
        #     ctx['error'] = f'{nott} datada bolishi kere'
        #     return render(requests, 'get_format/klient_list.html', ctx)
        try:
            d = Doktor.objects.filter(id=int(data['doktor'])).first()
            x = Xona.objects.filter(id=int(data['xona'])).first()
            h = Xamshira.objects.filter(id=int(data['xamshira'])).first()

            if x.odam_soni > 2 or d.status or h.status:
                ctx['error'] = f'Bular bant'
                return render(requests, 'get_format/klient_list.html', ctx)

            a = Klient.objects.create(
                ism=data['ism'],
                familiya=data['familiya'],
                phone=data['phone'],
                Xona=x,
                Doktor=d,
                Xamshira=h,
            )
        except ValueError:
            ctx['error'] = f'Data toliq emas'
            return render(requests, 'get_format/klient_list.html', ctx)
        send_messege(d.telegramnikname, h.telegramnikname, x, a.ism)

        d.status = True
        d.save()

        x.odam_soni += 1
        x.save()

        h.status = True
        h.save()
        return render(requests, 'get_format/klient_list.html', ctx)
    if pk:
        kpk = Klient.objects.filter(id=pk).first()
        dpk = Doktor.objects.filter(id=kpk.Doktor.id).first()
        xpk = Xona.objects.filter(id=kpk.Xona.id).first()
        hpk = Xamshira.objects.filter(id=kpk.Xamshira.id).first()
        dpk.status = False
        dpk.save()
        hpk.status = False
        hpk.save()
        xpk.odam_soni -= 1
        xpk.save()
        kpk.status = False
        kpk.save()
        # return render(requests, 'get_format/klient_list.html', ctx)
        return redirect('get_klient')
    return render(requests, 'get_format/klient_list.html', ctx)


def get_xamshira(requests):
    xamshira = Xamshira.objects.all().order_by('status')
    return render(requests, 'get_format/xamshira_list.html', {'all': xamshira})


def index(request):
    dok = Doktor.objects.all()
    xona = Xona.objects.all()
    kl = Klient.objects.all()
    xamshira = Xamshira.objects.all()

    ctx = {
        "doktor": len(dok),
        "xona": len(xona),
        "klient": len(kl),
        "xamshira": len(xamshira)
    }

    return render(request, 'index.html', ctx)

