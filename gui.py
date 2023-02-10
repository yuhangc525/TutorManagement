import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from mysql import MysqlHelper
from utils import Utils

# columns = [, , "联系方式",
#            "家长微信", "接单日期", "信息费",
#            "状态", "出单日期", "接单老师", "备注"]
colData = [
    {"text": "编号", "stretch": True},
    {"text": "家教信息", "stretch": True},
    {"text": "联系方式", "stretch": True},
    {"text": "家长微信", "stretch": True},
    {"text": "接单日期", "stretch": True},
    {"text": "信息费", "stretch": True},
    {"text": "状态", "stretch": True},
    {"text": "出单日期", "stretch": True},
    {"text": "接单老师", "stretch": True},
    {"text": "备注", "stretch": True},
    # {"text": "操作", "stretch": True}
]


class Tutor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill="both", expand=1)

        tv = Tableview(
            master=self,
            coldata=colData,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY
            # stripecolor=(self.style.colors.light)
        )
        # tv.pack(fill=BOTH, expand=YES, pads=10, pady=10)


if __name__ == '__main__':
    mysql = MysqlHelper()
    util = Utils()
    app = ttk.Window("家教管理系统")
    colors = app.style.colors
    tv = Tableview(
        master=app,
        coldata=colData,
        paginated=True,
        searchable=False,
        bootstyle=PRIMARY,
        stripecolor=(colors.light, None),
        pagesize=10,
        # height=20,
        # autofit=True,
        rowdata=util.deal(mysql.selectAll())
    )
    # tv.insert_row(mysql.selectAll())
    bt = ttk.Button()
    bt.pack()
    tv.pack(fill=BOTH, expand=YES, padx = 10, pady = 10)

    # Tutor(app)
    app.mainloop()
