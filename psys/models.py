from django.db import models

# 顧客情報のモデル
class Customer(models.Model):
    customer_code = models.CharField(primary_key=True, max_length=6)  # 顧客コード
    customer_name = models.CharField(max_length=32, blank=True, null=True)  # 顧客名
    customer_telno = models.CharField(max_length=13, blank=True, null=True)  # 電話番号
    customer_postalcode = models.CharField(max_length=8, blank=True, null=True)  # 郵便番号
    customer_address = models.CharField(max_length=40, blank=True, null=True)  # 住所
    discount_rate = models.IntegerField(blank=True, null=True)  # 割引率
    delete_flag = models.IntegerField()  # 削除フラグ

    class Meta:
        db_table = 'customer'  # データベースのテーブル名

    def __str__(self):
        return self.customer_name


# 顧客番号の管理用モデル
class CustomerNumbering(models.Model):
    customer_code = models.IntegerField()  # 顧客コード

    class Meta:
        db_table = 'customer_numbering'


# 従業員情報のモデル
class Employee(models.Model):
    employee_no = models.CharField(primary_key=True, max_length=6)  # 従業員番号
    employee_name = models.CharField(max_length=32, blank=True, null=True)  # 従業員名
    password = models.CharField(max_length=255, blank=True, null=True)  # パスワード

    class Meta:
        db_table = 'employee'


# 商品情報のモデル
class Item(models.Model):
    item_code = models.CharField(primary_key=True, max_length=6)  # 商品コード
    item_name = models.CharField(max_length=32, blank=True, null=True)  # 商品名
    price = models.IntegerField(blank=True, null=True)  # 価格
    stock = models.IntegerField(blank=True, null=True)  # 在庫数

    class Meta:
        db_table = 'item'


# 注文詳細のモデル
class OrderDetails(models.Model):
    order_no = models.OneToOneField('Orders', models.DO_NOTHING, db_column='order_no', primary_key=True)
    item_code = models.ForeignKey(Item, models.DO_NOTHING, db_column='item_code')
    order_num = models.IntegerField(blank=True, null=True)  # 注文数
    order_price = models.IntegerField(blank=True, null=True)  # 注文価格

    class Meta:
        db_table = 'order_details'
        unique_together = (('order_no', 'item_code'),)


class Orders(models.Model):
    order_no = models.CharField(primary_key=True, max_length=6)  # 注文番号
    customer_code = models.ForeignKey(
        Customer, 
        on_delete=models.SET_NULL,  # on_deleteを正しく設定
        db_column='customer_code', 
        blank=True, 
        null=True
    )  # 顧客コード
    employee_no = models.ForeignKey(
        Employee, 
        on_delete=models.SET_NULL,  # on_deleteを正しく設定
        db_column='employee_no', 
        blank=True, 
        null=True
    )  # 従業員番号
    total_price = models.IntegerField(blank=True, null=True)  # 合計金額
    detail_num = models.IntegerField(blank=True, null=True)  # 明細数
    deliver_date = models.DateField(blank=True, null=True)  # 配送日
    order_date = models.DateField(blank=True, null=True)  # 注文日

    class Meta:
        db_table = 'orders'
