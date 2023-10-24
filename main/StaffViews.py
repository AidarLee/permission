from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from validate_email import validate_email
import smtplib
from django.http import HttpResponseBadRequest, JsonResponse
import json
import time
from django.db import IntegrityError
import numpy as np
from pulp import LpMaximize, LpMinimize, LpProblem, LpStatus, LpVariable, lpSum, value, PULP_CBC_CMD, LpContinuous
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import get_object_or_404
from scipy.optimize import linprog
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q

def staff_home(request):
    return render(request, 'staff_templates/index.html')

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)
    return cur_language

# Получаем выбранный язык
def get_lang(trans):
    if trans == 'en':
        lang = 'English'
    elif trans == 'ky':
        lang = 'Кыргызча'
    else:
        lang = 'Русский'
    return lang

#Contact-us

def send_message(request):
    sucs=True
    if request.method == 'POST':
        
        settings.EMAIL_HOST_USER='csmbishkek@gmail.com'
        settings.EMAIL_HOST_PASSWORD='hswhmrcllyxoqbvx'

        Name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        to_email = 'csmbishkek@gmail.com'
        from_email =request.POST.get('email', '')
        phone = request.POST.get('phone')
        sub = request.POST.get('subject')
        subject = "Сообщение от пользователя, тема - " + sub 
        valid=validate_email(from_email, verify=True)

        if valid==True:
            
            try:
                body = {
                    'Name: ': "От кого: "+ Name, 
                    'from_email': "Эл.адрес: " + from_email,
                    'phone': "Тел:" + phone,
                    'text': "Сообщение: " + message,
                }
                messageAll = "\n".join(body.values())
                send_mail(subject, messageAll, from_email, [to_email],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Неправильный ввод данных')
            except smtplib.SMTPException:
                messages.add_message(request, messages.ERROR, 'Ошибка при отправлении, попробуйте еще раз!')
                return redirect ('contact')
            messages.add_message(request, messages.SUCCESS, 'Ваше сообщение отправлено!')
            return redirect ('contact')
        else:
            messages.add_message(request, messages.ERROR, 'Неправильный эл.адрес')
            
            return redirect ('contact')
    return redirect ('contact')


def about(request):
    context= {

    }

    return render(request, 'client_templates/pages/about.html')

def contact(request):
    context= {

    }

    return render(request, 'client_templates/pages/contact.html')

def product_details(request, id):
        
    product_id = Products.objects.get(id=id)
    fatacids = FatAcidCompositionOfMeal.objects.filter(product=id)
    mineracomp = MineralComposition.objects.filter(product=id)
    amoinacids = AminoAcidComposition.objects.filter(product=id)
    chemicals = Chemicals.objects.filter(product=id)
    context= {
        'product_id': product_id,
        'fatacids': fatacids,
        'mineracomp': mineracomp ,
        'amoinacids': amoinacids,
        'chemicals': chemicals,
    }
        
    return render(request, 'client_templates/pages/details.html',context)

def staff_calc(request):
    pass

#Designing Recips
def meels(request):
    trans = translate(language='ru')
    actual_url = []
    actual_url.append(request.path.split('/')[2])
    actual_url.append(request.path.split('/')[3])
    result = "/".join(actual_url)

    product = Products.objects.all()
    etalon = Products.objects.filter(Category__Name_of_category = "Эталон")
    print(etalon)
    check = False
    region_choices = Regions.objects.filter(language=get_lang(trans))
    hide_ingredients = None

    context= {
        'ingredient': product,
        "hide_result" : check,
        "regions" : region_choices,
        "hide_ingredients" : hide_ingredients,
        "etalon": etalon,
        "actual_url": result,
    }

    return render(request, 'client_templates/pages/meels.html', context)

class Result:

    def __init__(self, 
                 protein, fatacid, carbohydrates, price_100, price_1kg, isolecin, leitsin, valin,
                met_tsist2, fenilalalin_tirosin2, triptofan, lisin, treonin, isolecin2, leitsin2, 
                valin2, met_tsist3, fenilalalin_tirosin3, triptofan2, lisin2, treonin2, isolecin_a,
                leitsin_a, valin_a, met_tsist_a, fenilalalin_tirosin_a, triptofan_a, lisin_a, treonin_a,
                Cmin, power_kkal, power_kDj, kras, bc, U, G, my_time 
                 ):
        self.protein = protein
        self.fatacid = fatacid
        self.carbohydrates = carbohydrates
        self.price_100 = price_100
        self.price_1kg = price_1kg
        self.isolecin = isolecin
        self.leitsin = leitsin
        self.valin = valin
        self.met_tsist2 = met_tsist2
        self. fenilalalin_tirosin2 = fenilalalin_tirosin2
        self.triptofan = triptofan
        self.lisin = lisin
        self.treonin = treonin
        self.isolecin2 = isolecin2
        self.leitsin2 = leitsin2
        self.valin2 = valin2
        self.met_tsist3 = met_tsist3
        self.fenilalalin_tirosin3 = fenilalalin_tirosin3
        self.triptofan2 = triptofan2
        self.lisin2 = lisin2
        self.treonin2 = treonin2
        self.isolecin_a = isolecin_a
        self.leitsin_a = leitsin_a
        self.valin_a = valin_a
        self.met_tsist_a = met_tsist_a
        self.fenilalalin_tirosin_a = fenilalalin_tirosin_a
        self.triptofan_a = triptofan_a
        self.lisin_a = lisin_a
        self.treonin_a = treonin_a
        self.Cmin = Cmin
        self.power_kkal = power_kkal
        self.power_kDj = power_kDj
        self.kras = kras
        self.bc = bc
        self.U = U
        self.G = G
        self.my_time  = my_time 

    def __del__(self):
        print('Деструктор вызван')
        print('Ресурсы освобождены')

def get_recip_id(id):
    recip = Recips.objects.get(id=id)

    return recip

#Ajax Region
def load_courses(request):
    reg = request.GET.get('regionId')
    trans = translate(language='ru')
    ingredient = Products.objects.filter(Category__Region__id = reg, language = get_lang(trans))
    return render(request, 'client_templates/pages/dropdown_list_options.html', {'ingredients': ingredient})

@login_required
#Ajax calculations
def load_calculation(request):

    #Получаем название рецептуры
    recip_name = request.GET.get('Recip')
    #Получаем Регион продукта
    reg = json.loads(request.GET.get(('Regions')))
    #Получаем ID ингредиентов в виде списка
    ingredient = json.loads(request.GET.get('Ingredients'))
    #Получаем массовые доли ингредиентов в виде списка
    mass_fraction = json.loads(request.GET.get('MassFractions'))
    #Получаем цены ингредиентов в виде списка
    price = json.loads(request.GET.get('Prices'))
    #Получаем количество ингредиетов, целое число
    size = request.GET.get('counters')

    regions = Regions.objects.all()
    products = Products.objects.all()
    
    start = time.time()
    res = Result
    result = Result.__dict__

    mass_fractions = 0
    protein = 0.0
    prot = 0
    chemicals_prot = None
    
    chemicals_fat = None
    fatacid = 0
    fat = 0

    chemicals_carbo = None
    carbohydrates = 0
    carbo = 0

    # price.i 
    price_i = 0
    
    #price_1kg * mass_fraction / 1000
    pr = 0

    #price sum
    prplus = 0
    price_100 = 0
    price_1kg = 0

    #isoleicin
    amino_isoleicin = 0
    isol = 0
    isolecin = 0

    #leitsin
    amino_leitsin = 0
    leit = 0
    leitsin = 0

    #valin
    amino_valin = 0
    val = 0
    valin = 0

    #metionin
    amino_met = 0
    met_tsist1 = 0

    #tsistein
    amino_tsistein = 0

    #fenilalalin
    amino_fenilalalin = 0
    fenilanin_tirosin = 0
    fenilalalin_tirosin1 = 0

    #tirosin
    amino_tirosin = 0

    #triptofan
    amino_triptofan = 0
    tripto = 0
    triptofan = 0

    #lisin
    amino_lisin = 0
    lis = 0
    lisin = 0

    #treonin
    amino_treonin = 0
    treon = 0
    treonin = 0

    recip_id = 0

    total_mass_prot = 0

    error_message = "None"

    #Получаем название рецептуры
    recip_name = request.GET.get('Recip')
    #Получаем Регион продукта
    reg = json.loads(request.GET.get(('Regions')))
    #Получаем ID ингредиентов в виде списка
    ingredient = json.loads(request.GET.get('Ingredients'))
    #Получаем массовые доли ингредиентов в виде списка
    mass_fraction = json.loads(request.GET.get('MassFractions'))
    #Получаем цены ингредиентов в виде списка
    price = json.loads(request.GET.get('Prices'))
    #Получаем количество ингредиетов, целое число
    size = request.GET.get('counters')
    aminocaid_comp = None
    if recip_name and reg and ingredient and mass_fraction and price and size:
        for i in range(0, int(size)+1):
            try:
                ing = ingredient[i]
                try:
                    chemical_comp = Chemicals.objects.get(product=ing)
                except Chemicals.DoesNotExist:
                    error_message = "Не удалось найти химический состав ингредиентов, сообщите администратору об ошибке и дождитесь исправления!"
                    return render(request, 'client_templates/pages/load-calculation.html', {"error_message":error_message})
                try:
                    aminocaid_comp = AminoAcidComposition.objects.get(product=ing)
                except AminoAcidComposition.DoesNotExist:
                    error_message = "Не удалось найти аминокислотный состав ингредиентов, сообщите администратору об ошибке и дождитесь исправления!"
                    return render(request, 'client_templates/pages/load-calculation.html', {"error_message":error_message})
                try:
                    mass = 0
                    #Получаем масоовую долю белка в 100г для i-того ингредиента 
                    chemicals_prot = chemical_comp.protein
                    #Получаем масоовую долю i-того ингредиента 
                    mass = float(mass_fraction[i])
                    #Переводим проценты в десятичную дробь mass = mass / 100
                    #Получаем суммарную массовую долю ингредиентов
                    mass_fractions += mass
                    if mass_fractions > 100:
                        error_message = "Общая сумма массовой доли ингредиентов рецептуры не может превышать 100%!"
                        return render(request, 'client_templates/pages/load-calculation.html', {"error_message":error_message})
                    #Получаем масоовую долю белка в массовой доле i-того ингредиента
                    
                    prot += (float(mass) * chemicals_prot)

                    #Получаем цену i-того ингредиента
                    price_i = price[i]
                    #Получаем цену за i[массовая доля] г. ингредиента, т.е. если массовая доля i-того ингредиента равно 30, то получем цену за 30 грамм i-того ингредиента 
                    pr = (float(price_i) * mass) / 1000
                    #Получаем суммарную цену ингредиентов
                    prplus += pr

                    #Получаем масоовую долю жира в 100г для i-того ингредиента 
                    chemicals_fat = chemical_comp.fat
                    fat +=(float(mass)) * chemicals_fat

                    #Получаем масоовую долю углевода в 100г для i-того ингредиента 
                    chemicals_carbo = chemical_comp.carbohydrates
                    carbo +=(float(mass)*chemicals_carbo)

                    #Получаем масоовую долю изолейцина в 100г для i-того ингредиента 
                    amino_isoleicin = aminocaid_comp.izoleitsin 
                    isolecin = (amino_isoleicin * mass * chemicals_prot)
                    isol += isolecin
                    if amino_isoleicin > 0:
                        total_mass_prot += (float(mass) * chemicals_prot)

                    #Получаем масоовую долю лейцина в 100г для i-того ингредиента 
                    amino_leitsin = aminocaid_comp.leitsin
                    leitsin = (amino_leitsin * mass * chemicals_prot)
                    leit += leitsin

                    #Получаем масоовую долю валина в 100г для i-того ингредиента 
                    amino_valin = aminocaid_comp.valin
                    valin = (amino_valin * mass * chemicals_prot)
                    val += valin

                    #Получаем масоовую долю метионина в 100г для i-того ингредиента 
                    amino_met = aminocaid_comp.metionin
                    amino_tsistein = aminocaid_comp.tsistein
                    met_tsist = amino_tsistein + amino_met
                    metionin = (met_tsist * mass * chemicals_prot)
                    met_tsist1 += metionin

                    #Получаем масоовую долю фениланина в 100г для i-того ингредиента 
                    amino_fenilalalin = aminocaid_comp.fenilalalin
                    amino_tirosin = aminocaid_comp.tirosin
                    fenilanin_tirosin = amino_tirosin + amino_fenilalalin
                    fenilanin = (fenilanin_tirosin * mass * chemicals_prot)
                    fenilalalin_tirosin1 += fenilanin

                    #Получаем масоовую долю триптофана в 100г для i-того ингредиента 
                    amino_triptofan = aminocaid_comp.triptofan
                    triptofan = (amino_triptofan * mass * chemicals_prot)
                    tripto += triptofan

                    #Получаем масоовую долю лизина в 100г для i-того ингредиента 
                    amino_lisin = aminocaid_comp.lisin
                    lisin = (amino_lisin * mass * chemicals_prot)
                    lis += lisin

                    #Получаем масоовую долю треонина в 100г для i-того ингредиента 
                    amino_treonin = aminocaid_comp.treonin
                    treonin = (amino_treonin * mass * chemicals_prot)
                    treon += treonin

                except ValueError:
                    error_message = "Поле для массовой доли или цены не могут быть пустыми, пожайлуйста введите значения!"
                    return render(request, 'client_templates/pages/load-calculation.html', {"error_message":error_message})

            except Chemicals.DoesNotExist:
                error_message = "Не удалось найти ингредиент с таким названием!"
                return render(request, 'client_templates/pages/load-calculation.html', {"error_message":error_message})
    else:
        error_message = "Fill in the fields!"
        return render(request, 'client_templates/pages/load-calculation.html', {"error_message":error_message})
    #Содержание белка в суммарной массовой доле рецептуры
    protein = prot / mass_fractions
    #Содержание жира в суммарной массовой доле рецептуры
    fatacid = fat / 100
    #Содержание углевода в суммарной массовой доле рецептуры
    carbohydrates = carbo / 100
    #Стоимость рецептуры за 100 грамм
    price_100 = (prplus * 100) / mass_fractions
    #Стоимость рецептуры за 1 кг
    price_1kg = price_100 * 10

    if total_mass_prot == 0:
        aminocaid_comp = None
    else:
        isol = isol/total_mass_prot
        leit = leit/total_mass_prot
        val = val/total_mass_prot
        met_tsist1 = met_tsist1/total_mass_prot
        fenilalalin_tirosin1 = fenilalalin_tirosin1/total_mass_prot
        tripto = tripto/total_mass_prot
        lis = lis/total_mass_prot
        treon = treon/total_mass_prot
    

    if total_mass_prot == 0:
        aminocaid_comp = None
    else:
        #Аминокислотный скор для изолейцина (шкала ФАО/ВОЗ)
        isolecin2 = (isol / 4) * 100
        #Аминокислотный скор для лейцина (шкала ФАО/ВОЗ)
        leitsin2 = (leit / 7) * 100
        #Аминокислотный скор для валина (шкала ФАО/ВОЗ)
        valin2 = (val / 5) * 100
        #Аминокислотный скор для мет+цист (шкала ФАО/ВОЗ)
        met_tsist3 = (met_tsist1 / 3.5) * 100 
        #Аминокислотный скор для фен+тир (шкала ФАО/ВОЗ)
        fenilalalin_tirosin3 = (fenilalalin_tirosin1 / 6) * 100
        #Аминокислотный скор для триптофана (шкала ФАО/ВОЗ)
        triptofan2 = (tripto / 1) * 100
        #Аминокислотный скор для лизина (шкала ФАО/ВОЗ)
        lisin2 = (lis / 5.5) * 100
        #Аминокислотный скор для треонина (шкала ФАО/ВОЗ)
        treonin2 = (treon / 4) * 100
        #Минимальный из скоров незаменимых аминокислот исследуемого белка
        Cmin = min(isolecin2, leitsin2, valin2, met_tsist3, fenilalalin_tirosin3, triptofan2, lisin2, treonin2)
        
        #Утилитарность изолейцина в белке
        isolecin_a = Cmin/isolecin2
        #Утилитарность лейцина в белке
        leitsin_a = Cmin/leitsin2
        #Утилитарность валина в белке
        valin_a = Cmin/valin2
        #Утилитарность мет+цист в белке
        met_tsist_a = Cmin/met_tsist3
        #Утилитарность фен+тир в белке
        fenilalalin_tirosin_a = Cmin/fenilalalin_tirosin3
        #Утилитарность триптофана в белке
        triptofan_a = Cmin/triptofan2
        #Утилитарность лизина в белке
        lisin_a = Cmin/lisin2
        #Утилитарность треонина в белке
        treonin_a = Cmin/treonin2


        #Сумманая масса незаменимых аминокислот
        sum_M = isol * (1 - isolecin_a) + leit * (1 - leitsin_a) + val * (1 - valin_a) + (met_tsist1 * (1 - met_tsist_a)) + fenilalalin_tirosin1 * (1 - fenilalalin_tirosin_a) + tripto * (1 - triptofan_a) + treon * (1 - treonin_a) + lis * (1 - lisin_a)
        #Коэффициент КРАС - Средняя величина избытка аминакислотного скора
        kras = (isolecin2 - Cmin + leitsin2 - Cmin + valin2 - Cmin + met_tsist3 - Cmin + fenilalalin_tirosin3 - Cmin + triptofan2 - Cmin + lisin2 - Cmin + treonin2 - Cmin) / 8
        #Биологическая ценность пищевого белка
        bc = 100 - kras
        #Коэффициент утилитарности 
        U = (isolecin_a * isol + leitsin_a * leit + valin_a * val + met_tsist_a * met_tsist1 + fenilalalin_tirosin_a * fenilanin_tirosin + triptofan_a * tripto + treonin_a * treon + lisin_a * lis)/(isol + leit + val + met_tsist1 + fenilalalin_tirosin1 + tripto + treon + lis)
        #Коэффициент сопоставимой избыточности
        
        G = sum_M/(Cmin/100)

    #Каллорийность в Ккал
    power_kkal = protein * 4 + fatacid * 9 + carbohydrates * 4
    #Каллорийность в кДж
    power_kDj = protein * 17 + fatacid * 37 + carbohydrates * 4

    stop = time.time()  

    execution_time = stop - start

    #Конвертируем значения в строку и записываем новые переменные, чтобы прочитать через Chart.js
    chart_protein = str(protein)
    chart_fatacid = str(fatacid)
    chart_carbo = str(carbohydrates)
    recip_name = str(recip_name)

    #Записываем все данные в класс
    res.protein = round(protein, 5)
    res.fatacid = round(fatacid, 5)
    res.carbohydrates = round(carbohydrates, 5)
    res.price_100 = round(price_100, 5)
    res.price_1kg = round(price_1kg, 5)
    res.power_kkal = round(power_kkal, 5)
    res.power_kDj = round(power_kDj, 5)
    if total_mass_prot == 0:
        aminocaid_comp = None
    else:
        res.isolecin = round(isol, 5)
        res.isolecin2 = round(isolecin2, 5)
        res.leitsin = round(leit, 5)
        res.leitsin2 = round(leitsin2, 5)
        res.valin = round(val, 5)
        res.valin2 = round(valin2, 5)
        res.met_tsist2 = round(met_tsist1, 5)
        res.met_tsist3 = round(met_tsist3, 5)
        res.fenilalalin_tirosin2 = round(fenilalalin_tirosin1, 5)
        res.fenilalalin_tirosin3 = round(fenilalalin_tirosin3, 5)
        res.triptofan = round(tripto, 5)
        res.triptofan2 = round(triptofan2, 5)
        res.lisin = round(lis, 5)
        res.lisin2 = round(lisin2, 5)
        res.treonin = round(treon, 5)
        res.treonin2 = round(treonin2, 5)
        res.Cmin = round(Cmin, 5)
        res.isolecin_a = round(isolecin_a, 5)
        res.leitsin_a = round(leitsin_a, 5)
        res.valin_a = round(valin_a, 5)
        res.met_tsist_a = round(met_tsist_a, 5)
        res.fenilalalin_tirosin_a = round(fenilalalin_tirosin_a, 5)
        res.triptofan_a = round(triptofan_a, 5)
        res.lisin_a = round(lisin_a, 5)
        res.treonin_a = round(treonin_a, 5)
        res.kras = round(kras, 5)
        res.bc = round(bc, 5)
        res.U = round(U, 5) 
        res.G = round(G, 5)
    res.my_time  = round(execution_time, 5)
    chart_kras = 0
    chart_bc = 0
    chart_U = 0
    chart_G = 0
    if total_mass_prot == 0:
        aminocaid_comp = None
    else:
        #Конвертируем значения в строку и записываем новые переменные, чтобы прочитать через Chart.js
        chart_kras = str(kras)
        chart_bc = str(bc)
        chart_U = str(U)
        chart_G = str(G)
    if total_mass_prot == 0:
            context = {
            'ingredients': products,
            'region' : regions,
            'error_message' : error_message,
            'chemicals' : result,
            'protein':chart_protein,
            'fatacid':chart_fatacid,
            'carbo':chart_carbo,
            'recip_id':recip_id,
            'recip_name': recip_name,
            'counter':str(size),
            'Json_Indredients':ingredient,
            'mass_fractions':mass_fraction,
        }
    else:
        context = {
            'ingredients': products,
            'region' : regions,
            'error_message' : error_message,
            'chemicals' : result,
            'protein':chart_protein,
            'fatacid':chart_fatacid,
            'carbo':chart_carbo,
            'kras':chart_kras,
            'bc':chart_bc,
            'U':chart_U,
            'G':chart_G,
            'recip_id':recip_id,
            'recip_name': recip_name,
            'counter':str(size),
            'Json_Indredients':ingredient,
            'mass_fractions':mass_fraction,
        }
   
    return render(request, 'client_templates/pages/load-calculation.html', context)

def save_view(request):
    user_id = request.user.id
    trans = translate(language='ru')
    try:
        staff_object = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist as e:
        error = "Пользователь не найден!"
        return JsonResponse({'success': False, 'error':error})
    if request.method == 'POST':
        data = json.loads(request.body)

        size = data.get('counter')
        ingredient = data.get('ingred')
        ingredient_list = json.loads(ingredient)
        mass_fraction = data.get('mass_fraction')
        mass_fractions_list = json.loads(mass_fraction)
        table_chemicals = data.get('Table_Chemicals')
        table_chemicals_dict = json.loads(table_chemicals)[1]
        table_price = data.get('Table_Price')
        table_price_dict = json.loads(table_price)[1]

        if staff_object.user_type == "3": 
            table_scor = data.get('Table_Scor')
            table_scor_list = json.loads(table_scor)
        else:
            table_scor_list = []
        table_power = data.get('Table_Power')
        table_power_dict = json.loads(table_power)[1]
        if staff_object.user_type == "3": 
            table_kras = data.get('Table_Kras')
        recip_name = data.get('Recip')

        size = int(size) + 1 

        current_date = date.today()
        try:
            if not Recips.objects.filter(Q(name=recip_name) & Q(staff=user_id)).exists():
                recip_save = Recips(
                    name=recip_name,
                    cost_price_100gramm=float(table_price_dict['Table2_column0'].replace(',', '.')),
                    cost_price_1kg=float(table_price_dict['Table2_column1'].replace(',', '.')),
                    language=get_lang(trans=trans),
                    staff=staff_object,
                    date_analis=current_date
                )
                recip_save.save()
                recip_id = get_recip_id(recip_save.pk)
                if staff_object.user_type == "3": 
                    amino_recip = AminoAcidCompositionRecip(
                        recip=recip_id,
                        izoleitsin=float(table_scor_list[1]['Table3_column0'].replace(',', '.')),
                        leitsin=float(table_scor_list[1]['Table3_column1'].replace(',', '.')),
                        lisin=float(table_scor_list[1]['Table3_column2'].replace(',', '.')),
                        valin=float(table_scor_list[1]['Table3_column3'].replace(',', '.')),
                        metilcistein=float(table_scor_list[1]['Table3_column4'].replace(',', '.')),
                        feniltirosin=float(table_scor_list[1]['Table3_column5'].replace(',', '.')),
                        triptofan=float(table_scor_list[1]['Table3_column6'].replace(',', '.')),
                        treon=float(table_scor_list[1]['Table3_column7'].replace(',', '.')),
                        izoleitsin1=float(table_scor_list[2]['Table3_column0'].replace(',', '.')),
                        leitsin1=float(table_scor_list[2]['Table3_column1'].replace(',', '.')),
                        lisin1=float(table_scor_list[2]['Table3_column2'].replace(',', '.')),
                        valin1=float(table_scor_list[2]['Table3_column3'].replace(',', '.')),
                        metilcistein1=float(table_scor_list[2]['Table3_column4'].replace(',', '.')),
                        feniltirosin1=float(table_scor_list[2]['Table3_column5'].replace(',', '.')),
                        triptofan1=float(table_scor_list[2]['Table3_column6'].replace(',', '.')),
                        treon1=float(table_scor_list[2]['Table3_column7'].replace(',', '.')),
                        izoleitsin_a=float(table_scor_list[3]['Table3_column0'].replace(',', '.')),
                        leitsin_a=float(table_scor_list[3]['Table3_column1'].replace(',', '.')),
                        lisin_a=float(table_scor_list[3]['Table3_column2'].replace(',', '.')),
                        valin_a=float(table_scor_list[3]['Table3_column3'].replace(',', '.')),
                        metilcistein_a=float(table_scor_list[3]['Table3_column4'].replace(',', '.')),
                        feniltirosin_a=float(table_scor_list[3]['Table3_column5'].replace(',', '.')),
                        triptofan_a=float(table_scor_list[3]['Table3_column6'].replace(',', '.')),
                        treon_a=float(table_scor_list[3]['Table3_column7'].replace(',', '.')),
                        c_min=float(table_scor_list[4]['Table3_column0'].replace(',', '.'))
                    )
                    amino_recip.save()
                chemicals_recip = ChemicalsRecip(
                    recip=recip_id,
                    protein=float(table_chemicals_dict['Table1_column0'].replace(',', '.')),
                    fat=float(table_chemicals_dict['Table1_column1'].replace(',', '.')),
                    carbohydrates=float(table_chemicals_dict['Table1_column2'].replace(',', '.')),
                    kkal=float(table_power_dict['Table4_column0'].replace(',', '.')),
                    kJ=float(table_power_dict['Table4_column1'].replace(',', '.'))
                )
                chemicals_recip.save()
                saved_ingredients = []
                
                for i in range(0, int(size)):
                    ing = int(ingredient_list[i])
                    mf = float(mass_fractions_list[i].replace(',', '.'))
                    prod = Products.objects.get(id=ing)
                    ingredient_save = Ingredients(product=prod, mass_fraction=mf, recip=recip_id)
        
                    try:
                        ingredient_save.save()
                        saved_ingredients.append(ingredient_save)
                    except Exception as e:
                        print(f"Ошибка сохранения ингредиента: {e}")

            else:
                return JsonResponse({'success': False, 'error':"Рецепт с таким названием уже существует"})
        except Exception as e:
            return JsonResponse({'success': False, 'error':str(e)})

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error':"Invalid request method"})


def list(request):
    trans = translate(language='ru')
    actual_url = request.path.split('/')[1]
    
    list_of_products = Products.objects.filter(Category__Types__Name_of_type = "Продукт", language = get_lang(trans=trans))
    
    context= {
        'list_of_products':list_of_products,
        'actual_url':actual_url,
    }

    return render(request, 'client_templates/pages/list.html', context)

def recips_list(request):
    actual_url = request.path.split('/')[2]
    user_id = request.user.id
    list_of_recips = Recips.objects.filter(staff = user_id)
    
    context= {
        'list_of_products':list_of_recips,
        'actual_url':actual_url,
    }

    return render(request, 'client_templates/pages/recips_list.html', context)

def recips_detail(request, id):
    user_id = request.user.id
    try:
        staff_object = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist as e:
        error = "Пользователь не найден!"
        return JsonResponse({'success': False, 'error':error})

    actual_url = []
    actual_url.append(request.path.split('/')[2])
    actual_url.append(request.path.split('/')[3])
    result = "/".join(actual_url)
    amoinacids = None
    product_id = Recips.objects.get(id=id)
    if staff_object.user_type == "3": 
        amoinacids = AminoAcidCompositionRecip.objects.get(recip=product_id)
    chemicals = ChemicalsRecip.objects.get(recip=product_id)
    context= {
        'product_id': product_id,
        'amoinacids': amoinacids,
        'chemicals': chemicals,
        "actual_url": result,
    }
        
    return render(request, 'client_templates/pages/recips_details.html',context)
