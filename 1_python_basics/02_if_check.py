x_value = 2
y_value = 10.4

if x_value == 3:
    print("xは3")

if x_value > 10:
    print("xは10より大きい")
elif x_value > 5:
    print("xは10以下で，5より大きい")
elif x_value > 0 and y_value > 0:
    print("xは10以下で正の数．yも正の数")
else:
    print("すべての条件が満たされなかった．")

print("条件分岐終了")
print("xは {0}, yは {1}".format(x_value,y_value))
print("xを小数点まで書くと {0:f} とか {0:e} となる".format(x_value))

