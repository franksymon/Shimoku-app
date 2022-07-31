from app import shimoku


class BarChart:
    def bar_chart_vertical(
        self,
        data: dict[list],
        x: str,
        y: list[str],
        x_axis_name: str,
        y_axis_name: str,
        title: str,
        menu_path: str,
        order: int,
        rows_size: int,
        cols_size: int,
        padding: list[int] = "0,0,0,1",
    ):
        shimoku.plt.bar(
            data=data,
            x=x,
            y=y,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name,
            title=title,
            menu_path=menu_path,
            order=order,
            rows_size=rows_size,
            cols_size=cols_size,
            padding=padding,
        )

    def bar_chart_horizontal(
        self,
        data: list[dict],
        x: str,
        y: list[str],
        x_axis_name: str,
        y_axis_name: str,
        title: str,
        menu_path: str,
        order: int,
        rows_size: int,
        cols_size: int,
        padding: list[int] = "0,0,0,1",
    ):
        shimoku.plt.horizontal_barchart(
            data=data,
            x=x,
            y=y,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name,
            title=title,
            menu_path=menu_path,
            order=order,
            rows_size=rows_size,
            cols_size=cols_size,
            padding=padding,
        )

    def bar_chart_zero_center(
        self,
        data: list[dict],
        x: str,
        y: list[str],
        x_axis_name: str,
        y_axis_name: str,
        title: str,
        menu_path: str,
        order: int,
        rows_size: int,
        cols_size: int,
        padding: list[int] = "0,0,0,1",
    ):
        shimoku.plt.zero_centered_barchart(
            data=data,
            x=x,
            y=y,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name,
            title=title,
            menu_path=menu_path,
            order=order,
            rows_size=rows_size,
            cols_size=cols_size,
            padding=padding,
        )


class PieChart:
    def chart_pie(
        self,
        data: dict[list],
        x: str,
        y: str,
        menu_path: str,
        order: int,
        rows_size: int,
        cols_size: int,
        title: str,
    ):
        shimoku.plt.pie(
            data=data,
            x=x,
            y=y,
            menu_path=menu_path,
            order=order,
            rows_size=rows_size,
            cols_size=cols_size,
            title=title,
        )


class LineChart:
    def line_chart(
        self,
        data: list[dict],
        x: str,
        y: list[str],
        x_axis_name: str,
        y_axis_name: str,
        title: str,
        menu_path: str,
        order: int,
        rows_size: int,
        cols_size: int,
        padding: list[int] = "0,0,0,1",
    ):
        shimoku.plt.line(
            data=data,
            x=x,
            y=y,
            x_axis_name=x_axis_name,
            y_axis_name=y_axis_name,
            title=title,
            menu_path=menu_path,
            order=order,
            rows_size=rows_size,
            cols_size=cols_size,
            padding=padding,
        )
