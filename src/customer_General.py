from class_Charts import BarChart, LineChart, PieChart
from class_File import ProccesFile
from utils import create_title, df, df_store

MENU_PATH = "Customer General"


# Customer Characteristicas
# Chart Pie

title_characteristics = create_title(
    "Customer Characteristics",
    "This section shows the total result of the data",
    f"{MENU_PATH}/Characteristics",
    0,
)

branch_data = ProccesFile().chart_pie_data(df, "Branch")
chart_pie_branch = PieChart().chart_pie(
    branch_data, "name", "value", f"{MENU_PATH}/Characteristics", 1, 2, 6, "Branch"
)

city_data = ProccesFile().chart_pie_data(df, "City")
chart_pie_city = PieChart().chart_pie(
    city_data, "name", "value", f"{MENU_PATH}/Characteristics", 2, 2, 6, "City"
)

customer_type_data = ProccesFile().chart_pie_data(df, "Customer type")
chart_pie_customer_type = PieChart().chart_pie(
    customer_type_data,
    "name",
    "value",
    f"{MENU_PATH}/Characteristics",
    3,
    2,
    6,
    "Customer type",
)

gender_data = ProccesFile().chart_pie_data(df, "Gender")
chart_pie_gender = PieChart().chart_pie(
    gender_data, "name", "value", f"{MENU_PATH}/Characteristics", 4, 2, 6, "Gender"
)

payment_data = ProccesFile().chart_pie_data(df, "Payment")
chart_pie_payment = PieChart().chart_pie(
    payment_data, "name", "value", f"{MENU_PATH}/Characteristics", 5, 2, 6, "Payment"
)

product_line_data = ProccesFile().chart_pie_data(df, "Product line")
chart_pie_product_line = PieChart().chart_pie(
    product_line_data,
    "name",
    "value",
    f"{MENU_PATH}/Characteristics",
    6,
    2,
    6,
    "Product line",
)


# # Product sales
# # Bar Chart

product_line_gender_data = ProccesFile().bar_chart_data(
    df, "Product line", "Total", "Gender"
)
chart_bar_product_line_gender = BarChart().bar_chart_vertical(
    product_line_gender_data,
    "name",
    ["Female", "Male"],
    "Product Line",
    "Sum of total",
    "Product sales by product line and by gender",
    f"{MENU_PATH}/Product Sales",
    1,
    2,
    9,
)


product_line_city_data = ProccesFile().bar_chart_data(
    df, "Product line", "Total", "City"
)
chart_bar_product_line_city = BarChart().bar_chart_vertical(
    product_line_city_data,
    "name",
    ["Mandalay", "Naypyitaw", "Yangon"],
    "Product Line",
    "Sum of total",
    "Product sales by product line and by city",
    f"{MENU_PATH}/Product Sales",
    2,
    2,
    9,
)

product_line_customer_type_data = ProccesFile().bar_chart_data(
    df, "Product line", "Total", "Customer type"
)
chart_bar_product_line_customer_type = BarChart().bar_chart_vertical(
    product_line_customer_type_data,
    "name",
    ["Member", "Normal"],
    "Product Line",
    "Sum of total",
    "Product sales by product line and by customer type",
    f"{MENU_PATH}/Product Sales",
    3,
    2,
    9,
)

product_line_payment_data = ProccesFile().bar_chart_data(
    df, "Product line", "Total", "Payment"
)
chart_bar_product_line_payment = BarChart().bar_chart_vertical(
    product_line_payment_data,
    "name",
    ["Cash", "Credit card", "Ewallet"],
    "Product Line",
    "Sum of total",
    "Product sales by product line and by Payment",
    f"{MENU_PATH}/Product Sales",
    4,
    2,
    9,
)

# Product sales by Time
# Bar Chart

ps_months_city_data = ProccesFile().bar_chart_data(df_store, "month", "Total", "City")
chart_bar_ps_months_city = BarChart().bar_chart_vertical(
    ps_months_city_data,
    "name",
    ["Mandalay", "Naypyitaw", "Yangon"],
    "Month",
    "Sum of Total",
    "Product sales by months and by cities",
    f"{MENU_PATH}/Product sales by Time",
    1,
    2,
    9,
)

