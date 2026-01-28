from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout as auth_logout
from .models import Employee, Customer, Orders
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q
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

def customer_create(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False) # まだコミット（保存）しない
            customer.delete_flag = 0           # 手動で値をセット
            customer.save()                    # 今度こそ保存
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {
        'form': form,
    })



def customer_update(request, pk):
    customer = Customer.objects.get(pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customer_update.html', {'form': form})  


def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return redirect('customers')        


def orders_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def customer_list(request):
    query = request.GET.get('q')  # フォームからの検索ワードを取得
    if query:
        customers = Customer.objects.filter(
            Q(customer_name__icontains=query) | 
            Q(customer_code__icontains=query) |
            Q(customer_address__icontains=query)
        )
    else:
        customers = Customer.objects.all()

    return render(request, 'customer_list.html', {'customers': customers})

