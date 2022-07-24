from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from apps.order.models import Order, User
from apps.product.models import Category, Product


class ReportView(APIView):
    pagination_class = None
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None, *args, **kwargs):
        
        labels = []
        data = []
        dataRadar = []
        totalsolds = 0
        viewsTotal=0
        
        categories = Category.objects.filter(parent__isnull=False)
        products = Product.objects.all()
        
        for category in categories:
            labels.append(category.title)
            items = products.filter(category=category)
            data.append(items.count())
            solds = 0
            for item in items:
                solds += item.sold
                viewsTotal += item.num_visits
            totalsolds += solds
            dataRadar.append(solds)

        orders = Order.objects.all()

        days = [0, 0, 0, 0, 0, 0, 0]

        for orden in orders:
            if orden.date_issued.strftime("%A") == "Monday":
                days[0] += 1
            elif orden.date_issued.strftime("%A") == "Tuesday":
                days[1] += 1
            elif orden.date_issued.strftime("%A") == "Wednesday":
                days[2] += 1
            elif orden.date_issued.strftime("%A") == "Thursday":
                days[3] += 1
            elif orden.date_issued.strftime("%A") == "Friday":
                days[4] += 1
            elif orden.date_issued.strftime("%A") == "Saturday":
                days[5] += 1
            elif orden.date_issued.strftime("%A") == "Sunday":
                days[6] += 1

        return Response(
            {
                "pie": {
                    "labels": labels,
                    "data": data
                },
                "radar": {
                    "labels": labels,
                    "data": dataRadar
                },
                "area": {
                    "labels": ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
                    "data": days
                },
                "general": {
                    "products": products.count(),
                    "orders": orders.count(),
                    "subcategories": categories.count(),
                    "sales_products":totalsolds,
                    "visits": viewsTotal,
                    "clients": User.objects.filter(is_staff=False).count()
                }
            },
            status.HTTP_200_OK
        )