ps_day_city_data = ProccesFile().bar_chart_data(df_store, "day", "Total", "City")
chart_bar_ps_day_city = BarChart().bar_chart_vertical(
    ps_day_city_data,
    "name",
    ["Mandalay", "Naypyitaw", "Yangon"],
    "Day",
    "Sum of Total",
    "Product sales by days and by cities",
    f"{MENU_PATH}/Product sales by Time",
    2,
    2,
    9,
)

ps_day_customer_type_data = ProccesFile().bar_chart_data(
    df_store, "day", "Total", "Customer type"
)
chart_bar_ps_day_customer_type = BarChart().bar_chart_vertical(
    ps_day_customer_type_data,
    "name",
    ["Member", "Normal"],
    "Day",
    "Sum of Total",
    "Product sales by days and by customer type",
    f"{MENU_PATH}/Product sales by Time",
    3,
    2,
    9,
)


ps_day_gender_data = ProccesFile().bar_chart_data(df_store, "day", "Total", "Gender")
chart_bar_ps_day_gender = BarChart().bar_chart_vertical(
    ps_day_gender_data,
    "name",
    ["Female", "Male"],
    "Day",
    "Sum of Total",
    "Product sales by days and by gender",
    f"{MENU_PATH}/Product sales by Time",
    4,
    2,
    9,
)


ps_hour_gender_data = ProccesFile().bar_chart_data(df_store, "hour", "Total", "Gender")
line_chart_ps_hour_gender = LineChart().line_chart(
    ps_hour_gender_data,
    "name",
    ["Female", "Male"],
    "Hour",
    "Sum of Total",
    "Product sales by the hour and by gender",
    f"{MENU_PATH}/Product sales by Time",
    5,
    2,
    9,
)


# Product sales Quantity
# Bar Line


quantity_product_pl_ct_data = ProccesFile().bar_chart_data(
    df, "Product line", "Quantity", "Customer type"
)
chart_bar_quantity_product_pl_ct = BarChart().bar_chart_vertical(
    quantity_product_pl_ct_data,
    "name",
    ["Member", "Normal"],
    "Product Line",
    "Sum of quantity products",
    "Quantity of products sold by product line and by customer type",
    f"{MENU_PATH}/Products Quantity Sold",
    1,
    2,
    9,
)


quantity_product_pl_city_data = ProccesFile().bar_chart_data(
    df, "Product line", "Quantity", "City"
)
chart_bar_quantity_product_pl_city = BarChart().bar_chart_vertical(
    quantity_product_pl_city_data,
    "name",
    ["Mandalay", "Naypyitaw", "Yangon"],
    "Product Line",
    "Sum of quantity products",
    "Quantity of products sold by product line and by City",
    f"{MENU_PATH}/Products Quantity Sold",
    2,
    2,
    9,
)

quantity_product_pl_gender_data = ProccesFile().bar_chart_data(
    df, "Product line", "Quantity", "Gender"
)
chart_bar_quantity_product_pl_gender = BarChart().bar_chart_vertical(
    quantity_product_pl_gender_data,
    "name",
    ["Female", "Male"],
    "Product Line",
    "Sum of quantity products",
    "Quantity of products sold by product line and by Gender",
    f"{MENU_PATH}/Products Quantity Sold",
    3,
    2,
    9,
)

quantity_product_pl_payment_data = ProccesFile().bar_chart_data(
    df, "Product line", "Quantity", "Payment"
)
chart_bar_quantity_product_pl_payment = BarChart().bar_chart_horizontal(
    quantity_product_pl_payment_data,
    "name",
    ["Cash", "Credit card", "Ewallet"],
    "Product Line",
    "Sum of quantity products",
    "Quantity of products sold by product line and by Payment",
    f"{MENU_PATH}/Products Quantity Sold",
    4,
    2,
    9,
)

# Gross income

quantity_product_pl_gender_data = ProccesFile().bar_chart_data(
    df_store, "month", "gross income", "City"
)
chart_bar_quantity_product_pl_gender = BarChart().bar_chart_horizontal(
    quantity_product_pl_gender_data,
    "name",
    ["Mandalay", "Naypyitaw", "Yangon"],
    "Month",
    "Sum of gross income",
    "Gross income by month and by city",
    f"{MENU_PATH}/Gross Income",
    1,
    2,
    9,
)
