from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout as auth_logout
from .models import Employee, Customer, Orders
from .models import Customer
# ホームページのビュー
def index(request):
    return render(request, 'index.html')

# ログインビュー
def login(request):
    if request.method == 'POST':
        employee_no = request.POST['employee_no']
        password = request.POST['password']

        try:
            user = Employee.objects.get(employee_no=employee_no)
            if check_password(password, user.password):
                messages.success(request, f'{user.employee_name}さん、ログイン成功！')
                return redirect('main')  # ホームページなどにリダイレクト
            else:
                messages.error(request, 'パスワードが違います。')
        except Employee.DoesNotExist:
            messages.error(request, 'この社員番号は登録されていません。')

    return render(request, 'login.html')

# ログアウトビュー
def logout(request):
    auth_logout(request)  # セッション情報をクリアしてログアウト
    return redirect('login')

def hello(request):
    return render(request, 'hello.html')

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

# メインページのビュー
def main(request):
    customers = Customer.objects.all()
    return render(request, 'main.html', {'customers': customers})

# 顧客リストを表示するビュー
def customer_list(request):
    # Customerモデルから全データを取得
    customers = Customer.objects.all()

    # 顧客データをテンプレートに渡して表示
    return render(request, 'customer_list.html', {'customers': customers})

# 注文一覧のビュー
def orders_list(request):
    # Ordersモデルから全データを取得
    orders = Orders.objects.all()

    # 注文データをテンプレートに渡して表示
    return render(request, 'orders_list.html', {'orders': orders})

# サインアップビュー
def signup(request):
    if request.method == 'POST':
        employee_no = request.POST['employee_no']
        employee_name = request.POST['employee_name']
        password = make_password(request.POST['password'])  # パスワードをハッシュ化

        # 同じ社員番号がすでに存在するかをチェック
        if Employee.objects.filter(employee_no=employee_no).exists():
            messages.error(request, 'この社員番号はすでに登録されています。')
            return redirect('signup')

        # 新しい社員を登録
        Employee.objects.create(employee_no=employee_no, employee_name=employee_name, password=password)
        messages.success(request, '登録が完了しました。ログインしてください。')
        return redirect('login')

    return render(request, 'signup.html')
