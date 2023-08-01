from numpy import random
from TP_2_2_GeneradorDistribuido.Metodo_Transformada import ExponencialT, UniformeT
from TP_2_2_GeneradorDistribuido.Metodo_Rechazo import EmpiricaR
from matplotlib import pyplot as plt


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(random.uniform(0, 1))
    return numbers


class Inventory():

    def __init__(self, S: int, s: int, inventory_0: int = 60, backlog_0: int = 0) -> None:
        """
        s :Minimum stock acceptable policy
        S :Reposition stock policy"""
        self.min_stock = s
        self.max_reposition = S
        self.Item_montly_costs = 1
        self.bklog_costs = 5
        self.Item_Order_costs = 3
        self.time = 0
        self.inventory = inventory_0
        self.backlog = backlog_0
        self.montly_inv_check = []
        self.montly_bklog_check = []
        self.montly_order_costs = []
        # (time to next reposition, increment of inventory)
        self.Total_cost = 0

    def inventory_level(self) -> int:
        return self.inventory-self.backlog

    def Check_Inventory(self) -> None:
        """Montly check to register inventory levels
        and make orders to suppliers
        returns: Size of order to suppliers"""
        self.montly_inv_check.append(self.inventory)
        self.montly_bklog_check.append(self.backlog)
        # order to suplier
        order_cost = 0
        next_order = 0
        if self.inventory_level() < self.min_stock:
            next_order = self.max_reposition-self.inventory
            order_cost = 32 + next_order*self.Item_Order_costs  # 32 setup cost
        self.montly_order_costs.append(order_cost)
        return next_order

    def Average_holding_cost(self, m: int) -> float:
        """m :number of month to check the avg cost
        ADVICE: 1 <= m <= round(self.time)"""
        I = sum(self.montly_inv_check[0:m])/m
        return I*self.Item_montly_costs

    def Averge_bklog_cost(self, m: int) -> float:
        """m :number of month to check the avg cost
        ADVICE: 1 <= m <= round(self.time)"""
        I = sum(self.montly_bklog_check[0:m])/m
        return I*self.bklog_costs

    def Run_Program(self) -> None:
        orders_delivered = 0
        items_demand = []
        customer_orders = generador_numpy(10000)
        customer_orders = ExponencialT(customer_orders, 10)
        order_sizes = generador_numpy(10000)
        order_sizes = EmpiricaR(order_sizes, 1, [1/6, 1/3, 1/3, 1/6])
        deliver_lags = generador_numpy(10000)

        order_times = generador_numpy(120)
        order_times = UniformeT(order_times, .5, 1)

        nxt_cust_order = customer_orders.pop(0)
        nxt_check = 1  # 1 check per month
        nxt_items_order = 0
        nxt_delivery = 0

        Z = 0  # size of the order requested to supplier
        # first event is when an order arrive or the first month end
        month_items_demand = 0
        self.time += min(nxt_check, nxt_cust_order)

        while True:
            if self.time == nxt_check:  # monthly check
                Z = self.Check_Inventory()
                items_demand.append(month_items_demand)
                month_items_demand = 0
                if Z > 0:
                    nxt_items_order = self.time+order_times.pop(0)
                nxt_check += 1

            if self.time == nxt_items_order:  # resuply the stock
                self.inventory += Z
                Z = 0
                nxt_items_order = 0

            if self.time == nxt_cust_order:  # customer order items
                o_size = order_sizes.pop(0)
                month_items_demand += o_size
                if self.inventory < o_size:
                    # backlog items will be delivered the next delivery possible
                    self.backlog += o_size
                else:
                    self.inventory -= o_size
                    nxt_delivery = self.time+deliver_lags.pop(0)
                nxt_cust_order = self.time+customer_orders.pop(0)

            if self.time == nxt_delivery:  # delivery time
                orders_delivered += 1
                if self.backlog > self.inventory > 0:
                    dlv_xtras = self.backlog-self.inventory
                    self.backlog -= dlv_xtras
                    self.inventory = 0
                elif self.inventory > self.backlog > 0:
                    self.inventory -= self.backlog
                    self.backlog = 0
                nxt_delivery = 0

            if self.time >= 120.:
                break
            next_events = [x for x in [nxt_check, nxt_cust_order,
                                       nxt_delivery, nxt_items_order] if x > 0]
            self.time = min(next_events)

        # data
        holding_costs = []
        bklog_costs = []
        monthly_total = []
        inv_level = []
        for i in range(len(self.montly_inv_check)):
            holding_costs.append(self.Average_holding_cost(1+i))
            bklog_costs.append(self.Averge_bklog_cost(1+i))
            inv_level.append(
                self.montly_inv_check[i]-self.montly_bklog_check[i])
            # montly inv check es lista
            # montly order costs es la lista

        # graphics
        fig, axs = plt.subplots(
            ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6])

        # nivel de inv
        ax1 = axs[0, 0]
        ax1.set_title("Niveles del inventario")
        ax1.set(xlabel='Mes', ylabel='Cantidad de items')
        ax1.plot(self.montly_inv_check, label='Items en inventario')
        ax1.plot(self.montly_bklog_check, label='Exceso de demanda')
        ax1.plot(inv_level, label='Nivel de inventario')

        # costo promedio
        ax2 = axs[0, 1]
        ax2.set_title("Costos promedios en el tiempo")
        ax2.set(xlabel='Mes', ylabel='Costo promedio en el mes')
        ax2.plot(holding_costs, label='Costo promedio de mantenimiento')
        ax2.plot(bklog_costs, label='Perdida promedio por exceso de demanda')

        # demanda items
        ax3 = axs[1, 0]
        ax3.set_title("Demanda en el tiempo")
        ax3.set(xlabel='Mes', ylabel='Items demandados en el mes')
        ax3.plot(items_demand, label='Items demandados')
        ax3.plot(self.montly_inv_check, label='Items disponibles')

        # costo mensual total
        ax4 = axs[1, 1]
        ax4.set_title("Gastos realizados")
        ax4.set(xlabel='Mes', ylabel='$ gastado')
        ax4.plot(self.montly_order_costs, label='Gasto mensual en reposicion')
        bk_c = []
        h_c = []
        for i in range(len(self.montly_inv_check)):
            h = (self.montly_inv_check[i])*self.Item_montly_costs
            b = (self.montly_bklog_check[i])*self.bklog_costs
            c = self.montly_order_costs[i]
            bk_c.append(b)
            h_c.append(h)
            monthly_total.append((h+b+c))
        ax4.plot(bk_c, label='Gasto mensual por exceso de demanda')
        ax4.plot(h_c, label='Gasto mensual por mantenimiento')
        ax4.plot(monthly_total, label='Total mensual')
        for ax in axs.flat:
            ax.legend()
            ax.set_xlim(left=0, right=120)
        plt.show()
