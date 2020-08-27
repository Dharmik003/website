from django.shortcuts import render
import pickle
import numpy as np
from os.path import abspath


def index(request):

    if request.method == 'POST':
        disbursed_amount = request.POST.get("disbursed_amount")
        asset_cost = request.POST.get("asset_cost")
        ltv = request.POST.get("ltv")
        emp_type = request.POST.get("emp_type")
        m_flag = request.POST.get("m_flag")
        if m_flag.lower() == 'yes' or m_flag.lower() == 'y':
            m_flag = 1
        else:
            m_flag = 0
        a_flag = request.POST.get("a_flag")
        if a_flag.lower() == 'yes' or a_flag.lower() == 'y':
            a_flag = 1
        else:
            a_flag = 0
        p_flag = request.POST.get("p_flag")
        if p_flag.lower() == 'yes' or p_flag.lower() == 'y':
            p_flag = 1
        else:
            p_flag = 0
        d_flag = request.POST.get("d_flag")
        if d_flag.lower() == 'yes' or d_flag.lower() == 'y':
            d_flag = 1
        else:
            d_flag = 0
        pp_flag = request.POST.get("pp_flag")
        if pp_flag.lower() == 'yes' or pp_flag.lower() == 'y':
            pp_flag = 1
        else:
            pp_flag = 0
        performance_score = request.POST.get("performance_score")
        pri_accts = request.POST.get("pri_accts")
        pri_act_accts = request.POST.get("pri_act_accts")
        pri_over = request.POST.get("pri_over")
        pri_current = request.POST.get("pri_current")
        delinq = request.POST.get("delinq")
        acct_age = request.POST.get("acct_age")
        no_inq = request.POST.get("no_inq")

        if(disbursed_amount == '' or asset_cost == '' or ltv == '' or emp_type == '' or m_flag == '' or a_flag == ''
                or p_flag == '' or d_flag == '' or pp_flag == '' or performance_score == '' or pri_accts == ''
                or pri_act_accts == '' or pri_over == '' or pri_current == '' or delinq == ''
                or acct_age == '' or no_inq == ''):
            context = {}
            return render(request, 'homepage/homepage.html', context)

        with open(str(abspath(__file__))[:-8] + r'\model.pkl', 'rb') as f:
            classifier = pickle.load(f)

        data = np.array([[int(disbursed_amount), int(asset_cost), float(ltv), int(emp_type), int(m_flag),
                          int(a_flag), int(p_flag), int(d_flag), int(pp_flag), int(performance_score),
                          int(pri_accts), int(pri_act_accts), int(pri_over), int(pri_current), int(delinq),
                          int(acct_age), int(no_inq)]])

        answer = classifier.predict(data)
        if answer[0] == 1:
            return render(request, 'homepage/approval.html')
        elif answer[0] == 0:
            return render(request, 'homepage/rejection.html')

    context = {}

    return render(request, 'homepage/homepage.html', context)
